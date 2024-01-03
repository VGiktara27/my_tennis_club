from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import path

def members(request):
  # templates = loader.get_template('first.html')
  print("request:",request)
  return render(request,'first.html')
