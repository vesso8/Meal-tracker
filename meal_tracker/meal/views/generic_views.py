from django.urls import reverse_lazy
from django.views import generic as generic_views

from meal_tracker.meal.models import Menu


class HomeView(generic_views.ListView):
    TEMPLATE_NAME = 'Home'
    model = Menu
    template_name = 'generic/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        context['all_menus'] = Menu.objects.all()
        return context



