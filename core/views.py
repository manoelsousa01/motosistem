from django.shortcuts import render
from core.models import Cliente, Moto, Venda, Peca, Item
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSet
from django.http import HttpResponseRedirect

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


# Pecas
class PecaListView(ListView):
	model = Peca

class PecaDetailView(DetailView):
	model = Peca

class PecaCreateView(CreateView):
	model = Peca
	success_url = reverse_lazy('peca-list')


class PecaUpdateView(UpdateView):
	model = Peca
	success_url = reverse_lazy('peca-list')

class PecaDeleteView(DeleteView):
	model = Peca
	success_url = reverse_lazy('peca-list')

#-Cliente
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

#venda
class VendaListView(ListView):
	model = Venda

class VendaDetailView(DetailView):
	model = Venda

class ItemInline(InlineFormSet):
	model = Item
	extra = 5

class VendaCreateView(CreateWithInlinesView):
	model = Venda
	fields = ('cliente', 'funcionario')
	inlines = [ItemInline]
	success_url = reverse_lazy('venda-list')
	def forms_valid(self, form, inlines):
		self.obj = form.save()
		valor_total_venda = 0
		for inline in inlines:
			for item in inline:
				if 'quantidade' in item.cleaned_data.keys():
					valor_total_venda += item.cleaned_data['quantidade'] * item.cleaned_data['valor_unitario']
					peca = Peca.objects.get(nome = item.cleaned_data['peca'])
					peca.quantidade -= item.cleaned_data['quantidade']
					peca.save()
		self.obj.valor_total = valor_total_venda
		self.obj.save()
		return HttpResponseRedirect(self.get_success_url())

class VendaUpdateView(UpdateView):
	model = Venda
	success_url = reverse_lazy('venda-list')

class VendaDeleteView(DeleteView):
	model = Venda
	success_url = reverse_lazy('venda-list')