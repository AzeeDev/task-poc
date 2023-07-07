from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    status = models.BooleanField(default=False)
