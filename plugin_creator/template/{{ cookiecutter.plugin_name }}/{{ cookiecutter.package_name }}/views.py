"""API views for the {{ cookiecutter.plugin_name }} plugin.

In practice, you would define your custom views here.

Ref: https://www.django-rest-framework.org/api-guide/views/
"""

from datetime import date
import random
import string

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ExampleSerializer


class ExampleView(APIView):
    """Example API view for the {{ cookiecutter.plugin_name }} plugin.
    
    This view returns some very simple example data,
    but the concept can be extended to include more complex logic.
    """

    # You can control which users can access this view using DRF permissions
    permission_classes = [permissions.IsAuthenticated]

    # Control how the response is formatted
    serializer_class = ExampleSerializer

    def get(self, request, *args, **kwargs):
        """Override the GET method to return example data."""

        from part.models import Part

        response_serializer = self.serializer_class(data={
            'random_text': ''.join(random.choices(string.ascii_letters, k=50)),
            'part_count': Part.objects.count(),
            'today': date.today()
        })

        # Serializer must be validated before it can be returned to the client
        response_serializer.is_valid(raise_exception=True)

        return Response(
            response_serializer.data,
            status=200
        )
