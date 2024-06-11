from django.db import models

# Create your models here.
# tasks/models.py
from django.db import models

class Task(models.Model):
    location_choices = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17')
    ]

    department_choices = [
        ('kitchen', 'Kitchen'),
        ('terminal', 'Terminal'),
        ('driver', 'Driver')
    ]

    shift_choices = [
        ('lunch', 'Lunch shift'),
        ('evening', 'Evening shift')
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=4, choices=location_choices)
    department = models.CharField(max_length=10, choices=department_choices)
    shift = models.CharField(max_length=10, choices=shift_choices)
    date = models.DateField()
    # all_completed= models.BooleanField(default=False)
    # make_juice = models.BooleanField(default=False)
    # make_pizza = models.BooleanField(default=False)
    # process_orders = models.BooleanField(default=False)
    # manage_inventory = models.BooleanField(default=False)
    # deliver_orders = models.BooleanField(default=False)
    # check_vehicle = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.department} on {self.date}"
from django.db import models

class KitchenTask(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='kitchen_task')
    make_juice_completed = models.BooleanField(default=False)
    make_pizza_completed = models.BooleanField(default=False)
