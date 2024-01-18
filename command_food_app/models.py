from django.db import models



class Command(models.Model):

    IN_PROGRESS =  'in progress'
    FINISHED = 'finished'
    NOT_ACTIF = 'not actif'

    CHOICES = [
        (IN_PROGRESS, 'in progress'),
        (FINISHED, 'finished'),
        (NOT_ACTIF, 'not actif')
    ]
    command_identiant=models.CharField(max_length=90)
    command_client_name = models.CharField(max_length=150)
    command_client_phone_number = models.CharField(max_length=12)
    place_of_delivery = models.CharField(max_length=50)
    command_status = models.CharField(max_length=50, choices=CHOICES)
    creator = models.CharField(max_length=50, default='amer')
