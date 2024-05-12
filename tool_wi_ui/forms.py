from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control formulaire',
                                                           'id': 'Prenom'}
                                                    )
                             )
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control formulaire',
                                                        'id': 'nom'}
                                                 )
                          )

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control formulaire',
                                                            'id': 'email'}
                                                     )
                             )

    motDePasse = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control formulaire',
                                                                   'id': 'password'}
                                                            )
                                 )

    class Meta:
        model = User
        fields = "__all__"
