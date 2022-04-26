from django import test as django_test
from django.contrib.auth import get_user, get_user_model
from django.http import HttpRequest
from django.urls import reverse
from django.test.client import Client
from meal_tracker.auth_user.models import Profile, AuthUser


class CreateTestDataMixin(django_test.TestCase):
    UserModel = get_user_model()
    VALID_USER_REGISTER_DATA = {
        'email': 'test@gmail.com',
        'first_name': 'Georgi',
        'last_name': 'Georgiev',
        'password1': 'secret_password_1234',
        'password2': 'secret_password_1234'
    }

    VALID_USER_LOGIN_DATA = {
        'email': 'test@gmail.com',
        'password': 'secret_password_1234'
    }
    VALID_FOOD_CREDENTIALS = {
        'name': 'apple',
        'type_of_food': 'fruit',
        'quantity': 2,
        'calorie': 20
    }

    REGISTER_URL = reverse('register')
    REGISTER_SUCCESS_URL = reverse('home')
    LOGOUT_URL = reverse('logout')
    LOGIN_URL = reverse('login')
    LOGIN_SUCCESS_URL = reverse('home')
    HOME_URL = reverse('home')
    ADD_FOOD_URL = reverse('add food')
    SELECT_FOOD_URL = reverse('select food')
    ADD_MENU_URL = reverse('add menu')
    CALORIE_COUNTER_URL = reverse('calorie counter')
    MEAL_TRACKER_URL = reverse('meal tracker')

    def register(self):
        return self.client.post(self.REGISTER_URL, data=self.VALID_USER_REGISTER_DATA)

    def login_and_register(self):
        self.register()
        return self.client.login(**self.VALID_USER_LOGIN_DATA)

    def get_user_data(self):
        request = HttpRequest()
        request.session = self.client.session
        return get_user(request)

    def add_food_data_cred(self):
        self.login_and_register()
        self.VALID_FOOD_CREDENTIALS['person_of_id'] = self.get_user_data()
        return self.VALID_FOOD_CREDENTIALS
    def add_food(self):
        self.add_food_data_cred()
        return self.client.post(self.ADD_FOOD_URL, data=self.VALID_FOOD_CREDENTIALS)
    def add_menu_superuser(self):
        my_admin = self.UserModel.objects.create_superuser(email='myuser@gmail.com', password='user11223344')
        c = Client()
        return c.login(email=my_admin.email, password=my_admin.password)
