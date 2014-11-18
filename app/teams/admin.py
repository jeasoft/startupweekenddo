from django.contrib import admin
from .models import Enterpreneaur, Team, Category

class EnterpreneaurAdmin(admin.ModelAdmin):
	exclude = ("slug",)

class TeamAdmin(admin.ModelAdmin):
	exclude = ("slug",)

class CategoryAdmin(admin.ModelAdmin):
	exclude = ("slug",)

admin.site.register(Enterpreneaur,EnterpreneaurAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Category, CategoryAdmin)