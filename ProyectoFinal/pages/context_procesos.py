# Cargo el modelo de las paginas
from pages.models import Page

# Defino una vista, que retornara las paginas creadas
def get_pages(request):
    # Extraigo los valores que  me interesan, filtrando por visibilidad
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id','title','slug')
    # Retorno los valores
    return {'pages':pages}
