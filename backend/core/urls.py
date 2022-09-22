from django.urls import path
from . import views
from django.urls import path, re_path
from .views import Post

urlpatterns = [
    re_path(r'^post/$', views.post_list),
    re_path(r'^posts/([0-9])$', views.posts_detail),
    ]
