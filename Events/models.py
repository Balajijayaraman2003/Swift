from django.db import models
from django.contrib.auth.models import User
from Authentication.models import *

class Event(models.Model):
    TECHNICAL = "Technical"
    NON_TECHNICAL = "Non Technical"

    TYPE_CHOICES = [
        (TECHNICAL, "Technical"),
        (NON_TECHNICAL, "Non Technical"),
    ]

    name = models.CharField(max_length=200)
    head = models.OneToOneField(Swifters, on_delete=models.CASCADE, related_name="event_head",null=True,blank=True)
    sub_heads = models.ManyToManyField(Swifters, related_name="event_sub_heads", blank=True,null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.name} ({self.type}) on {self.date}"