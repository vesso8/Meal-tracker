from meal_tracker.meal.models import Menu
from meal_tracker.meal.tests.create_test_data_mixin import CreateTestDataMixin
from meal_tracker.meal.views.generic_views import HomeView


class GenericViewsTest(CreateTestDataMixin):
    def test_home_page_shows_correct_template(self):
        response = self.client.get(self.HOME_URL)
        expected = HomeView.TEMPLATE_NAME
        current = response.context_data['template_name']
        self.assertEqual(expected, current)

