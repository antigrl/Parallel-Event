from django.shortcuts import render_to_response
from django.template.context import RequestContext
import simplejson


def index(request, template='index.html'):
    services = [
        'Facebook',
        'foursquare',
        'Instagram',
        'Tumblr',
        'Twitter',
        'LinkedIn',
        'FitBit',
        'Email'
    ]
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        # We replace single quotes with double quotes b/c of python's strict json requirements
        profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response
