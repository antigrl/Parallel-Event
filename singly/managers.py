from django.db import models
from singly import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class UserProfileManager(models.Manager):

    def get_or_create_user(self, singly_id, access_token):
        endpoint = '/profiles'
        request = {'auth': 'true'}
        profiles = Singly(access_token=access_token).make_request(endpoint, request=request)
        singly_id = profiles['id']
        try:
            user_profile = self.get(singly_id=singly_id)
            user_profile.profiles = profiles
            user_profile.save()

        except ObjectDoesNotExist:
            try:
                user = User.objects.get(username=singly_id)
            except ObjectDoesNotExist:
                # Made-up email address included due to convention
                user = User.objects.create_user(singly_id, singly_id + '@singly.com', 'fakepassword')
            user_profile = self.model(
                access_token=access_token,
                singly_id=singly_id,
                profiles=profiles,
                user=user
            )
            user_profile.save()
        return user_profile
