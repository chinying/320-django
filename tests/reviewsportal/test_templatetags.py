import pytest

from reviewsportal.templatetags.reviews_tags import modify_site_name
from django.test import TestCase


class TestModifySiteName(TestCase):
    def test_modify_site_name(self):
        site = "example.com"
        assert modify_site_name(site) == "http://example.com"

        # ensure that https does not get stripped
        site = "https://example.com"
        assert modify_site_name(site) == "https://example.com"

        # test that paths are not stripped
        site = "https://example.com/path/"
        assert modify_site_name(site) == site
