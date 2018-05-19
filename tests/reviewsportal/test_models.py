from django.test import TestCase

from mixer.backend.django import mixer
from reviewsportal.models import Company, Review


class TestModels(TestCase):
    def test_reviews_overall_rating(self):
        ratings_fields = set()
        for field in Review._meta.get_fields():
            if field.name.endswith("rating"):
                ratings_fields.add(field.name)
        ratings_fields.remove('overall_rating')

        mixer.blend(Review, mentorship_rating=60,
            work_life_balance_rating=40, personal_growth_rating=80)
        review = Review.objects.last()
        overall_rating = 0.0

        for field in ratings_fields:
            overall_rating += getattr(review, field)

        assert review.overall_rating == 60
