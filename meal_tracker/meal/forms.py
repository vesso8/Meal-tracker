from django import forms

from meal_tracker.meal.models import Food, Menu, Meal_tracker


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields =('name', 'type_of_food', 'quantity', 'calorie')

class UpdateFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'type_of_food', 'quantity', 'calorie')

class DeleteFoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
    def save(self, commit=True):
        self.instance.delete()
        return self.instance
    class Meta:
        model = Food
        fields = ('name', 'type_of_food', 'quantity', 'calorie')

class BaseMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('title', 'image', 'breakfast', 'snack_1', 'lunch', 'snack_2', 'dinner', 'snack_3', 'calories')

class AddMenuForm(BaseMenuForm):
    class Meta(BaseMenuForm.Meta):
        pass

class MenuDetailsForm(BaseMenuForm):
    class Meta(BaseMenuForm.Meta):
        pass

class SelectFoodForm(forms.ModelForm):
    class Meta:
        model = Meal_tracker
        fields = ('food_selected', 'quantity')

    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)

class MealTrackerForm(forms.ModelForm):
    class Meta:
        model = Meal_tracker
        fields = ('calorie_goal',)

