from django.db import models
from django.contrib.auth.models import AbstractUser



class UserAppModel(AbstractUser):
    username = models.CharField(max_length=50)
    image = models.ImageField(verbose_name='image profile')
    whatsapp_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username','image','whatsapp_number']