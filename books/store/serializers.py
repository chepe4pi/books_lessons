from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Book, UserBookRelation


class BookReaderSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class BooksSerializer(ModelSerializer):
    annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    owner_name = serializers.CharField(source='owner.username', default="",
                                       read_only=True)
    readers = BookReaderSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author_name', 'annotated_likes',
                  'rating', 'owner_name', 'readers')


class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')
