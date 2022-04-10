from django.urls import path
from blog import views
from blog.views import AddTopicView, AddPostView

urlpatterns = []

urlpatterns += [
    path('', views.get_topics, name='topics'),
    path('posts/<int:pk>', views.get_topic_posts, name='posts'),
    path('create_topic/', AddTopicView.as_view(), name='create_topic'),
    path('posts/add_post/', AddPostView.as_view(), name='add_post'),
]
