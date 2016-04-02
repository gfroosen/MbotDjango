from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    'api.views',
    url(r'^api/$', 'api_dashboard', name='api_dashboard'),
    url(r'^api/(?P<pk>[0-9]+)$', 'api_detail', name='api_detail'),
    url(r'^control/$', views.robot_control, name='robot_control'),
    url(r'^$', views.index, name='index'),
)
