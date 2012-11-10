from django.contrib.auth.models import User
from django.db import models
from managers import UserProfileManager


class UserProfile(models.Model):
    access_token = models.CharField(max_length=260, null=True, blank=True)
    singly_id = models.CharField(max_length=260, null=True, blank=True)
    profiles = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='profile')

    objects = UserProfileManager()

    class Meta:
        db_table = 'user_profile'
