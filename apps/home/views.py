from django.shortcuts import render, get_object_or_404, HttpResponse
from datetime import datetime
# Create your views here.
from django.views.generic import ListView,DetailView, CreateView
from blogs.models import Post
from .models import Portfolio, Messages
# Create your views here.
class HomeListView(ListView):
    template_name = 'main/index.html'  # 指定页面模板
    context_object_name = 'home'           # 指定传参变量名
    extra_context={
        'title':'Home Page',
        'year':datetime.now().year,
    }
    
    def get_queryset(self):
        queryset = {'blogs': Post.objects.filter(status='p'), 
                    'portfolio': Portfolio.objects.all().filter()}
        return queryset
    
    
class HomeView(HomeListView):
    pass

class PortfolioListView(ListView):
    """Renders the about page."""
    template_name = 'main/portfolio.html'  
    context_object_name = 'lists'           
    extra_context={
        'title':'Home Page',
        'year':datetime.now().year,
    }
    
    def get_queryset(self):
        return Portfolio.objects.all()

def messages(request):
    messages = Messages.objects.get(pk=1)
    return render(request, 'blog/messages.html', {'messages': messages})
