from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AdvUser(AbstractUser):
    ''' Customniy polsovatel'''
    is_activated=models.BooleanField(default=True,db_index=True)
    send_messages=models.BooleanField(default=True)
    class Meta(AbstractUser.Meta):
        pass