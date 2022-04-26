from django.contrib import admin

from meal_tracker.auth_user.models import Profile, AuthUser


@admin.register(Profile)
class RegisterProfile(admin.ModelAdmin):
    pass


@admin.register(AuthUser)
class RegisterAuthUser(admin.ModelAdmin):
    pass
