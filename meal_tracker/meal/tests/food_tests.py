from django.core.exceptions import ValidationError
from django.urls import reverse
from meal_tracker.meal.tests.create_test_data_mixin import CreateTestDataMixin
from meal_tracker.meal.models import Food

class FoodViewTest(CreateTestDataMixin):

    def test_add_food_not_available_for_unauthenticated_users(self):
        response =self.client.get(self.ADD_FOOD_URL)
        expected = self.LOGIN_URL + '?redirect_to=%2Ffood%2Fadd%2F'
        self.assertRedirects(response, expected)
    def test_add_food__show_correct_template(self):
        self.login_and_register()
        self.client.login(email='test@gmail.com', password='secret_password_1234',)
        request = self.client.get(self.ADD_FOOD_URL)
        self.assertEqual(request.status_code, 200)

    def test_add_food_adding_food_correct(self):
        self.add_food()
        expected = self.VALID_FOOD_CREDENTIALS['name']
        current = 'apple'
        self.assertEqual(expected, current)

    def test_select_food_not_available_for_unauthenticated_users(self):
        response = self.client.get(self.SELECT_FOOD_URL)
        expected = self.LOGIN_URL + '?redirect_to=%2Fselect_food%2F'
        self.assertRedirects(response, expected)
    def test_select_food_show_correct_template(self):
        self.login_and_register()
        self.client.login(email='test@gmail.com', password='secret_password_1234',)
        request = self.client.get(self.SELECT_FOOD_URL)
        self.assertEqual(request.status_code, 200)


    def test_meal_tracker_not_available_for_unauthenticated_users(self):
        response = self.client.get(self.MEAL_TRACKER_URL)
        expected = self.LOGIN_URL + '?redirect_to=%2Fmeal_tracker%2F'
        self.assertRedirects(response, expected)
    def test_meal_tracker_show_correct_template(self):
        self.login_and_register()
        self.client.login(email='test@gmail.com', password='secret_password_1234', )
        request = self.client.get(self.MEAL_TRACKER_URL)
        self.assertEqual(request.status_code, 200)


    def test_calorie_counter_not_available_for_unauthenticated_users(self):
        response = self.client.get(self.CALORIE_COUNTER_URL)
        expected = self.LOGIN_URL + '?redirect_to=%2Fcalorie_counter%2F'
        self.assertRedirects(response, expected)
    def test_calorie_counter__show_correct_template(self):
        self.login_and_register()
        self.client.login(email='test@gmail.com', password='secret_password_1234', )
        request = self.client.get(self.CALORIE_COUNTER_URL)
        self.assertEqual(request.status_code, 200)


