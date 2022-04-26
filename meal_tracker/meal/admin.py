from django.contrib import admin

from django.contrib import admin

from meal_tracker.meal.models import Food, Meal_tracker, PostFood, Menu


@admin.register(Food)
class RegisterFood(admin.ModelAdmin):
    pass


@admin.register(Meal_tracker)
class RegisterMeal_tracker(admin.ModelAdmin):
    pass

@admin.register(PostFood)
class RegisterPostFood(admin.ModelAdmin):
    pass

@admin.register(Menu)
class RegisterMenu(admin.ModelAdmin):
    pass
