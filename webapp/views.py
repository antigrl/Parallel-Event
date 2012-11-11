from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import simplejson

import gdata.calendar.service
import cal_events
from forms import LinkForm

urls = None

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

def link_accounts(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LinkForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        token = request.GET.get('token')
        events, client = cal_events.getAllEvents(token)

        calendars = cal_events.getAllCalendars(client)

        calendar_choices = tuple((val, choice) for val, choice in enumerate(calendars))

        profiles = request.user.get_profile().profiles
        profiles = eval(profiles)
        profiles.pop("id")
        
        profile_choices = tuple(((val, choice.capitalize()) for val, choice in enumerate(profiles.keys())))


        form = LinkForm(initial= {'calendar_choices': calendar_choices,
                                  'share_choices': profile_choices,
                                  'format_text': 'Hello World'})

    return render(request, 'link_form.html', {
        'form': form,
    })
