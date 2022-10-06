from django.urls import path
from . import viewsets

"""
Blog Routes
"""

urlpatterns = [
    path("", viewsets.IndexView.as_view(), name="index"),
    path("register/", viewsets.UserRegisterView.as_view(), name="register"),
    path("login/", viewsets.UserRegisterView.as_view(), name="login"),
    path("about/", viewsets.about_view, name="about"),
    path("news/<int:pk>", viewsets.news_detail_view, name="news-detail"),
    path("add_post", viewsets.AddPostView.as_view(), name="add-post"),
]
