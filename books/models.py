# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


class BooksAuthor(models.Model):
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'books_author'


class BooksBook(models.Model):
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_book'
        ordering = ['-download_count']


class BooksBookAuthors(models.Model):
    book = models.ForeignKey(
        BooksBook, models.DO_NOTHING, related_name='author')
    author = models.ForeignKey(BooksAuthor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_authors'
        unique_together = (('book', 'author'),)


class BooksBookBookshelves(models.Model):
    book = models.ForeignKey(
        BooksBook, models.DO_NOTHING, related_name='bookshelf')
    bookshelf = models.ForeignKey('BooksBookshelf', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_bookshelves'
        unique_together = (('book', 'bookshelf'),)


class BooksBookLanguages(models.Model):
    book = models.ForeignKey(
        BooksBook, models.DO_NOTHING, related_name='language')
    language = models.ForeignKey('BooksLanguage', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_languages'
        unique_together = (('book', 'language'),)


class BooksBookSubjects(models.Model):
    book = models.ForeignKey(
        BooksBook, models.DO_NOTHING, related_name='subject')
    subject = models.ForeignKey('BooksSubject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_subjects'
        unique_together = (('book', 'subject'),)


class BooksBookshelf(models.Model):
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'books_bookshelf'


class BooksFormat(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(
        BooksBook, models.DO_NOTHING, related_name='bookformat')

    class Meta:
        managed = False
        db_table = 'books_format'


class BooksLanguage(models.Model):
    code = models.CharField(unique=True, max_length=4)

    class Meta:
        managed = False
        db_table = 'books_language'


class BooksSubject(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'books_subject'
