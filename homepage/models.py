from django.db import models

# Create your models here.
Class Sponsor(models.Model):
	next_int_num = models.IntegerField(default = 1)
	filename = models.CharField(max_length=100)

Class Participant(models.Model):
	sponsor = models.ForeignKey(Sponsor)
	internal_num = models.IntegerField(default = 0)
	filename = models.CharField(max_length=100)