from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('webapp.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('singly.urls')),
    url(r'^$', 'index', name='index')
)
