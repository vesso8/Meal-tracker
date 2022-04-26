# from django import test as django_test
# from django.urls import reverse
#
# from meal_tracker.auth_user.models import Profile, AuthUser
#
#
# class UserProfileCreateViewTest(django_test.TestCase):
#     VALID_USER_REGISTER_DATA = {
#         'email': 'test@gmail.com',
#         'first_name': 'Georgi',
#         'last_name': 'Georgiev',
#         'password1': 'secret_password_1234',
#         'password2': 'secret_password_1234'
#     }
#     VALID_USER_LOGIN_DATA = {
#         'email': 'test@gmail.com',
#         'password': 'secret_password_1234'
#     }
#
#     REGISTER_URL = reverse('register')
#     REGISTER_SUCCESS_URL = reverse('home')
#     LOGIN_URL = reverse('login')
#     LOGIN_SUCCESS_URL = reverse('home')
#
#     def test_create_profile(self):
#         self.client.post(self.REGISTER_URL, data=self.VALID_USER_REGISTER_DATA)
#         profile =Profile.objects.first()
#
#         self.assertIsNotNone(profile)
#         self.assertEqual(self.VALID_USER_REGISTER_DATA['first_name'], profile.first_name)
#         self.assertEqual(self.VALID_USER_REGISTER_DATA['last_name'], profile.last_name)
#
#     def test_create_user(self):
#         self.client.post(self.REGISTER_URL, data=self.VALID_USER_REGISTER_DATA)
#         user = AuthUser.objects.first()
#         self.assertIsNotNone(user)
#         self.assertEqual(self.VALID_USER_REGISTER_DATA['email'], user.email)
#         self.assertFalse(user.is_staff)
#
#     def test_successful_registration_redirects_to_home(self):
#         response = self.client.post(self.REGISTER_URL, data=self.VALID_USER_REGISTER_DATA)
#         self.assertRedirects(response, self.REGISTER_SUCCESS_URL)
#     def test_successful_login_redirects_to_home(self):
#         self.client.post(self.REGISTER_URL, data=self.VALID_USER_REGISTER_DATA)
#         is_logged_in =self.client.login(**self.VALID_USER_LOGIN_DATA)
#         self.assertTrue(is_logged_in)
#
