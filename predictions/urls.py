from . import views
from django.urls import path

app_name = "predictions"

urlpatterns = [
    path('v1/', views.prediction_basique, name='basique'),
    path('v2/', views.prediction_basique, name='premium'),
    path('revenu/', views.prediction_basique, name='revenu'),
]

