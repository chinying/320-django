from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from reviewsportal.models import Company


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30


class CompanyListView(APIView):
    def get(self, request, *args, **kwargs):
        resp = Company.objects.values('id', 'name')
        query_params = request.query_params
        if 'name' in query_params:
            name = query_params.get('name')
            if name:
                resp = Company.objects.filter(name__icontains=name).values('id', 'name')
        return Response(resp, status=status.HTTP_200_OK)


class GetCompanyReviews(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        query_params = request.query_params
        if 'id' in query_params:
            try:
                company = Company.objects.get(pk=query_params.get('id'))
                resp = company.get_reviews().values()
                return Response(resp, status=status.HTTP_200_OK)
            except Company.DoesNotExist:
                raise Http404
        return Response({'': ''}, status=status.HTTP_400_BAD_REQUEST)
