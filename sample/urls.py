from rest_framework.response import Response
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SampleViewSet


router = DefaultRouter()
router.register('samples', SampleViewSet)

def hello(request):
    return Response(data='OK')

urlpatterns = [
    path('', include(router.urls)),
]

