from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    site = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Review(models.Model):
    author = models.ForeignKey(User, blank=True)
    company = models.ForeignKey(Company, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()

    # ratings
    mentorship_rating = models.IntegerField()
    work_life_balance_rating = models.IntegerField()
    personal_growth_rating = models.IntegerField()

    salary = models.IntegerField(null=True, blank=True)
