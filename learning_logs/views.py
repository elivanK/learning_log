from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
# The homepage for learning log
    return render(request, 'learning_logs/index.html')

def topics(request):
    # Show all topics
    topics = Topic.objects.order_by('data_added')
    content = {'topics': topics }
    return render(request, 'learning_logs/topics.html', content)

def topic(request, topic_id):
    # Show a single topic and all its entries
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
