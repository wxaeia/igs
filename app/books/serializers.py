from django.db.models import fields
from requests import models
from rest_framework import serializers
from django.utils import timezone
from .models import (
    BooksBook,
    BooksBookAuthors,
    BooksAuthor,
    BooksBookBookshelves,
    BooksBookLanguages,
    BooksBookSubjects,
    BooksBookshelf,
    BooksFormat,
    BooksLanguage
)
from django.db import transaction


class BooksBookAuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksBookAuthors
        fields = '__all__'
        depth = 1


class BooksBookBookshelvesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksBookBookshelves
        fields = ['bookshelf', ]
        depth = 1


class BooksBookLanguagesSerializer(serializers.ModelSerializer):
    # language = BooksLanguageSerializer(read_only=True)

    class Meta:
        model = BooksBookLanguages
        fields = ['language']
        depth = 1


class BooksBookSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookSubjects
        fields = ['subject']
        depth = 1


class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        fields = ['url', 'mime_type']
        depth = 1


class BooksBookSerializer(serializers.ModelSerializer):
    """ Serialiser with few specific fields about each BooksBook """
    book_id = serializers.IntegerField(source='gutenberg_id')
    author = BooksBookAuthorsSerializer(many=True)
    bookshelf = BooksBookBookshelvesSerializer(many=True)
    language = BooksBookLanguagesSerializer(many=True)
    subject = BooksBookSubjectsSerializer(many=True)
    bookformat = BooksFormatSerializer(many=True)

    class Meta:
        model = BooksBook
        fields = ['id', 'book_id', 'title', 'author', 'bookshelf',
                  'language', 'subject', 'bookformat']
