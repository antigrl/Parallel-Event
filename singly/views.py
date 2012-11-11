from django.http import HttpResponseRedirect
from singly import SinglyHelper
from django.contrib.auth import authenticate, login as auth_login
from models import UserProfile


def authenticate_redirect(request, service):
    url = SinglyHelper.get_authorize_url(service)
    return HttpResponseRedirect(url)


def authorize_callback(request):
    code = request.GET.get('code')
    content = SinglyHelper.get_access_token(code)
    user_profile = UserProfile.objects.get_or_create_user(
            content['account'], content['access_token'])
    if not request.user.is_authenticated():
        user = authenticate(username=user_profile.user.username, password='fakepassword')
        auth_login(request, user)
    return HttpResponseRedirect('/')
