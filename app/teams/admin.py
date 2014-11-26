from django.contrib import admin
from .models import Enterpreneaur, Team

class TeamAdmin(admin.ModelAdmin):
	exclude = ("slug",)

admin.site.register(Enterpreneaur)
admin.site.register(Team, TeamAdmin)
