import os
import joblib
from django.apps import AppConfig
from django.conf import settings


    
class DjangoapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DjangoAPI'
    MODEL_FILE = os.path.join(settings.MODELS, "House_Price_Model.joblib")
    model = joblib.load(MODEL_FILE)