from django.urls import path
from .views import getinfo


urlpatterns = [
    path("info",getinfo,name="getInfo")
]
