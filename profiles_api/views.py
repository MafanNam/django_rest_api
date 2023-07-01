from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'User HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'massage': 'Hello!', 'an_apiview': an_apiview})
