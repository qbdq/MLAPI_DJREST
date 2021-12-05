from django import forms
from django import forms

class HouseForm(forms.Form):
     Size = forms.IntegerField()
     Bedrooms = forms.IntegerField()

