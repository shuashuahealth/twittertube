from django.db import models
from twittube.models import Sponsor

class Participant(models.Model):
	sponsor = models.ForeignKey(Sponsor)
	internal_num = models.IntegerField(default = 0)
	filename = models.CharField(max_length=100)