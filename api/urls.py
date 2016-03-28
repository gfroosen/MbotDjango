from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^api/$', 'api_dashboard', name='api_dashboard'),
    url(r'^api/(?P<pk>[0-9]+)$', 'api_detail', name='api_detail'),
)
