from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .filters import AuthorFilter, BookFilter
from .models import Author, Book
from .paginations import LimitPagination
from .permissions import IsSuperuserOrReadOnly
from .serializers import (AuthorSerializer, BookDetailSerializer,
                          BookListSerializer)


class BaseViewSet(viewsets.ModelViewSet):
    """
    Добавлена пагинация по лимиту.
    По умолчанию 10 записей на страницу.
    По желанию можно изменить лимит.
    Максимальное число для лимита - 100, что бы 
    при большом количестве пользователей и большом количестве книг снизить 
    нагрузку на сервер.
    """
    permission_classes = [IsSuperuserOrReadOnly]
    pagination_class = LimitPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class AuthorViewSet(BaseViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter
    ordering_fields = ['name']


class BookViewSet(BaseViewSet):
    """
    Для уменьшения запросов к базе данных используется select_related
    в queryset запросе.
    """
    queryset = Book.objects.all().select_related('author')
    list_serializer_class = BookListSerializer
    detail_serializer_class = BookDetailSerializer
    filterset_class = BookFilter
    ordering_fields = ['title',]

    def get_serializer_class(self):
        """
        Разные сериализаторы для списка и детализации.
        Что бы снизить нагрузку на сервер при запросе списка книг 
        из выдачи убрана информация  с предисловием и обложкой.
        Данную информацию можно получить только при детализации книги.
        """
        if self.action == 'list':
            return self.list_serializer_class
        return self.detail_serializer_class
