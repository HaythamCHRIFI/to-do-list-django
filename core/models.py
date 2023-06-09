from django.db import models

# Create your models here.

class Task(models.Model):
    todo = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo
