from django.db import models
from django.forms import PasswordInput

class Champ(models.Model):
    id_article = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    superficie = models.FloatField()
    region = models.CharField(max_length=50)
    ph_sol= models.FloatField()
    azote_sol= models.FloatField()
    potassium_sol= models.FloatField()

    def __str__(self) -> str:
        return f'{self.nom} '
    
