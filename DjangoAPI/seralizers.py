from rest_framework import seralizers
from rest_framework import serializers
from . models import house

class HouseSeralizer(serializers.ModelSerializer):
	class Meta:
		model=house
		fields='__all__'