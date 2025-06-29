from django.urls import path,include
from . views import *
from . routers import *
urlpatterns = [
    # path('fund/<int:pk>/', FundViews.as_view(), name='fund-detail'),
    # path('fund/', FundViews.as_view(), name='fund-detail'),
    path('api/',include(router.urls) , name='fund-detail'),

]