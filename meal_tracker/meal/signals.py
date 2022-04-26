from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from meal_tracker.meal.models import Meal_tracker

UserModel = get_user_model()
def create_meal_tracker(sender,instance,created,**kwargs):
	if created:
		Meal_tracker.objects.create(person_of=instance)

post_save.connect(create_meal_tracker,sender=UserModel)