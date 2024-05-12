from django import forms
from .models import PredictionBasique, PredictionPremium, PredictionRevenu
import json

class PredictionBasiqueForm(forms.ModelForm):

    rainfall =  forms.FloatField(min_value=0, label="Pluviomètrie", help_text="Requis", required=True)
    culture = forms.CharField(label="Culture", help_text='Requis', required=True)
    region = forms.CharField(label="Region", help_text='Requis', required=True)
    temp = forms.FloatField(min_value=0, label="Température", help_text="Requis", required=True)
    humidity =forms.FloatField(min_value=0, label="Humidité", help_text="Requis", required=True)
    superfice = forms.FloatField(min_value=0, label="Superficie", help_text="Requis", required=True)
    wind = forms.FloatField(min_value=0, label="Vitesse vent", help_text="Requis", required=True)

    class Meta:
        model = PredictionBasique
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def as_json(self):
        return json.dumps(self.cleaned_data)

class PredictionPremiumForm(forms.ModelForm):

    rainfall =  forms.FloatField(min_value=0, label="Pluviomètrie", help_text="Requis", required=True)
    culture = forms.CharField(label="Culture", help_text='Requis', required=True)
    region = forms.CharField(label="Region", help_text='Requis', required=True)
    temp = forms.FloatField(min_value=0, label="Température", help_text="Requis", required=True)
    humidity =forms.FloatField(min_value=0, label="Humidité", help_text="Requis", required=True)
    superfice = forms.FloatField(min_value=0, label="Superficie", help_text="Requis", required=True)
    wind = forms.FloatField(min_value=0, label="Vitesse vent", help_text="Requis", required=True)
    p = forms.FloatField(min_value=0, label="Phosphore", help_text="Requis", required=True)
    k = forms.FloatField(min_value=0, label="Potassium", help_text="Requis", required=True)
    n = forms.FloatField(min_value=0, label="Azote", help_text="Requis", required=True)
    ph = forms.FloatField(min_value=0, label="PH", help_text="Requis", required=True)

    class Meta:
        model = PredictionPremium
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def as_json(self):
        return json.dumps(self.cleaned_data)

class PredictionRevenuForm(forms.ModelForm):

    produit = forms.CharField(label="Culture", help_text='Requis', required=True)
    region = forms.CharField(label="Region", help_text='Requis', required=True)
    mois = forms.FloatField(min_value=0, label="Mois", help_text="Requis", required=True)
    annee = forms.FloatField(min_value=0, label="Annee", help_text="Requis", required=True)
    prix =forms.FloatField(min_value=0, label="Prix", help_text="Requis", required=True)


    class Meta:
        model = PredictionRevenu
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def as_json(self):
        return json.dumps(self.cleaned_data)