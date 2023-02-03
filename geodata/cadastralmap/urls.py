from django.urls import path
from .views import MainPageView, CadastralMapView
from . import views

urlpatterns = [
    path('', MainPageView.as_view(), name='cadastralmap'),
    path('result/', CadastralMapView.as_view(), name='result'),
]
