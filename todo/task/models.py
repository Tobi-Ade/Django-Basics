from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(default=None, max_length=200)
    complete = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task
