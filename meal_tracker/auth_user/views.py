from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_views, login, get_user_model
from django.views import generic as generic_views
from meal_tracker.auth_user import forms as custom_forms
from meal_tracker.auth_user.forms import ChangePasswordForm
from meal_tracker.auth_user.models import Profile, AuthUser

UserModel = get_user_model()


class CustomPermissionMixin(generic_views.View):
    def dispatch(self, request, *args, **kwargs):
        user = UserModel.objects.get(pk=kwargs['pk'])
        if request.user != user:
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(generic_views.CreateView):
    form_class = custom_forms.RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url


class LogoutUserView(auth_views.LogoutView):
    next_page = 'login'


class ProfileDetailsUserView(CustomPermissionMixin, generic_views.DetailView):
    TEMPLATE_NAME = 'Profile Details'
    model = Profile
    template_name = 'user/user_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        profile = Profile.objects.get(pk=user.id)
        context['profile'] = profile
        context['template_name'] = self.TEMPLATE_NAME
        return context


class ProfileEditView(CustomPermissionMixin, generic_views.UpdateView):
    TEMPLATE_NAME = 'Edit Profile'
    model = Profile
    template_name = 'user/user_edit.html'
    fields = ('picture', 'first_name', 'last_name')
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class ProfileDeleteView(CustomPermissionMixin, generic_views.DeleteView):
    model = AuthUser
    template_name = 'user/user_delete.html'
    success_url = reverse_lazy('home')


class PasswordChangeView(CustomPermissionMixin, generic_views.UpdateView):
    TEMPLATE_NAME = 'Change Password'
    model = AuthUser
    form_class = ChangePasswordForm
    fields = '__all__'
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('login')

    def get_form_class(self):
        return self.form_class

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.pop('instance')
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context
