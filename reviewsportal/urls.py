from django.conf.urls import url

from reviewsportal import api_views, views

app_name = "reviews"

urlpatterns = [
    # apis
    url(r"^api/company/$", api_views.CompanyListView.as_view(), name="api-company-search"),

    url(r"^company/$", views.CompanyListView.as_view(), name="company-list"),
    url(r"^company/new$", views.CompanyCreateView.as_view(), name="company-new"),
    url(r"^company/(?P<pk>[-\w]+)/detail/$", views.CompanyDetailView.as_view(),
        name="company-detail"),

    url(r"^review/new$", views.ReviewCreateView.as_view(), name="review-new"),
]
