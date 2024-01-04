from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class ShowTable(models.Model):
    Date = models.DateField
    CIF = models.IntegerField
