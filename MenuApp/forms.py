from django import forms
from MenuApp.models import MenuAppModel, Eater


class CreateMenuApp(forms.ModelForm):

    class Meta:
        model = MenuAppModel
        fields = ['menu_title','menu_type_food','menu_image','menu_creator']




class EaterForm(forms.Form):
    name = forms.CharField(max_length=120)
    description = forms.CharField(widget=forms.TextInput)
    price = forms.FloatField()
    menu_type = forms.CharField(max_length=50)
    image = forms.ImageField()


class EaterFormUpdater(forms.ModelForm):
    class Meta:
        model = Eater
        fields = ['description','price','image']
