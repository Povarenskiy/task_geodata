from .services import get_map
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """Отображение главной страницы"""
    template_name = 'cadastralmap/mainpage.html'


class CadastralMapView(TemplateView):
    """Отображение карты"""
    template_name = 'cadastralmap/resultmap.html'

    def get_context_data(self, **kwargs): 
        return get_map(self.request.GET.get('q'))







