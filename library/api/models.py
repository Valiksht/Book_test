from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО автора')
    birth_date = models.DateField(verbose_name='Дата рождения')
    biography = models.TextField(verbose_name='Автобиография')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name='Автор'
    )
    publication_year = models.PositiveIntegerField(verbose_name='Год издания')
    title = models.CharField(max_length=255, verbose_name='Название книги')
    preface = models.TextField(verbose_name='Предисловие')
    cover = models.ImageField(upload_to='covers/', verbose_name='Обложка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']
