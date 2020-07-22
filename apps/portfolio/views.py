from django.shortcuts import render, get_object_or_404, HttpResponse
from datetime import datetime
# Create your views here.
from django.views.generic import ListView,DetailView, CreateView
from .models import Portfolio
from django.http import Http404

class PortfolioListView(ListView):
    """Renders the about page."""
    template_name = 'portfolio/portfolio.html'  
    context_object_name = 'portfolios'           
    extra_context={
        'title':'Home Page',
        'year':datetime.now().year,
    }
    
    def get_queryset(self):
        return Portfolio.objects.all()

class PortfolioDetailsView(DetailView):
    model = Portfolio
    template_name = 'portfolio/details.html'
    context_object_name = 'portfolio'
    pk_url_kwarg = 'portfolio_id'

    def get_object(self, queryset=None):
        obj = super(PortfolioDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Portfolio doesn't exists")
        else:
            obj.viewed()
            self.object = obj
        return obj

    # def get_object(self, queryset=None):
    #     obj = super(JobDetailsView, self).get_object(queryset=queryset)
    #     if obj is None:
    #         raise Http404("Job doesn't exists")
    #     return obj

    def get_context_data(self, **kwargs):
        portfolio_id = int(self.kwargs[self.pk_url_kwarg])
        user = self.request.user
        
        kwargs['next_portfolio'] = self.object.next_portfolio
        kwargs['prev_portfolio'] = self.object.prev_portfolio

        return super(PortfolioDetailsView, self).get_context_data(**kwargs)
