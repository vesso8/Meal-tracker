from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from meal_tracker.meal.forms import AddMenuForm, MenuDetailsForm, AddExerciseForm, ExerciseDetailsForm
from meal_tracker.meal.models import Menu, Exercise

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


class CreateExerciseView(CustomPermissionMixin, generic_views.CreateView):
    model = Exercise
    form_class = AddExerciseForm
    template_name = 'exercise/exercise_add.html'
    success_url = reverse_lazy('home')


class ExercisesView(generic_views.ListView):
    TEMPLATE_NAME = 'Exercise'
    model = Exercise
    template_name = 'exercise/exercises.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        context['all_exercises'] = Exercise.objects.all()
        return context


class ExerciseDetailsView(generic_views.DetailView):
    TEMPLATE_NAME = 'Exercise Details'
    model = Exercise
    form_class = ExerciseDetailsForm
    template_name = 'exercise/details.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class EditExerciseView(CustomPermissionMixin, generic_views.UpdateView):
    TEMPLATE_NAME = 'Edit Exercise'
    model = Exercise
    template_name = 'exercise/edit_exercise.html'
    fields = (
    'muscle_group', 'sets', 'reps', 'image', 'exercise', 'calories_burned')
    success_url = reverse_lazy('exercises')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class DeleteExerciseView(CustomPermissionMixinDelete, generic_views.DeleteView):
    TEMPLATE_NAME = 'Delete Exercise'
    model = Exercise
    template_name = 'exercise/delete_exercise.html'
    success_url = reverse_lazy('exercises')

