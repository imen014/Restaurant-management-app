from django.db import models
from authentication.models import UserAppModel




class MenuAppModel(models.Model):
    FOOD = 'food'
    DESERT = 'desert'
    DRINK = 'drink'

    CHOICES = [
        (FOOD, 'food'),
        (DESERT, 'desert'),
        (DRINK, 'drink')
    ]
    menu_creator = models.ForeignKey(UserAppModel, on_delete=models.CASCADE)
    menu_title = models.CharField(max_length=70)
    menu_type_food = models.CharField(max_length=50, choices=CHOICES)
    menu_image = models.ImageField(null=True,blank=True)
    menu_updater=models.CharField(max_length=50, blank=True, null=True)

class Eater(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField()
    menu_type = models.ForeignKey(MenuAppModel, on_delete=models.CASCADE)
    image = models.ImageField()
    creator = models.CharField(max_length=255)
    updater = models.CharField(default='_______',max_length=255)