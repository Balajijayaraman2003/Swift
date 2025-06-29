from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Authentication.views import *

from .routers import *

urlpatterns = [
    path('api/',include(router.urls)),
]