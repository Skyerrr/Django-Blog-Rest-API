from typing import Type
from rest_framework.request import Request
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import Http404
from django.http.response import HttpResponse
from django.core.cache import cache
from .. import models


class UserRegisterView(CreateView):
    """
    Generic class-based view class for User Registration.
    Takes care of Registration Forms
    Updates DB models.User with user form input data.
    """

    form_class = UserCreationForm
    template_name = "registration/register.html"
    sucess_url = reverse_lazy("login")


class IndexView(ListView):
    """
    Generic class-based view for blog home page.
    render index.html with a list of all news models
    """

    model = models.News
    template_name = "index.html"


class AddPostView(CreateView):
    """
    Generic class-based view to create a new post and redirect user to the created post
    Updates DB models.News with the user form input data.
    return user to created post page based on post int(primary key)
    """

    model = models.News
    template_name = "add-post.html"
    fields = "__all__"


def news_detail_view(request: Type[Request], pk: int) -> Type[HttpResponse]:
    """
    Filter models.News table by primary key.
    View function to verify if models.News page is in cache.
    if not, store it cache and return desired models.News page.
    Raise HTTP 404 if not found.
    params:
    pk -> models.News int primary key
    """

    if cache.get(pk):
        print("DATA FROM CACHE")
        post = cache.get(pk)

    else:
        try:
            post = models.News.objects.get(pk=pk)
            cache.set(pk, post)
            print("DATA FROM DB")

        except models.News.DoesNotExist as exc:
            raise Http404("News does not exist") from exc

    context = {"post": post}

    return render(request, "post.html", context)


def about_view(request: Type[Request]) -> Type[HttpResponse]:
    """
    View function to render about page
    return about.html
    """
    return render(request, "about.html")
