
from . models import house
from .seralizers import HouseSeralizer
from rest_framework import viewsets
 
# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
	queryset = house.objects.all()
	serializer_class = HouseSeralizer
		