from django.shortcuts import render
from blog.models import Topic, Post
from django.views.generic import CreateView


def get_topics(request):
    topics = Topic.objects.all()
    context = {
        "topics": topics
    }
    return render(request, "topics.html", context)


def get_topic_posts(requests, pk):
    posts = Post.objects.filter(topic__id=pk)
    context = {
        'posts': posts
    }
    return render(requests, "posts.html", context)


class AddTopicView(CreateView):
    model = Topic
    template_name = "create_topic.html"
    fields = '__all__'


class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = 'topic', 'text', 'name'
