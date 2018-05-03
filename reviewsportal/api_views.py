from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reviewsportal.models import Company

class CompanyListView(APIView):
    def get(self, request, *args, **kwargs):
        resp = Company.objects.values('id', 'name')
        query_params = request.query_params
        if 'name' in query_params:
            name = query_params.get('name')
            if name:
                resp = Company.objects.filter(username__icontains=name).values('id', 'name')
        return Response(resp, status=status.HTTP_200_OK)
