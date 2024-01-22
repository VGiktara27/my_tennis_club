from django.db import models


class Member(models.Model):
    Member_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255, null=False, blank=True)
    lastname = models.CharField(max_length=255, null=False, blank=True)
    phone_number = models.CharField(max_length=255, null=False, default="", blank=True)
    email = models.CharField(max_length=255, null=False, default="", blank=True)

class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255, null=False, blank=True)
    lastname = models.CharField(max_length=255, null=False, blank=True)
    phone_number = models.CharField(max_length=255, null=False, default="", blank=True)
    email = models.CharField(max_length=255, null=False, default="", blank=True)




# class ShowTable(models.Model):
#     Date = models.DateField
#     CIF = models.IntegerField


class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    bookname = models.CharField(max_length=255, default="", null=True, blank=True)
    authorname = models.CharField(max_length=255, null=True, blank=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE,)
    # author_2=models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    publication_name = models.CharField(max_length=255, null=True, blank=True)


class Lent(models.Model):
    member_id = models.ForeignKey(Member,null=True,on_delete=models.CASCADE)
    book_id=models.ForeignKey(Books,null=True,on_delete=models.CASCADE)
    Date=models.DateField(null=False)


