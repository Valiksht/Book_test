from django_filters.rest_framework import FilterSet, CharFilter

from .models import Author, Book


class AuthorFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='startswith')

    class Meta:
        model = Author
        fields = ['name']

class BookFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='startswith')

    class Meta:
        model = Book
        fields = ['title']