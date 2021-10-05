from django.urls import path, include
from .views import ProjetoList, ProjetoDetail
from .views import Servicos, Contatos, save_form, TodosList


urlpatterns = [
    path('', ProjetoList.as_view(), name="projeto_list"),
    path('servicos/', Servicos.as_view(), name="services"),
    path('contatos/', Contatos.as_view(), name="contact"),
    path('projeto/<int:pk>/', ProjetoDetail.as_view(), name="projeto_detail"),
    path('save-form/', save_form, name='save_form'),
    path('projetos/', TodosList.as_view(), name="projetos_list"),
]