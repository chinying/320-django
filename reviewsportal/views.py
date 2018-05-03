from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, FormView

from reviewsportal.forms import CompanyCreateForm, ReviewCreateForm
from reviewsportal.models import Company, Review


class CompanyListView(ListView):
    model = Company
    template_name = "companies/list.html"
    context_object_name = "companies"

    def get_queryset(self):
        qs = Company.objects.all()
        print(qs)
        return qs


class CompanyDetailView(DetailView):
    model = Company
    template_name = "companies/detail.html"


class CompanyCreateView(FormView):
    template_name = "companies/new.html"
    success_url = reverse_lazy("reviews:company-list")

    def get_form_class(self):
        return CompanyCreateForm

    def form_valid(self, form):
        form.save()
        return super(CompanyCreateView, self).form_valid(form)


class ReviewsListView(ListView):
    pass


class ReviewCreateView(FormView):
    template_name = "reviews/new.html"
    success_url = reverse_lazy("reviews:company-list")

    def get_form_class(self):
        return ReviewCreateForm
