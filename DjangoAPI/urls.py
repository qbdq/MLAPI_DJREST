from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', HouseView)


urlpatterns = [
	path('form/', HouseDetails, name='HouseDetails'),
    path('api/', include(router.urls)),
#   path('status/' , Houseprediction)
]
