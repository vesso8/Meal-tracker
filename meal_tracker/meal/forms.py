from django import forms

from meal_tracker.meal.models import Food, Menu, Calorie_counter, Exercise


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields =('name', 'type_of_food', 'quantity', 'quantity_units', 'calorie')

class UpdateFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'type_of_food', 'quantity', 'quantity_units', 'calorie')

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
        fields = ('name', 'type_of_food', 'quantity', 'quantity_units','calorie')

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
        model = Calorie_counter
        fields = ('food_selected', 'quantity')
    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        self.fields['food_selected'].queryset = Food.objects.filter(person_of=user, available_quantity=True)

class MealTrackerForm(forms.ModelForm):
    class Meta:
        model = Calorie_counter
        fields = ('calorie_goal',)


class BaseExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('muscle_group', 'sets', 'reps', 'image', 'exercise', 'calories_burned')


class AddExerciseForm(BaseExerciseForm):
    class Meta(BaseExerciseForm.Meta):
        pass

class ExerciseDetailsForm(BaseExerciseForm):
    class Meta(BaseExerciseForm.Meta):
        pass