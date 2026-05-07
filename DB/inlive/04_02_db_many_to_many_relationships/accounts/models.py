from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self',related_name='followers', symmetrical=False)
    pass

    # def __str__(self):
    #     return self.username
