from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render, redirect
from datetime import timedelta
from django.views import generic as generic_views

from meal_tracker.meal.forms import SelectFoodForm, AddFoodForm, MealTrackerForm, UpdateFoodForm, DeleteFoodForm
from meal_tracker.meal.models import PostFood, Calorie_counter, Food
from datetime import date

UserModel = get_user_model()


@login_required(login_url=reverse_lazy('login'), redirect_field_name='redirect_to')
def calorie_counter(request):
    last_day = Calorie_counter.objects.filter(person_of=request.user).last()
    calorie_goal = last_day.calorie_goal

    if date.today() > last_day.date:
        profile = Calorie_counter.objects.create(person_of=request.user)
        profile.save()
    all_food_today = PostFood.objects.filter(profile=last_day)
    calorie_goal_status = round(calorie_goal - last_day.total_calorie)
    over_calorie = 0
    if calorie_goal_status < 0:
        over_calorie = abs(calorie_goal_status)
    context = {
        'total_calorie': last_day.total_calorie,
        'calorie_goal': calorie_goal,
        'calorie_goal_status': calorie_goal_status,
        'over_calorie': over_calorie,
        'food_selected_today': all_food_today
    }
    return render(request, 'generic/calorie_counter.html', context)


@login_required(login_url=reverse_lazy('login'), redirect_field_name='redirect_to')
def add_food(request):
    food_items = Food.objects.filter(person_of=request.user)
    form = AddFoodForm(request.POST)
    if request.method == 'POST':
        form = AddFoodForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.person_of = request.user
            profile.save()
            return redirect('add food')
    else:
        form = AddFoodForm()

    context = {
        'form': form,
        'food_items': food_items,
    }
    return render(request, 'food/food_add.html', context)


@login_required(login_url=reverse_lazy('login'), redirect_field_name='redirect_to')
def select_food(request):
    person = Calorie_counter.objects.filter(person_of=request.user).last()
    food_items = Food.objects.filter(person_of=request.user)
    form = SelectFoodForm(request.user, instance=person)

    if request.method == 'POST':
        form = SelectFoodForm(request.user, request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('calorie counter')
    else:
        form = SelectFoodForm(request.user)
    context = {
        'form': form,
        'food_items': food_items
    }
    return render(request, 'food/select_food.html', context)


@login_required(login_url=reverse_lazy('login'), redirect_field_name='redirect_to')
def update_food(request, pk):
    food = Food.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateFoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('meal tracker')
    else:
        form = UpdateFoodForm(instance=food)

    context = {
        'form': form,
        'food': food
    }
    return render(request, 'food/edit_food.html', context)


@login_required(login_url=reverse_lazy('login'), redirect_field_name='redirect_to')
def delete_food(request, pk):
    food = Food.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteFoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('meal tracker')
    else:
        form = DeleteFoodForm(instance=food)

    context = {
        'form': form,
        'food': food
    }
    return render(request, 'food/delete_food.html', context)


@login_required(login_url=reverse_lazy('login'), redirect_field_name='redirect_to')
def meal_tracker(request):
    person = Calorie_counter.objects.filter(person_of=request.user).last()
    food_items = Food.objects.filter(person_of=request.user)
    form = MealTrackerForm(instance=person)

    if request.method == 'POST':
        form = MealTrackerForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('calorie counter')
    else:
        form = MealTrackerForm(instance=person)
    day_of_the_past_week = timezone.now().date() - timedelta(days=7)
    records = Calorie_counter.objects.filter(date__gte=day_of_the_past_week, date__lt=timezone.now().date(),
                                          person_of=request.user)
    context = {
        'form': form,
        'food_items': food_items,
        'records': records
    }
    return render(request, 'generic/meal_tracker.html', context)
