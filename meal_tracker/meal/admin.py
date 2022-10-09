from django.contrib import admin

from django.contrib import admin

from meal_tracker.meal.models import Food, Calorie_counter, PostFood, Menu, Exercise


@admin.register(Food)
class RegisterFood(admin.ModelAdmin):
    pass


@admin.register(Calorie_counter)
class RegisterCalorieCounter(admin.ModelAdmin):
    pass

@admin.register(PostFood)
class RegisterPostFood(admin.ModelAdmin):
    pass

@admin.register(Menu)
class RegisterMenu(admin.ModelAdmin):
    pass

@admin.register(Exercise)
class RegisterExercise(admin.ModelAdmin):
    pass
