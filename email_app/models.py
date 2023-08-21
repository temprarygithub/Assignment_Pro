from django.db import models

# Create your models here.

class Event(models.Model):
    employee_id = models.IntegerField()
    event_type = models.CharField(max_length=50)
    event_date = models.DateField()

class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=50)
    template = models.TextField()

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    email = models.EmailField()
