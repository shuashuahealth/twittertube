from django.conf.urls import patterns, url

urlpatterns = patterns('conversation.views',
	url(r'^(?P<sponsor_id>\d+)/$', 'index', name='index'),
	url(r'^handlefile/$', 'handlefile', name='handlefile')
)

