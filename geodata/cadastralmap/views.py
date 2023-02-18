from .services import get_map, create_docx
from django.views.generic import TemplateView
from .forms import DocxForm
from django.http import FileResponse, HttpResponse


class MainPageView(TemplateView):
    """Отображение главной страницы"""
    template_name = 'cadastralmap/mainpage.html'


class CadastralMapView(TemplateView):
    """Отображение карты"""
    template_name = 'cadastralmap/resultmap.html'

    def get_context_data(self, **kwargs):
        cadastral_number = self.request.GET.get('q') 
        map_data = get_map(cadastral_number)
        form = DocxForm(initial={'cadastral_number': cadastral_number})
        return {'map_data': map_data, 'form': form }
    

def get_docx(request):    
    form = DocxForm(request.POST)
    if form.is_valid():
        document = create_docx(**form.cleaned_data)
        return FileResponse(open(document, 'rb'))








