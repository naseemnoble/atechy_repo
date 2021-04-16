from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    #userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    userid = models.CharField(max_length=200)
    message = models.CharField(max_length=200)