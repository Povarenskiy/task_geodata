from django.urls import path
from .views import MainPageView, CadastralMapView, get_docx
from . import views

urlpatterns = [
    path('', MainPageView.as_view(), name='cadastralmap'),
    path('result/', CadastralMapView.as_view(), name='result'),
    path('get-docx/', get_docx, name='get_docx'),
]
