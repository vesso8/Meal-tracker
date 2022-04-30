from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views
from meal_tracker.meal.forms import AddMenuForm, MenuDetailsForm
from meal_tracker.meal.models import Menu


UserModel = get_user_model()

class CustomPermissionMixinDelete(generic_views.View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.is_authenticated:
            return redirect('unauthorized')
        elif not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
class CustomPermissionMixin(generic_views.View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.is_staff and request.user.is_authenticated:
            return redirect('unauthorized')
        elif not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

class CreateMenuView(CustomPermissionMixin, generic_views.CreateView):
    model = Menu
    form_class = AddMenuForm
    template_name = 'menu/menu_add.html'
    success_url = reverse_lazy('home')

class MenuDetailsView(generic_views.DetailView):
    TEMPLATE_NAME = 'Menu Details'
    model = Menu
    form_class = MenuDetailsForm
    template_name = 'menu/details.html'

    def get_success_url(self):
        return reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context

class EditMenuView(CustomPermissionMixin, generic_views.UpdateView):
    TEMPLATE_NAME = 'Edit Menu'
    model = Menu
    template_name = 'menu/edit_menu.html'
    fields = ('title', 'image', 'breakfast', 'snack_1', 'lunch', 'snack_2', 'dinner', 'snack_3', 'calories')
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context

class DeleteMenuView(CustomPermissionMixinDelete, generic_views.DeleteView):
    model = Menu
    template_name = 'menu/delete_menu.html'
    success_url = reverse_lazy('home')