from django.db import models

# Create your models here.
class ToDo(models.Model):
    list_element = models.CharField(max_length=100)
    is_completed = models.BooleanField(null = False, default=False)