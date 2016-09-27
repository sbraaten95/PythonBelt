from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.

class Poke(models.Model):
	poker = models.ForeignKey('login.User', models.DO_NOTHING, related_name="Poker")
	pokee = models.ForeignKey('login.User', models.DO_NOTHING, related_name="Pokee")
	count = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class PokeRef(models.Model):
	poker = models.ForeignKey('login.User', models.DO_NOTHING, related_name="PokerRef")
	pokeeref = models.ForeignKey('login.User', models.DO_NOTHING, related_name="PokeeRef")
	count = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)