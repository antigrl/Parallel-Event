from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import simplejson

import gdata.calendar.service
import cal_events

def index(request, template='index.html'):
    services = [
        'Facebook',
        'Twitter',
    ]
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        # We replace single quotes with double quotes b/c of python's strict json requirements
        profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response

def GetAuthSubUrl():
    #next = 'http://www.parallelevent.com/gauthcomplete'
    next = 'http://localhost:8000/gauthcomplete'
    scope = 'http://www.google.com/calendar/feeds/'
    secure = False
    session = True
    calendar_service = gdata.calendar.service.CalendarService()
    return calendar_service.GenerateAuthSubURL(next, scope, secure, session)

def gauth_redirect(request):
    url = GetAuthSubUrl()
    return HttpResponseRedirect(str(url))

def gauth_complete(request):
    token = request.GET.get('token')
    events, _ = cal_events.getAllEvents(token)
    return HttpResponse(str(events))
