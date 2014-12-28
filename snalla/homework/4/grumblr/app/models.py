from django.db import models

# User class for built-in authentication module
from django.contrib.auth.models import User

# Create your models here.


#Grumbler is a user
class Grumbler(models.Model):
    user = models.ForeignKey(User, related_name="user")
    image = models.ImageField(upload_to="profile-pictures", blank=True, default="/media/profile-pictures/default.gif")
    followers = models.ManyToManyField("self", related_name="followers")
    following = models.ManyToManyField("self", related_name="following")
    #blocked by these users
    blockers = models.ManyToManyField("self", related_name="blockers")

class Post(models.Model):
    text = models.CharField(max_length=250)
    author = models.ForeignKey(Grumbler, related_name="author")
    dislikes = models.ManyToManyField(Grumbler, related_name="disliked_by")
    published_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text


class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(Grumbler)
    post = models.ForeignKey(Post)
    published_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
 

