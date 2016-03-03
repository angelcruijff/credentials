from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from .models import Entry, Metadata, MetadataValue, EntryType

class Index(View):
    """
    Cuando vamos a crear una nueva orden
    """

    def get(self, request):
        context_dict = dict()
        return render(request, 'entries/index.html', context_dict)

    def post(self, request):
        context_dict = {}
        busqueda = request.POST.get('Entrada')
        entradas = Entry.objects.filter(name__icontains=busqueda).order_by('name')
        lista_entradas = []
        if entradas:
            for entrada in entradas:
                entry = {}
                valores = {}
                template = entrada.entry_type.template
                metadatos = Metadata.objects.filter(entry_type=entrada.entry_type)
                for metadato in metadatos:
                    llave = metadato.key
                    try:
                        valor = MetadataValue.objects.get(entry=entrada, metadata=metadato)
                        valores[llave] = valor.value
                    except ObjectDoesNotExist:
                        valores[llave] = ""
                temp = template.format_map(valores)
                entry['template'] = temp
                entry['nombre'] = entrada.name
                entry['metadatos'] = valores
                lista_entradas.append(entry)
            context_dict['Busqueda'] = True
            context_dict['entradas'] = lista_entradas
        return render(request, 'entries/index.html', context_dict)
