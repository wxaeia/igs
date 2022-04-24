from .serializers import BooksBookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, mixins
from rest_framework.filters import SearchFilter

from .models import (BooksAuthor, BooksBook, BooksBookAuthors)
import django_filters

# class BooksBookFilter(filters.FilterSet):
#     class Meta:
#         model = BooksBook
#         fields = {'title': ['exact', 'in', 'startswith']}


# class BooksBookAuthorsFilter(filters.FilterSet):
#     author = filters.RelatedFilter(
#         BooksBookFilter, field_name='author', queryset=BooksBook.objects.all())

#     class Meta:
#         model = BooksBookAuthors
#         fields = {'author': ['exact', 'in', 'startswith']}

class BooksBookAuthorsFilter(django_filters.FilterSet):
    class Meta:
        model = BooksBookAuthors
        fields = ['author', ]


class BookFilter(django_filters.FilterSet):
    book_id = django_filters.CharFilter(
        field_name='gutenberg_id', lookup_expr='icontains')
    title = django_filters.CharFilter(
        field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(
        field_name='author__author__name', lookup_expr='icontains')
    language = django_filters.CharFilter(
        field_name='language__language__code', lookup_expr='icontains')
    mime_type = django_filters.CharFilter(
        field_name='bookformat__mime_type', lookup_expr='icontains')
    topic = django_filters.CharFilter(
        method='my_custom_filter', lookup_expr='icontains')

    class Meta:
        model = BooksBook
        fields = ['title', 'author', 'language', 'mime_type', 'topic', ]

    def my_custom_filter(self, queryset, name, value):
        bookshelf = 'bookshelf__bookshelf__name__icontains'
        subject = 'subject__subject__name__icontains'
        return queryset.filter(**{bookshelf: value}) | queryset.filter(**{subject: value})


class BooksViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ---
    # Books API's
    """
    serializer_class = BooksBookSerializer
    queryset = BooksBook.objects.exclude(
        download_count=None)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_class = BookFilter
