from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    remaining_links = models.IntegerField(default = 10)
    active_links = models.IntegerField(default = 0)

    def __str__(self):
        return self.username
