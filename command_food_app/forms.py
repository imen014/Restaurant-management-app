from django import forms
from command_food_app.models import Command


class CommandFormCreator(forms.ModelForm):
    class Meta:
        model = Command
        fields = ['command_identiant','command_client_name','command_client_phone_number','place_of_delivery','command_status']
