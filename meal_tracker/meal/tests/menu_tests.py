from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
from meal_tracker.meal.tests.create_test_data_mixin import CreateTestDataMixin

from meal_tracker.meal.models import Menu
from meal_tracker.meal.views.menu_views import CreateMenuView

UserModel = get_user_model()
class MenuCreateTests(CreateTestDataMixin):
    VALID_MENU_CREDENTIALS = {
        'title': 'Monday',
        'breakfast': 'Pancakes',
        'lunch': 'Chicken Fillet',
        'dinner': 'Salad',
        'calories': 1500
    }
    def test_not_authenticated_user_expect_redirect_to_login(self):
        response = self.client.get(self.ADD_MENU_URL)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.LOGIN_URL)
    def test_not_super_user_expect__to_redirect_to_home(self):
        self.login_and_register()
        self.client.login(email='test@gmail.com', password='secret_password_1234')
        response = self.client.get(self.ADD_MENU_URL)
        self.assertRedirects(response, self.HOME_URL)

    # def test_superuser__expect_to_show_template(self):
    #     self.add_menu_superuser()
    #     self.client.login(email='myuser@gmail.com', password='user11223344')
    #     request = self.client.get(self.ADD_MENU_URL)
    #     self.assertEqual(request.status_code, 200)


