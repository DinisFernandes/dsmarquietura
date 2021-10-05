from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Projeto, GaleriaPhotos, Testemunho, Contact

# Create your views here.

class ProjetoList(ListView):
    model = Projeto
    template_name = 'projeto_list.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context.update({
            'projetos': Projeto.objects.all().order_by('?')[:4],
            'testemunhos': Testemunho.objects.all().order_by('?'),
            'conta': Testemunho.objects.all().count()
        })
        return context



class Servicos(TemplateView):
    template_name = 'website/services.html'

class Contatos(TemplateView):
    template_name = 'website/contact.html'

class ProjetoDetail(DetailView):
    model = Projeto

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context.update({
            'items': GaleriaPhotos.objects.filter(projeto__pk=self.kwargs.get('pk')).count(),
            'todos': GaleriaPhotos.objects.filter(projeto__pk=self.kwargs.get('pk')),
        })
        return context


def save_form(request):
    name = request.POST['name']
    telefone = request.POST['telm']
    email = request.POST['email']
    message = request.POST['message']

    if type(telefone) != int:
        telefone=0

    Contact.objects.create(
        name = name,
        telefone = telefone,
        email = email,
        message = message,
        tratado = False,
    )
    return render(request, 'contact_success.html',{'name':name})

class TodosList(ProjetoList):
    template_name = 'website/projetos_list.html'
    paginate_by = 16

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-data_post')
        return qs

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #
    #     context.update({
    #         'projetos': Projeto.objects.all().order_by('-data_post'),
    #         'conta': Projeto.objects.all().count()
    #     })
    #     return context