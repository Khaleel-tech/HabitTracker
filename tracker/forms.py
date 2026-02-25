from django import forms

from .models import Habit, HabitLog


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g., Read 30 minutes'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional notes...'}),
        }


class HabitLogForm(forms.ModelForm):
    class Meta:
        model = HabitLog
        fields = ['habit', 'date', 'minutes', 'done']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'minutes': forms.NumberInput(attrs={'min': 0}),
        }
