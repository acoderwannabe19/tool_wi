from django.shortcuts import render
from .forms import PredictionBasiqueForm, PredictionPremiumForm, PredictionRevenuForm
import requests
import json

# Create your views here.
def prediction_basique(request):
    if request.method == 'POST':
        predictionForm = PredictionBasiqueForm(request.POST)
        if predictionForm.is_valid():
            response = requests.post(
                "http://localhost:8100/api/yield-forecast/v1",
                json = predictionForm.as_json()
            )
            return render(request, 'basique.html', {'form': predictionForm, 'prediction': response["rendement"]})
    else:
        predictionForm = PredictionBasiqueForm()
    return render(request, 'basique.html', {'form': predictionForm})

def prediction_premium(request):
    if request.method == 'POST':
        predictionForm = PredictionPremiumForm(request.POST)
        if predictionForm.is_valid():
            response = requests.post(
                "http://localhost:8100/api/yield-forecast/v2",
                json = predictionForm.as_json()
            )
            return render(request, 'premium.html', {'form': predictionForm, 'prediction': response["rendement"]})
    else:
        predictionForm = PredictionPremiumForm()
    return render(request, 'premium.html', {'form': predictionForm})

def prediction_revenu(request):
    if request.method == 'POST':
        predictionForm = PredictionRevenuForm(request.POST)
        if predictionForm.is_valid():
            response = requests.post(
                "http://localhost:8100/api/yield-forecast/v2",
                json = predictionForm.as_json()
            )
            return render(request, 'revenu.html', {'form': predictionForm, 'prediction': response["prix"]})
    else:
        predictionForm = PredictionPremiumForm()
    return render(request, 'revenu.html', {'form': predictionForm})