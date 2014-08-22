from django.db import models

# Create your models here.

class Collaborators(models.Model):
	full_name = models.CharField(max_length=40)
	mini_bio = models.TextField()
	image = models.ImageField(upload_to="img")
	twitter = models.URLField()
	linkedin = models.URLField()
	email = models.EmailField()
	category = models.CharField(max_length=40)

class Sponsors(models.Model):
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='img')
    sponsor_type = models.CharField(max_length=40)

