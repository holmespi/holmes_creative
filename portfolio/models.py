from django.db import models

# Create your models here.

class item(models.Model):
	image = models.URLField(max_length=255)
	link = models.URLField(max_length=255)
	desc = models.TextField()
	sketch = models.BooleanField()