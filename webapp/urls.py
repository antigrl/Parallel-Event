from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('webapp.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gauth/$', 'gauth_redirect'),
    url(r'^gauthcomplete$', 'link_accounts'),
    url(r'', include('singly.urls')),
    url(r'^$', 'index', name='index'),
    url(r'^link_accounts/$', 'link_accounts'),
)
