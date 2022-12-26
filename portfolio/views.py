from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from portfolio.models import Portfolio, Post, Contact


# Create your views here.


class PortfolioView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'portfolios': Portfolio.objects.all(),
            'news': Post.objects.all(),
        }


class ContactView(CreateView):
    model = Contact
    fields = ('name', 'email', 'message')
    success_url = reverse_lazy('portfolio')
    template_name = 'index.html'
