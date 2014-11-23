import csv
from django.http import HttpResponse
from django.shortcuts import render
from teams.models import Enterpreneaur, Team

def home(request):
	return render(request, 'base.html')

