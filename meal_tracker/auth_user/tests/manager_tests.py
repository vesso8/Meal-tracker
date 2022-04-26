from django.contrib.auth import get_user_model

from meal_tracker.meal.tests.create_test_data_mixin import CreateTestDataMixin

UserModel = get_user_model()

class ManagerTest(CreateTestDataMixin):
    def test_create_user_successful(self):
        manager = UserModel.objects
        email =self.VALID_USER_LOGIN_DATA['email']
        password = self.VALID_USER_LOGIN_DATA['password']

        user = manager.create_user(email=email, password=password)

        current_email = user.email
        self.assertEqual(email, current_email)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_raises_error(self):
        manager = UserModel.objects
        with self.assertRaises(ValueError) as value_error:
            manager.create_user(email='')
        expected = 'The given email must be set'
        current =value_error.exception.args[0]
        self.assertEqual(expected, current)
    def test_create_superuser_successful(self):
        manager = UserModel.objects
        email = self.VALID_USER_LOGIN_DATA['email']
        password = self.VALID_USER_LOGIN_DATA['password']
        superuser = manager.create_superuser(email=email, password=password)
        current_email = superuser.email
        self.assertEqual(email, current_email)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
    def test_create_superuser_raises_error(self):
        manager = UserModel.objects
        email = self.VALID_USER_LOGIN_DATA['email']
        password = self.VALID_USER_LOGIN_DATA['password']
        staff_field = {'is_staff': False}
        superuser_field = {'is_superuser': False}

        with self.assertRaises(ValueError) as is_staff_value_error:
            manager.create_superuser(email=email, password=password, **staff_field)
        with self.assertRaises(ValueError) as is_superuser_value_error:
            manager.create_superuser(email=email, password=password, **superuser_field)


        expected_staff_error ='Superuser must have is_staff=True.'
        expected_superuser_error = 'Superuser must have is_superuser=True.'
        current_is_staff_error = is_staff_value_error.exception.args[0]
        current_is_superuser_error = is_superuser_value_error.exception.args[0]
        self.assertEqual(expected_staff_error, current_is_staff_error)
        self.assertEqual(expected_superuser_error, current_is_superuser_error)

