from django.db import models
from django import forms


class TodoList(models.Model):
    item = models.CharField(max_length=100)

    Active = 'active'
    Done = 'done'
    Canceled = 'canceled'

    Status = ((Active, 'active'),(Done, 'done'),(Canceled, 'canceled'),)

    status = models.CharField(max_length=20, choices=Status, default=Active)

    def __str__(self):
        return self.item