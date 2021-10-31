# api/urls.py : App urls.py
from django.conf.urls import url
from django.urls import path, include
from .views import (
    StatesApiView,
    ResultsDataApiView
)

urlpatterns = [
    path('states/', StatesApiView.as_view()),
    path('results/', ResultsDataApiView.as_view()),
]