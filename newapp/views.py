from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    return render(request, 'newapp/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'newapp/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'newapp/topic.html', context)


def new_topic(request):
    """Define new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('newapp:topics')

    context = {'form': form}
    return render(request, 'newapp/new_topic.html', context)


def new_entry(request, topic_id):
    """Define new entry"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('newapp:topic', topic_id=topic_id)

    context = {'topic': topic, 'form':form}
    return render(request, 'newapp/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit entries"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('newapp:topic', topic_id = topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'newapp/edit_entry.html', context)
