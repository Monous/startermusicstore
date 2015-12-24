"""
Definition of models.
"""

from django.db import models
from django.forms import ModelForm

# Create your models here.

# objects is a method that is inherited from models. The objects method are the records for a given model (e.g. Artist, Album)

class Artist(models.Model):
    """ verbose_name is by default the first parameter for the Type parameter list"""
    name = models.CharField("Artist", max_length = 50);
    year_formed = models.PositiveIntegerField();

class ArtistForm(ModelForm):
    class Meta:
        model = Artist;
        fields = ['name', 'year_formed'];

class Album(models.Model):
    name = models.CharField("Album", max_length = 50);
    artist = models.ForeignKey(Artist);
    
