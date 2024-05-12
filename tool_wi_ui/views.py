import time
from django.shortcuts import render, redirect



def view_base(request):
    return render(request, "home.html")


def view_analyse(request):
    return render(request, "champ.html")