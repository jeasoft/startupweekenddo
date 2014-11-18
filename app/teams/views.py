from django.shortcuts import render
from django.views.generic import ListView
from .models import Team

class TeamList(ListView):
	model = Team
	context_object_name = 'team_list'
	#template_name = 'index.html'
