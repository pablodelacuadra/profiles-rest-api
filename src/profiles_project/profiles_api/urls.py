from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()

router.register('hello-viewset',HelloViewset,base_name = 'hello-viewset')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('',include(router.urls))
    
]