from django.db import models
from django.utils import timezone

# Model to save the todoList


class TodoListItem(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.item + '|' + str(self.completed)
