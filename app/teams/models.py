from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters


@python_2_unicode_compatible
class Category(models.Model):
    """Category for the Enterpreneaur"""

    class Meta:
        verbose_name_plural =  "categories"

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class Team(models.Model):
    """Model for the Team """

    TEAM_PLACE_CHOICES = (
        (0, "---------"),
        (1, "1er Lugar"),
        (2, "2do Lugar"),
        (3, "3er Lugar"),
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    logo = models.ImageField(upload_to="img/logos", blank=True, null=True)
    team_photo = models.ImageField(upload_to="img/team/photo", blank=True, null=True)
    slogan = models.CharField(max_length=140)
    description = models.TextField()
    place = models.PositiveSmallIntegerField(choices = TEAM_PLACE_CHOICES, default=0 )
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Team, self).save(*args, **kwargs)


    def __str__(self):
        return self.name 


@python_2_unicode_compatible
class Enterpreneaur(models.Model):
    """ Model for the Enterpreneaurs """

    full_name = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    photo = models.ImageField(upload_to="img/enterpreneaurs/photo", blank=True, null=True)
    mini_bio = models.TextField()
    team = models.ForeignKey(Team)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    gplus = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

