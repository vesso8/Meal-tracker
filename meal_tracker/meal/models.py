from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from cloudinary import models as cloudinary_models
from django.shortcuts import redirect, render
from django.views import generic as generic_views

from meal_tracker.auth_user.models import AuthUser

UserModel = get_user_model()




class Food(models.Model):
    FOOD_NAME_MAX_LENGTH = 25
    TYPE_OF_FOOD_MAX_LENGTH = 25
    UNITS_MAX_LENGTH = 11
    FRUIT = 'Fruit'
    VEGETABLES = 'Vegetables'
    DAIRY = 'Dairy'
    CARBS = 'Carbs'
    PROTEIN = 'Protein'
    FATS = 'Fats'

    GRAMS = '(gr)'
    KILOGRAMS = '(kg)'
    LITERS = '(l)'
    MILLILITERS = '(ml)'
    PER_PIECE = '(per piece)'

    FOOD_TYPES = [(x, x) for x in [FRUIT, VEGETABLES, DAIRY, CARBS, PROTEIN, FATS]]
    UNITS = [(y, y) for y in [GRAMS, KILOGRAMS, LITERS, MILLILITERS, PER_PIECE]]

    name = models.CharField(
        max_length=FOOD_NAME_MAX_LENGTH
    )
    type_of_food = models.CharField(
        max_length=TYPE_OF_FOOD_MAX_LENGTH,
        choices=FOOD_TYPES,
    )
    quantity = models.PositiveIntegerField(null=False, default=0)
    quantity_units = models.CharField(
        max_length=UNITS_MAX_LENGTH,
        choices=UNITS,
    )
    calorie = models.FloatField(null=False,
                                default=0,
                                validators=(MinValueValidator(0),))
    available_quantity = models.BooleanField(default=True)
    person_of = models.ForeignKey(UserModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def update_new_quantity_and_calories(pk, given_quantity):
        food_selected = Food.objects.get(id=pk)
        quantity_difference = food_selected.quantity - given_quantity
        if quantity_difference == 0:
            calories_difference = 0
            food_selected.available_quantity = False

        elif given_quantity > food_selected.quantity:
            return redirect('calorie counter')
        else:
            calories_difference = round(food_selected.calorie / (food_selected.quantity / quantity_difference))
        food_selected.quantity = quantity_difference
        food_selected.calorie = calories_difference
        food_selected.save()


class Calorie_counter(models.Model):
    person_of = models.ForeignKey(UserModel, null=True, on_delete=models.CASCADE)
    calorie_count = models.FloatField(default=0, null=True, blank=True)
    food_selected = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0,
                                 validators=(MinValueValidator(1),))
    total_calorie = models.FloatField(default=0, null=True)
    date = models.DateField(auto_now_add=True)
    calorie_goal = models.PositiveIntegerField(default=0)
    all_food_selected_today = models.ManyToManyField(Food, through='PostFood', related_name='inventory')

    def save(self, *args, **kwargs):
        if self.food_selected != None:
            self.amount = (self.food_selected.calorie / self.food_selected.quantity)
            self.calorie_count = self.amount * self.quantity
            self.total_calorie = self.calorie_count + self.total_calorie
            self.calorie_count = round(self.calorie_count, 1)
            self.total_calorie = round(self.total_calorie, 1)
            calories = Calorie_counter.objects.filter(person_of=self.person_of).last()
            Food.update_new_quantity_and_calories(self.food_selected.pk ,self.quantity)
            PostFood.objects.create(profile=calories, food=self.food_selected, calories_amount=self.calorie_count,
                                    amount=self.quantity)
            self.food_selected = None

            super(Calorie_counter, self).save(*args, **kwargs)
        else:
            super(Calorie_counter, self).save(*args, **kwargs)
    def clean(self):
        super().clean()
        if self.quantity:
            if self.quantity > self.food_selected.quantity:
                raise ValidationError("There is no enough quantity of this product")
        super(Calorie_counter, self)

    def __str__(self):
        return f'Person: {self.person_of} -Calories: {self.calorie_count}'


class PostFood(models.Model):
    profile = models.ForeignKey(Calorie_counter, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    calories_amount = models.FloatField(default=0, null=True, blank=True)
    amount = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.calories_amount = round(self.calories_amount, 2)
        super(PostFood, self).save(*args, **kwargs)

    def __str__(self):
        return f'Person: {self.profile.person_of} - Food added: {self.food}- Calories: {self.calories_amount}'


class Menu(models.Model):
    TITLE_MAX_LENGTH = 25
    EACH_FOOD_MAX_LENGTH = 50

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
    )
    breakfast = models.CharField(
        max_length=EACH_FOOD_MAX_LENGTH,
    )
    snack_1 = models.CharField(
        max_length=EACH_FOOD_MAX_LENGTH,
        null=True,
        blank=True,
    )
    lunch = models.CharField(
        max_length=EACH_FOOD_MAX_LENGTH,
    )
    snack_2 = models.CharField(
        max_length=EACH_FOOD_MAX_LENGTH,
        null=True,
        blank=True,
    )
    dinner = models.CharField(
        max_length=EACH_FOOD_MAX_LENGTH,
    )
    snack_3 = models.CharField(
        max_length=EACH_FOOD_MAX_LENGTH,
        null=True,
        blank=True,
    )
    image = cloudinary_models.CloudinaryField('image')
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title}'


class Exercise(models.Model):
    MUSCLE_GROUP_MAX_LENGTH = 10
    CHEST = 'Chest'
    BACK = 'Back'
    BICEPS = 'Biceps'
    TRICEPS = 'Triceps'
    ABS = 'Abs'
    LEGS = 'Legs'
    SHOULDERS = 'Shoulders'
    EXERCISE_MAX_LENGTH = 255

    MUSCLE_TYPES = [(x, x) for x in [CHEST, BACK, BICEPS,TRICEPS,  ABS, LEGS, SHOULDERS]]

    muscle_group = models.CharField(
        max_length= MUSCLE_GROUP_MAX_LENGTH,
        choices=MUSCLE_TYPES,
    )
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    image = cloudinary_models.CloudinaryField('image')
    exercise = models.TextField(
        max_length=EXERCISE_MAX_LENGTH,
        null=False
    )
    calories_burned = models.PositiveIntegerField(default=50)
