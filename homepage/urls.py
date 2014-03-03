from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('homepage.views',
	url(r'^', 'index', name='index'),
	url(r'^handlefile/$', 'handlefile', name='handlefile')
)

