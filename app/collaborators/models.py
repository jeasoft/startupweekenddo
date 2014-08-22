from django.db import models

# Create your models here.

class Collaborators(models.Model):
    """All the colaboratos goes here without exception"""
	full_name = models.CharField(max_length=40)
	mini_bio = models.TextField()
	image = models.ImageField(upload_to="img")
	twitter = models.URLField()
	linkedin = models.URLField()
	email = models.EmailField()
	category = models.CharField(max_length=40)

class Sponsors(models.Model):
    """This model provides a good base to handle the 
    event sponsors
    """
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='img')
    sponsor_type = models.CharField(max_length=40)

