from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(BooksBook)
admin.site.register(BooksAuthor)
admin.site.register(BooksFormat)
admin.site.register(BooksLanguage)
admin.site.register(BooksSubject)
admin.site.register(BooksBookshelf)
