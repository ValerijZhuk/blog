from django.shortcuts import render, get_object_or_404

from blog.forms import CreateCommentForm
from blog.models import Topic, Post, Comment
from django.views.generic import CreateView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import CreateCommentForm


def get_topics(request):
    topics = Topic.objects.all()
    context = {
        "topics": topics
    }
    return render(request, "topics.html", context)


def get_topic_posts(requests, pk):
    posts = Post.objects.filter(topic__id=pk)
    context = {
        'posts': posts,
        'topic_id': pk,
    }
    return render(requests, "posts.html", context)


def like_view(request, pk):
    id = request.POST.get("post_id")
    post = Post.objects.get(id=id)
    post.likes_count += 1
    post.save()
    return HttpResponseRedirect(reverse("posts", args=[str(pk)]))


class AddTopicView(CreateView):
    model = Topic
    template_name = "create_topic.html"
    fields = '__all__'


class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = 'topic', 'text', 'name'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class CreateCommentView(CreateView):
    model = Comment
    template_name = 'create_comment.html'
    fields = '__all__'
    # form_class = CreateCommentForm
