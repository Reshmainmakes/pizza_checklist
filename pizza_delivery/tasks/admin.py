from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['date', 'location', 'department', 'shift', 'name']
    list_filter = ['date', 'location', 'department', 'shift']
    search_fields = ['date', 'location', 'department', 'shift', 'name']

# from django.contrib import admin
# from .models import KitchenTask
#
# class KitchenTaskAdmin(admin.ModelAdmin):
#     list_display = ['task', 'make_juice_completed', 'make_pizza_completed']
#     list_filter = ['make_juice_completed', 'make_pizza_completed']
#     search_fields = ['task__name']
#
# admin.site.register(KitchenTask, KitchenTaskAdmin)
