from django.urls import path

from portfolio.views import PortfolioView, ContactView

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('contact', ContactView.as_view(), name='contact')
]