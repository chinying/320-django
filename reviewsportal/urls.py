from django.conf.urls import url

from reviewsportal import views

app_name = "reviews"

urlpatterns = [
    url(r"^company/$", views.CompanyListView.as_view(), name="company-list"),
    url(r"^company/new$", views.CompanyCreateView.as_view(), name="company-new"),

    url(r"^review/new$", views.ReviewCreateView.as_view(), name="review-new"),
]
