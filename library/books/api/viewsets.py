from typing import Type
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.api import serializers
from books import models


class BooksDetail(APIView):
    """
    Books View Get ALL and POST
    """

    def get(self, request: Type[Request]) -> Type[Response]:
        """
        Get Method
        """
        print(type(request))
        obj = models.Books.objects.all()
        serializer = serializers.BooksSerializer(obj, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Type[Request]) -> Type[Response]:
        """
        Post Method
        """

        serializer = serializers.BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BooksInfo(APIView):
    """
    Books View Get with ID, POST, PUT, PATCH AND DELETE
    """

    def get(self, request: Type[Request], id: str) -> Type[Response]:
        """
        GET Method by Specific ID
        """

        try:
            obj = models.Books.objects.get(id=id)
            print(type(request))

        except models.Books.DoesNotExist:
            msg = {"msg": "ID not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.BooksSerializer(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Type[Request], id: str) -> Type[Response]:
        """
        Put Method by Specific ID
        """

        try:
            obj = models.Books.objects.get(id=id)

        except models.Books.DoesNotExist:
            msg = {"msg": "ID not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.BooksSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Type[Request], id: str) -> Type[Response]:
        """
        Patch Method by Specific ID
        """

        try:
            obj = models.Books.objects.get(id=id)

        except models.Books.DoesNotExist:
            msg = {"msg": "ID not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.BooksSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Type[Request], id: str) -> Type[Response]:
        """
        Delete Method by Specific ID
        """

        try:
            obj = models.Books.objects.get(id=id)

        except models.Books.DoesNotExist:
            msg = {"msg": "ID not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
