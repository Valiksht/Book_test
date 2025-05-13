from django.contrib import admin

from .models import Author, Book

class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    validate_min = False
    verbose_name = 'Книга'
    verbose_name_plural = 'Книги'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = (BookInline,)