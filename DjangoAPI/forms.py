from django import forms
from django import forms

class HouseForm(forms.Form):
     Size = forms.IntegerField(widget = forms.NumberInput(attrs ={'placeholder' : 'Size of house in meters'}))
     Bedrooms = forms.IntegerField(widget = forms.NumberInput(attrs ={'placeholder' : 'Number of bedrooms'}))

