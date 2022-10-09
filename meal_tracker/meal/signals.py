from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from meal_tracker.meal.models import Calorie_counter

UserModel = get_user_model()
def create_calorie_counter(sender,instance,created,**kwargs):
	if created:
		Calorie_counter.objects.create(person_of=instance)

post_save.connect(create_calorie_counter,sender=UserModel)

