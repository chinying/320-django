from django import forms
from django.core.validators import URLValidator

from reviewsportal.models import Company, Review


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name", "site", "description")

    def __init__(self, *args, **kwargs):
        super(CompanyCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(CompanyCreateForm, self).clean()
        site = cleaned_data.get("site")
        # TODO: validate site


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("title", "body")

    def __init__(self, *args, **kwargs):
        super(ReviewCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
