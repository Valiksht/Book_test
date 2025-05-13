from rest_framework import viewsets

from .models import Author, Book
from .paginations import LimitPagination
from .permissions import IsSuperuserOrReadOnly
from .serializers import (AuthorSerializer, BookDetailSerializer,
                          BookListSerializer)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperuserOrReadOnly]
    pagination_class = LimitPagination

    def get_srializer_class(self):
        return self.serializer_class


class AuthorViewSet(BaseViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(BaseViewSet):
    queryset = Book.objects.all()
    list_serializer_class = BookListSerializer
    detail_serializer_class = BookDetailSerializer
