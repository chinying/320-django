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


class ReviewCreateForm(forms.Form):
    rating_choices = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )

    company = forms.CharField(required=True, widget=forms.TextInput())
    title = forms.CharField(required=True)
    body = forms.CharField(widget=forms.Textarea, required=False)

    mentorship = forms.ChoiceField(choices=rating_choices, widget=forms.RadioSelect)
    work_life_balance = forms.ChoiceField(choices=rating_choices, widget=forms.RadioSelect)
    personal_growth = forms.ChoiceField(choices=rating_choices, widget=forms.RadioSelect)

    salary = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(ReviewCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CompanyFilterForm(forms.Form):
    company_name = forms.CharField(required=False)

    def __init__(self, request, *args, **kwargs):
        super(CompanyFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
