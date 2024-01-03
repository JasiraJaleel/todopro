from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=250)
    taskDesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Task"

    def __str__(self):
        return self.taskTitle