from django import forms
from django import forms

class HouseForm(forms.Form):
     Size = forms.IntegerField(widget = forms.NumberInput(attrs ={'placeholder' : 'Enter your value here..','class': 'myfieldclass'}))
     Bedrooms = forms.IntegerField(widget = forms.NumberInput(attrs ={'placeholder' : 'Enter your value here..','class': 'myfieldclass'}))

