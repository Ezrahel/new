from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from Dapp.models import Topic

# Create your views here.
def homepage(request):
    return (HttpResponse("Coding with my guyyyy!!! you did it Lol"))

def index(request):
    """render from HTML file"""
    return render(request, 'Dapp/index.html')
    
def topics(request):
    topics = Topic.objects.order_by('dateAdded')
    context = {'topic': topics}
    return render(request, 'Dapp/topics.html', context)

# def topic(request, topic_id):
#     """Show a single topic and all its entries."""
#     topic = Topic.objects.get(id=topic_id)
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'learning_logs/topic.html', context)