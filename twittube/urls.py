from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twittube.views.home', name='home'),
    # url(r'^twittube/', include('twittube.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'twittube.views.index', name='index'),
    url(r'^handlefile/$', 'twittube.views.handlefile', name='handlefile'),
    url(r'^(?P<sponsor_id>\d+)/', include('conversation.urls')),
)
