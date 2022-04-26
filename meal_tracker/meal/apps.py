from django.apps import AppConfig


class MealConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meal_tracker.meal'

    def ready(self):
        import meal_tracker.meal.signals