from django.urls import path

from meal_tracker.meal.views.menu_views import CreateMenuView, MenuDetailsView, EditMenuView, \
    DeleteMenuView
from meal_tracker.meal.views.generic_views import HomeView
from meal_tracker.meal.views.meal_tracker_views import select_food, add_food, calorie_counter, meal_tracker, \
    update_food, delete_food

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('food/add/', add_food, name='add food'),
    path('food/update/<int:pk>/', update_food, name='update food'),
    path('food/delete/<int:pk>/', delete_food, name='delete food'),
    path('menu/add/', CreateMenuView.as_view(), name='add menu'),
    path('menu/details/<int:pk>/', MenuDetailsView.as_view(), name='menu details'),
    path('menu/edit/<int:pk>/', EditMenuView.as_view(), name='edit menu'),
    path('menu/delete/<int:pk>/', DeleteMenuView.as_view(), name='delete menu'),
    path('meal_tracker/', meal_tracker, name='meal tracker'),
    path('calorie_counter/', calorie_counter, name='calorie counter'),
    path('select_food/', select_food, name='select food'),
)