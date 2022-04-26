from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from cloudinary import models as cloudinary_models
from meal_tracker.auth_user.models import AuthUser

UserModel = get_user_model()
class Food(models.Model):
    FOOD_NAME_MAX_LENGTH = 25
    TYPE_OF_FOOD_MAX_LENGTH = 25

    FRUIT = 'Fruit'
    VEGETABLES = 'Vegetables'
    DAIRY = 'Dairy'
    CARBS = 'Carbs'
    PROTEIN = 'Protein'
    FATS = 'Fats'

    FOOD_TYPES = [(x, x) for x in [FRUIT, VEGETABLES, DAIRY, CARBS, PROTEIN, FATS]]


    name = models.CharField(
        max_length=FOOD_NAME_MAX_LENGTH
    )
    type_of_food = models.CharField(
        max_length=TYPE_OF_FOOD_MAX_LENGTH,
        choices=FOOD_TYPES,
    )
    quantity = models.PositiveIntegerField(null=False, default=0)
    calorie = models.FloatField(null=False, default=0)
    person_of = models.ForeignKey(UserModel,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Meal_tracker(models.Model):
    person_of = models.ForeignKey(UserModel, null=True,on_delete=models.CASCADE)
    calorie_count = models.FloatField(default=0, null=True, blank=True)
    food_selected = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.FloatField(default=0)
    total_calorie = models.FloatField(default=0, null=True)
    date = models.DateField(auto_now_add=True)
    calorie_goal = models.PositiveIntegerField(default=0)
    all_food_selected_today = models.ManyToManyField(Food, through='PostFood', related_name='inventory')

    def save(self, *args, **kwargs):
        if self.food_selected != None:
            self.amount = (self.food_selected.calorie/self.food_selected.quantity)
            self.calorie_count = self.amount*self.quantity
            self.total_calorie = self.calorie_count + self.total_calorie
            self.calorie_count = round(self.calorie_count, 1)
            self.total_calorie = round(self.total_calorie, 1)
            calories = Meal_tracker.objects.filter(person_of=self.person_of).last()
            PostFood.objects.create(profile=calories, food=self.food_selected,calories_amount=self.calorie_count,amount=self.quantity)
            self.food_selected = None
            super(Meal_tracker, self).save(*args, **kwargs)
        else:
            super(Meal_tracker, self).save(*args, **kwargs)
    def __str__(self):
        return f'Person: {self.person_of} -Calories: {self.calorie_count}'

class PostFood(models.Model):
    profile = models.ForeignKey(Meal_tracker, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    calories_amount = models.FloatField(default=0,null=True,blank=True)
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
    calories = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

