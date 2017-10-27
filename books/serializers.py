from rest_framework import serializer
from .models import Author, Book, Publisher

class AuthorSerializer(serializer.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializer.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
