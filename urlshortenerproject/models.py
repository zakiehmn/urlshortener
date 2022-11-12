from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    remaining_links = models.PositiveIntegerField(default = 10, validators = [MinLengthValidator(0)])
    active_links = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.name


class Shortener(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    long_url = models.URLField()
    short_url = models.URLField(max_length=20, unique=True, blank=True)

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def find_staff(self):
        return Staff.objects.get(user=self.user)

    def reduce_remaining_links(self):
        staff = Staff.objects.get(user=self.user)
        staff.remaining_links -= 1
        staff.save()

    def increase_active_links(self):
        staff = Staff.objects.get(user=self.user)
        staff.active_links += 1
        staff.save()

    def save(self, *args, **kwargs):
        self.reduce_remaining_links()
        self.increase_active_links()
        super(Shortener, self).save(*args, **kwargs)


