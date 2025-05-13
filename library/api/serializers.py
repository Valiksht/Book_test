from rest_framework import serializers

from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Author'''

    class Meta:
        model = Author
        fields = ('id', 'name', 'birth_date', 'biography')


class BookListSerializer(serializers.ModelSerializer):
    '''Сериализатор для списка книг'''

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_year')


class BookDetailSerializer(serializers.ModelSerializer):
    '''Сериализатор для детальной информации о книге'''

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'publication_year',
            'preface',
            'cover',
        )
