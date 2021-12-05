from django.db import models

# Create your models here.
class house(models.Model):
    Size = models.IntegerField()
    Bedrooms = models.IntegerField()


    def __str__(self):
        return self.Size , self.Bedrooms