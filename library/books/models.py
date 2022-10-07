from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from . import sendemail

# Create your models here.


class Books(models.Model):
    """
    Books Rest API table
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}--{self.release_year}--{self.pages}"


class Category(models.Model):
    """
    Category table -> News
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class News(models.Model):
    """
    News table -> User, Category
    """

    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.name
            + " | "
            + str(self.author)
            + " | "
            + str(self.date)
            + " | "
            + str(self.category_id)
            + " | "
            + str(self.published)
        )

    def get_absolute_url(self):
        """
        sendemail.sending_email -> Send email to all users with superuser status
        Return User to the page that has been create
        post -> Blog post from News that has just be created.
        all_users -> all users from User table.
        """
        post = str(self.pk)
        all_users = User.objects.all()
        post = News.objects.get(pk=post)
        sendemail.sending_email(all_users, post)

        return reverse(
            "news-detail",
            args=[str(self.pk)],
        )
