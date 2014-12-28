from django.db import models

# User class for built-in authentication module
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	text = models.CharField(max_length=250)
	user = models.ForeignKey(User)
  	publishedDate = models.DateField()

	def __unicode__(self):
		return self.text
