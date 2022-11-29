from django.urls import path

from meal_tracker.auth_user.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDetailsUserView, \
    ProfileEditView, ProfileDeleteView, PasswordChangeView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('details/<int:pk>/', ProfileDetailsUserView.as_view(), name='user details'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='user edit'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='user delete'),
    path('change-password/<int:pk>/', PasswordChangeView.as_view(), name='change password')

)