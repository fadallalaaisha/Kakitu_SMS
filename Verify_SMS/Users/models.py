from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13)

    def __unicode__(self):
        return self.phone_number

class PickForm(ModelForm):
    class Meta:
        Model = CustomUser