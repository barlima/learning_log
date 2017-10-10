"""URL patterns for learning logs app"""

from django.conf.urls import url

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Topics
    url(r'^topics/$', views.topics, name='topics'),
    # Single topic page
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
