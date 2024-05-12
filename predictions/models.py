from django.db import models

# Create your models here.
class PredictionBasique(models.Model):
    """
        Une prédiction basique
    """
    
    culture = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    temp = models.FloatField()
    humidity =models.FloatField()
    superfice = models.FloatField()
    wind = models.FloatField()
    rainfall = models.FloatField()

class PredictionPremium(PredictionBasique):
    """
        Une prédiction premium
    """
    p = models.FloatField()
    k = models.FloatField()
    n = models.FloatField()
    ph = models.FloatField()

class PredictionRevenu(models.Model):
    """
        Une prédiction premium
    """
    produit = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    mois = models.FloatField()
    annee = models.FloatField()
    prix = models.FloatField()
