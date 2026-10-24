from django.db import models

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BreakdownRequest(models.Model):
    PROBLEM_CHOICES = [
        ('puncture', 'Puncture'),
        ('battery', 'Battery Dead'),
        ('fuel', 'Out of Fuel'),
        ('engine', 'Engine Problem'),
        ('other', 'Other'),
    ]

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    problem = models.CharField(max_length=20, choices=PROBLEM_CHOICES)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.problem}"

# Create your models here.
