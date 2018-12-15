from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view(request):
    s='<h1> Head Tag </h1>'
    return HttpResponse(s)
