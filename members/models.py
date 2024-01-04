from django.db import models


class Member(models.Model):
    author_id = models.IntegerField(max_length=255, primary_key=True),
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)


class ShowTable(models.Model):
    Date = models.DateField
    CIF = models.IntegerField


class Books(models.Model):
    book_id = models.IntegerField(max_length=255, primary_key=True),
    bookname = models.CharField(max_length=255),
    authorname = models.CharField(max_length=255, null=False),
    author_id = models.ForeignKey(Member, null=True, on_delete=models.CASCADE).IntegerField(max_length=255, null=False),
    publication_name = models.CharField(max_length=255, null=False)
