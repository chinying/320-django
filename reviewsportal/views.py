from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, FormView

from reviewsportal.forms import CompanyCreateForm, CompanyFilterForm, ReviewCreateForm
from reviewsportal.models import Company, Review
from reviewsportal.utils import CompanyFilter


class CompanyListView(ListView):
    model = Company
    template_name = "companies/list.html"
    context_object_name = "companies"

    def get_queryset(self):
        return CompanyFilter(self.request).filter_queryset()

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context["form"] = CompanyFilterForm(self.request)
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = "companies/company_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        company = get_object_or_404(Company, pk=self.kwargs["pk"])
        context["company"] = company

        whitelist = {"date": "created_at", "rating": "overall_rating"}
        sort_paramater = self.request.GET.get("sort")
        sort = whitelist[sort_paramater] if sort_paramater in whitelist else None
        if sort:
            context["sorted_reviews"] = company.get_reviews(sortby=sort)
        else:
            context["sorted_reviews"] = company.get_reviews()
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


class ReviewCreateView(SuccessMessageMixin, LoginRequiredMixin, FormView):
    template_name = "reviews/new.html"
    success_url = reverse_lazy("reviews:company-list")
    success_message = "Thank you for submitting your review!"

    def get_form_class(self):
        return ReviewCreateForm

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        company_name = cleaned_data.get("company")
        company, _ = Company.objects.get_or_create(name=company_name)
        Review.objects.create(author=self.request.user, company=company, title=cleaned_data.get("title"),
            body=cleaned_data.get("body"), mentorship_rating=cleaned_data.get("mentorship"),
            work_life_balance_rating=cleaned_data.get("work_life_balance"),
            personal_growth_rating=cleaned_data.get("personal_growth"),
            salary=cleaned_data.get("salary"))
        return super(ReviewCreateView, self).form_valid(form)
