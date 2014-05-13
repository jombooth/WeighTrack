from django.contrib.auth.models import User
from django import forms
from weightrack_app.models import TaggedItem, Scale, Order



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

class ReorderForm(forms.ModelForm):
    class Meta:
    	model = Order
        fields = ('name',)