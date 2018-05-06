class CompanyFilter(object):
    def __init__(self, request, *args, **kwargs):
        super(CompanyFilter, self).__init__(*args, **kwargs)
        self.request = request

    def get_url_parameters(self):
        """
        this function fetches GET parameters from the URL and returns them as a dictionary for processing
        rtype: dict
        """
        company_name = self.request.GET.get("company_name", None)

        return {
            "company_name": company_name
        }

    def filter_queryset(self):
        from reviewsportal.models import Company

        url_parameters = self.get_url_parameters()
        queryset = Company.objects.all()

        if url_parameters["company_name"]:
            queryset = queryset.filter(name__icontains=url_parameters["company_name"])

        return queryset
