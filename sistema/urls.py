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
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
