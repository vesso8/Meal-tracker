from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views

from meal_tracker.meal.models import Menu


def unauthorized(request):
    context = {
        'template_name': '401 (Unauthorized)'
    }
    return render(request, context=context, template_name='generic/401.html')


def handler404(request, *args, **argv):
    response = render(request, context={}, template_name='generic/404.html')
    response.status_code = 404
    return response

def handler405(request, *args, **argv):
    TEMPLATE_NAME = '405 Not Allowed'
    response = render(request, context={}, template_name='generic/405.html')
    response.status_code = 405
    return response


def handler500(request, *args, **argv):
    response = render(request, context={}, template_name='generic/500.html')
    response.status_code = 500
    return response

class HomeView(generic_views.ListView):
    TEMPLATE_NAME = 'Home'
    model = Menu
    template_name = 'generic/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        context['all_menus'] = Menu.objects.all()
        return context
