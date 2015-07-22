from django.db import models
from django.contrib.auth.models import User


class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    administrator = models.ForeignKey('BBS_user')


class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=256, default='This gay is too lazy to leave anything here.')
    photo = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/user-1.jpg")

    def __unicode__(self):
        return self.user.username


class Comment(models.Model):
    content = models.TextField()
    user_id = models.ForeignKey('BBS_user')
    bbs_id = models.ForeignKey('BBS')
    date = models.DateTimeField()

    def __unicode__(self):
        return self.content

