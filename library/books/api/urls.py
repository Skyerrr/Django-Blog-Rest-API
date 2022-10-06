from django.urls import path
from books.api import viewsets

"""
Defining REST framework Routes
"""

urlpatterns = [
    path("api/books", viewsets.BooksDetail.as_view(), name="test1"),
    path("api/books/<str:id>/", viewsets.BooksInfo.as_view(), name="test2"),
]

# urlpatterns = [
#     url(r"^api/books$", viewsets.books_list),
#     url(r"^api/books/(?P<pk>[0-9]+)$", viewsets.books_detail),
#     url(r"^api/books/published$", viewsets.books_list_published),
# ]
