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
    created_at = models.DateTimeField(auto_now_add=True)

    # ratings
    mentorship_rating = models.IntegerField()
    work_life_balance_rating = models.IntegerField()
    personal_growth_rating = models.IntegerField()

    # this field is derived from the above ratings
    overall_rating = models.FloatField(blank=True, db_index=True)

    salary = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ratings = [self.mentorship_rating, self.work_life_balance_rating,
            self.personal_growth_rating]
        self.overall_rating = sum(ratings) / len(ratings)
        super(Review, self).save(*args, **kwargs)
