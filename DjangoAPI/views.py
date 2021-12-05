from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import house
from .seralizers import HouseSeralizer
import numpy as np
import pandas as pd
from .apps import DjangoapiConfig
from .forms import HouseForm
from django.contrib import messages

# Create your views here.
class HouseView(viewsets.ModelViewSet):
	queryset = house.objects.all()
	serializer_class = HouseSeralizer
		

#@api_view(["POST"])
def Houseprediction(size,bedrooms):
    try:
        Size =size
        Bedroom = bedrooms
        lin_reg_model = DjangoapiConfig.model
        House_price_prediction = lin_reg_model.predict([[Size, Bedroom]])[0][0]
        House_price_prediction = np.round(House_price_prediction, 1)
        response_text = "Predicted Price ($): {}".format(House_price_prediction) 
        return response_text
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def HouseDetails(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            Size = form.cleaned_data['Size']
            Bedrooms = form.cleaned_data['Bedrooms']
            messages.success(request, Houseprediction(Size,Bedrooms))

    form = HouseForm()
    return render(request , 'houseForm/houseform.html', {'form':form})
