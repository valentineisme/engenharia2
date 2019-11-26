"""autoauction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from aa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^cadastro_usuario/$', views.cadastro_usuario, name='cadastro_usuario'),
    url(r'^acesso_negado/$', views.index, name='acesso_negado'),
    url(r'^logar/$', views.validacao, name='logar'),
    url(r'^sair/$', views.sair, name='sair'),

    url(r'^perfil/editar/$', views.usuario_editar, name='usuario_editar'),
    url(r'^editar_usuario_final/$', views.usuario_editar_final, name='editar_usuario_final'),

    url(r'^cadastro_veiculo/$', views.cadastro_veiculo, name='cadastro_veiculo'),
    url(r'^leiloar_veiculo/$', views.leiloar_veiculo, name='leiloar_veiculo'),
    url(r'^leiloar_veiculo/leiloando/$', views.leiloando, name='leiloando'),
    url(r'^em_leilao/$', views.em_leilao, name='em_leilao'),
    url(r'^leilao_ativo/$', views.leilao_ativo, name='leilao_ativo'),
    url(r'^leilao_ativo/ativar/$', views.leilao_ativar, name='leilao_ativar'),

    url(r'^lances/$', views.lances, name='lances'),

    url(r'^ajax/pesquisa/$', views.ajax_pesquisa, name='ajax_pesquisa'),

]
