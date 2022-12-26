from django.urls import path

from portfolio.views import PortfolioView

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio')
]