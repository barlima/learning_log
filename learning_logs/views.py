from django.shortcuts import render

from .models import Topic


def index(request):
    """Home page for Learning log app."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Displays all of the topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Displays single topic and its related posts"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
