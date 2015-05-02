from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^moto/$', MotoListView.as_view(), name='moto-list'),
    url(r'^moto/(?P<pk>\d+)/$', MotoDetailView.as_view(), name='moto-detail'),
    url(r'^moto/add/$', MotoCreateView.as_view(), name='moto-add'),
    url(r'^moto/editar/(?P<pk>\d+)/$', MotoUpdateView.as_view(), name='moto-edit'),
    url(r'^moto/deletar/(?P<pk>\d+)/$', MotoDeleteView.as_view(), name='moto-delete'),

    url(r'^cliente/$', ClienteListView.as_view(), name='cliente-list'),
    url(r'^cliente/(?P<pk>\d+)/$', ClienteDetailView.as_view(), name='cliente-detail'),
    url(r'^cliente/add/$', ClienteCreateView.as_view(), name='cliente-add'),
    url(r'^cliente/editar/(?P<pk>\d+)/$', ClienteUpdateView.as_view(), name='cliente-edit'),
    url(r'^cliente/deletar/(?P<pk>\d+)/$', ClienteDeleteView.as_view(), name='cliente-delete'),
    

    url(r'^venda/$', VendaListView.as_view(), name='venda-list'),
    url(r'^venda/(?P<pk>\d+)/$', VendaDetailView.as_view(), name='venda-detail'),
    url(r'^venda/add/$', VendaCreateView.as_view(), name='venda-add'),
    url(r'^venda/editar/(?P<pk>\d+)/$', VendaUpdateView.as_view(), name='venda-edit'),
    url(r'^venda/deletar/(?P<pk>\d+)/$', VendaDeleteView.as_view(), name='venda-delete'),

    url(r'^peca/$', PecaListView.as_view(), name='peca-list'),
    url(r'^peca/(?P<pk>\d+)/$', PecaDetailView.as_view(), name='peca-detail'),
    url(r'^peca/add/$', PecaCreateView.as_view(), name='peca-add'),
    url(r'^peca/editar/(?P<pk>\d+)/$', PecaUpdateView.as_view(), name='peca-edit'),
    url(r'^peca/deletar/(?P<pk>\d+)/$', PecaDeleteView.as_view(), name='peca-delete'),



    url(r'^admin/', include(admin.site.urls)),
)
