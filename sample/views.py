from rest_framework import viewsets, parsers

from .models import Sample
from .serializers import SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]