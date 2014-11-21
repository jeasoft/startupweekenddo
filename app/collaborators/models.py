from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Collaborators(models.Model):
    """All the colaboratos goes here without exception"""

    class Meta:
        verbose_name_plural = "Collaborators"

    COLLABORATOR_CATEGORY_CHOICES = (
        ('Facilitador', 'Facilitador'),
        ('Mentor', 'Mentor'),
        ('Juez', 'Juez'),
        ('Organizador', 'Organizador'),
        ('Colaborador', 'Colaborador'),
    )

    full_name = models.CharField(max_length=40)
    mini_bio = models.TextField()
    image = models.ImageField(upload_to="img")
    twitter = models.URLField()
    linkedin = models.URLField()
    email = models.EmailField()
    category = models.CharField(max_length=40, choices=COLLABORATOR_CATEGORY_CHOICES)

    def __str__(self):
        return self.full_name

@python_2_unicode_compatible
class Sponsors(models.Model):
    """This model provides a good base to handle the 
    event sponsors
    """

    class Meta:
        verbose_name_plural = "Sponsors"

    SPONSOR_TYPE_CHOICE = (
        ('Diamond', 'Diamante'),
        ('Platinum', 'Platino'),
        ('Gold','Oro'),
        ('Silver', 'Plata'),
        ('Bronze','Bronce'),
        ('Media Partner', 'Media Partner'),
    )
    
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='img')
    sponsor_type = models.CharField(max_length=40, choices=SPONSOR_TYPE_CHOICE)

    def __str__(self):
        return self.name