from django.urls import path,include
from .routers import *

urlpatterns=[
    path("api/",include(router.urls),name="event_route")
]