from rest_framework import serializers
from books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    """
    Books DB Serializer
    """

    class Meta:
        model = Books
        fields = "__all__"
