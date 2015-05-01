from django.shortcuts import render
from core.models import Moto, Cliente
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):
	template_name = 'index.html'

class MotoListView(ListView):
	model = Moto
	paginate_by = 2


class MotoDetailView(DetailView):
	model = Moto

class MotoCreateView(CreateView):
	model = Moto
	success_url = '/moto/'


class MotoUpdateView(UpdateView):
	model = Moto
	success_url = '/moto/'


class MotoDeleteView(DeleteView):
	model = Moto
	success_url = reverse_lazy('moto-list')



class ClienteListView(ListView):
	model = Cliente


class ClienteDetailView(DetailView):
	model = Cliente

class ClienteCreateView(CreateView):
	model = Cliente
	success_url = reverse_lazy('cliente-list')


class ClienteUpdateView(UpdateView):
	model = Cliente
	success_url = reverse_lazy('cliente-list')


class ClienteDeleteView(DeleteView):
	model = Cliente
	success_url = reverse_lazy('cliente-list')