from django.db import models

class Estimation(models.Model):
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft_living = models.IntegerField()
    sqft_lot = models.IntegerField()
    floors = models.FloatField()
    waterfront = models.BooleanField()
    condition = models.IntegerField()
    grade = models.IntegerField()
    sqft_above = models.IntegerField()
    sqft_basement = models.IntegerField()
    yr_built = models.IntegerField()
    yr_renovated = models.IntegerField()
    zipcode = models.IntegerField()