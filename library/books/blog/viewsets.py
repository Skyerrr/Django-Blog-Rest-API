from typing import Type
from rest_framework.request import Request
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import Http404
from django.http.response import HttpResponse
from .. import models


class UserRegisterView(CreateView):
    """
    Class for User Registration Form
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
    Class to create a new post.
    """

    model = models.News
    template_name = "add-post.html"
    fields = "__all__"


def news_detail_view(request: Type[Request], pk: int) -> Type[HttpResponse]:
    """
    Function to filter News table by primary key and return it and raise HTTP 404 if not found.
    """

    try:

        post = models.News.objects.get(pk=pk)

    except models.News.DoesNotExist:
        raise Http404("News does not exist")

    return render(request, "post.html", context={"post": post})


def about_view(request: Type[Request]) -> Type[HttpResponse]:
    """
    View function for about page
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
