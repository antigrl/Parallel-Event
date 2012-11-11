from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^authenticate/(?P<service>[a-z]+)/$', 'singly.views.authenticate_redirect',
        name='authenticate_redirect'),
    url(r'^authorize/callback/$', 'singly.views.authorize_callback',
        name='authorize_callback'),
    url(r'^auth$', 'singly.views.authorize_callback',
        name='authorize_callback'),
)
