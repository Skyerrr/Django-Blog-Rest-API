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
    Generic class-based view class for User Registration
    """

    form_class = UserCreationForm
    template_name = "registration/register.html"
    sucess_url = reverse_lazy("login")


class IndexView(ListView):
    """
    Generic class-based view for a list of blogs posted by a particular BlogAuthor.
    """

    model = models.News
    template_name = "index.html"


class AddPostView(CreateView):
    """
    Generic class-based view to create a new post and redirect user to the created post
    """

    model = models.News
    template_name = "add-post.html"
    fields = "__all__"


# def news_detail_view(request: Type[Request], pk: int) -> Type[HttpResponse]:
#     """
#     View function to filter News table by primary key and return it and raise HTTP 404 if not found.
#     """

#     try:

#         post = models.News.objects.get(pk=pk)

#     except models.News.DoesNotExist:
#         raise Http404("News does not exist")

#     return render(request, "post.html", context={"post": post})


def news_detail_view(request: Type[Request], pk: int) -> Type[HttpResponse]:
    """
    View function to verify if data is in cache, if not store in cache,
    filter News table by primary key and return it and raise HTTP 404 if not found.
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
    """
    return render(request, "about.html")


# def quoteThankyou(request: Type[Request], pk: int):
#     """
#     Function to send email to all users
#     """
#     all_users = models.User.objects.all()
#     post = models.News.objects.get(pk=pk)
#     for user in all_users:

#     subject = f"Hello {user.username} we have a new post!"
#     message = f"Hey come check this out! {post.name} --- The best {post.category_id.name} News of all time!"
#     send_mail(
#         subject,
#         message,
#         "sender@email.com",
#         [f"{user.email}"],
#         fail_silently=False,
#     )

#     return render(request, "blog/quote_thankyou.html")
