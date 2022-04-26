from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.urls import reverse
from django.contrib import auth
from meal_tracker.auth_user.models import Profile, AuthUser
from meal_tracker.auth_user.templatetags.user_profile import user_profile
from meal_tracker.auth_user.views import ProfileDetailsUserView
from meal_tracker.meal.tests.create_test_data_mixin import CreateTestDataMixin
from django.test.client import Client



UserModel = get_user_model()
class UserProfileTests(CreateTestDataMixin):
    def test_create_profile(self):
        self.register()
        profile = Profile.objects.first()
        expected_first_name = self.VALID_USER_REGISTER_DATA['first_name']
        expected_last_name = self.VALID_USER_REGISTER_DATA['last_name']
        current_first_name = profile.first_name
        current_last_name = profile.last_name
        self.assertIsNotNone(profile)
        self.assertEqual(expected_first_name, current_first_name)
        self.assertEqual(expected_last_name, current_last_name)

    def test_create_user(self):
        self.register()
        user = AuthUser.objects.first()
        expected_email_address = self.VALID_USER_REGISTER_DATA['email']
        current_email_address = user.email
        self.assertIsNotNone(user)
        self.assertEqual(expected_email_address, current_email_address)
        self.assertFalse(user.is_staff)

    def test_successful_registration_redirects_to_home(self):
        response = self.register()
        expected_redirect = self.REGISTER_SUCCESS_URL
        current_redirect = response
        self.assertRedirects(current_redirect, expected_redirect)

    def test_successful_login_redirects_to_home(self):
        is_logged_in = self.login_and_register()
        self.assertTrue(is_logged_in)
    def test_successful_logout(self):
        self.login_and_register()
        self.client.logout()
        user = self.get_user_data()
        self.assertTrue(user.is_anonymous)
    def test_show_correct_user__for_user_details(self):
        url_name = 'user details'
        self.login_and_register()
        user = self.get_user_data()

        response = self.client.get(reverse(url_name, kwargs={'pk': user.id}))
        expected = user.id
        current = response.context_data['profile'].user_id
        self.assertEqual(expected, current)

    def test_show_correct_template__for_user_details(self):
        url_name = 'user details'
        self.login_and_register()
        user = self.get_user_data()
        response = self.client.get(reverse(url_name, kwargs={'pk': user.id}))
        expected = ProfileDetailsUserView.TEMPLATE_NAME
        actual = response.context_data['template_name']
        self.assertEqual(expected, actual)
    def test_change_password_view__expect_to_change_password(self):
        self.login_and_register()
        user = self.get_user_data()
        change_password_data = {
            'old_password': 'secret_password_1234',
            'new_password1': 'secret_password_12345',
            'new_password2': 'secret_password_12345'
        }
        url_name = 'change password'
        url_kwargs ={
            'pk': user.id,
        }

        response = self.client.post(reverse(url_name, kwargs=url_kwargs),
                                    data=change_password_data)
        expected_message = 302
        actual_message = response.status_code
        self.assertEqual(expected_message, actual_message)

    def test_edit_user_profile_view(self):
        url_name = 'user edit'
        self.login_and_register()
        user = self.get_user_data()
        self.VALID_USER_REGISTER_DATA['first_name'] = 'Georgi'
        self.client.post(reverse(url_name, kwargs={'pk': user.id}), data=self.VALID_USER_REGISTER_DATA)

        user = self.get_user_data()
        profile = Profile.objects.get(pk=user.id)
        expected_user = self.VALID_USER_REGISTER_DATA['first_name']
        current = profile.first_name
        self.assertEqual(expected_user, current)
    def test_user_profile__expect_template_tag_to_return_correct(self):
        self.login_and_register()
        request = HttpRequest()
        request.user = self.get_user_data()
        context = {'request': request}
        user = user_profile(context)
        expected_first_name = self.VALID_USER_REGISTER_DATA['first_name']
        expected_last_name = self.VALID_USER_REGISTER_DATA['last_name']
        actual_first_name = user['first_name']
        actual_last_name = user['last_name']

        self.assertEqual(expected_first_name, actual_first_name)
        self.assertEqual(expected_last_name, actual_last_name)
    def test_user_profile__expect_to_return_none(self):
        client = Client()
        request = HttpRequest()
        request.user = auth.get_user(client)
        context = {'request': request}
        user = user_profile(context)
        self.assertIsNone(user)
    def test_user_model_data(self):
        user = UserModel(first_name='test', last_name='test1', email='test@test1.com')

        expected_first_name = 'test'
        expected_last_name = 'test1'
        expected_email = 'test@test1.com'

        actual_first_name = user.first_name
        actual_last_name = user.last_name
        actual_email = user.email

        self.assertEqual(expected_first_name, actual_first_name)
        self.assertEqual(expected_last_name, actual_last_name)
        self.assertEqual(expected_email, actual_email)
