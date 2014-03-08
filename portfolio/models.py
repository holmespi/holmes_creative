from django.db import models

# Create your models here.

class item(models.Model):
	image = models.URLField(max_length=255)
	link = models.URLField(max_length=255, blank=True)
	desc = models.TextField(blank=True)
	priority = models.IntegerField(default=0)

class freeLunch(models.Model):
	image = models.URLField(max_length=255)
	link = models.URLField(max_length=255, blank=True)
	desc = models.TextField(blank=True)
	priority = models.IntegerField(default=0)

class sketch(models.Model):
	image = models.URLField(max_length=255)
	link = models.URLField(max_length=255, blank=True)
	desc = models.TextField(blank=True)
	priority = models.IntegerField(default=0)