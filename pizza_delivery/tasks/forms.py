# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['date','location', 'department', 'shift', 'name']
# # tasks/forms.py
# from django import forms
# from .models import KitchenTask
#
# class KitchenTaskForm(forms.ModelForm):
#     class Meta:
#         model = KitchenTask
#         fields = ['task', 'make_juice_completed', 'make_pizza_completed']
