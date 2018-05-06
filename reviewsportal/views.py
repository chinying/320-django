from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
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
    template_name = "companies/company_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context["company"] = get_object_or_404(Company, pk=self.kwargs["pk"])
        return context


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

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        company_name = cleaned_data.get("company")
        company, _ = Company.objects.get_or_create(name=company_name)
        Review.objects.create(author=self.request.user, company=company, title=cleaned_data.get("title"),
            body=cleaned_data.get("body"))
        return super(ReviewCreateView, self).form_valid(form)
