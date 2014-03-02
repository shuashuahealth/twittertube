from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('homepage.views',
	url(r'^$', views.index, name='index'),
	url(r'^handlefile/$', views.handlefile, name='handlefile')
)

