from django.urls import path,include
from .views import *
app_name = "portfolio"
urlpatterns = [
    path('portfolio', PortfolioListView.as_view(), name='portfolio'),
    path(r'portfolio/<int:year>/<int:month>/<int:day>/<int:portfolio_id>/<slug:slug>.html', PortfolioDetailsView.as_view(), name='single_portfolio'),
]