from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)


class Task(models.Model):
    name = models.CharField(max_length=64)

    TO_DO = "To-do"
    DONE = "Done"
    STATUS = [
        ("TO-DO", TO_DO),
        ("DONE", DONE)
    ]
    status = models.CharField(max_length=64, choices=STATUS, default=TO_DO)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True)
