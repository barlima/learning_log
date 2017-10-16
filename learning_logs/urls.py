"""URL patterns for learning logs app"""

from django.conf.urls import url

from . import views

# app_name = 'learning_logs'
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Topics
    url(r'^topics/$', views.topics, name='topics'),
    # Single topic page
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # New topic page
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # New entry page
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
