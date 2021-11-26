from django.shortcuts import HttpResponse
from django.shortcuts import render

def home(requests):
    return HttpResponse("Olá django")
