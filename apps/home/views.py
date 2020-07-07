from django.shortcuts import render, get_object_or_404, HttpResponse
from datetime import datetime
# Create your views here.
from django.views.generic import ListView,DetailView, CreateView
from blog.models import Article
from .models import  Messages
from portfolio.models import Portfolio
# Create your views here.
class HomeListView(ListView):
    template_name = 'main/index.html'  # 指定页面模板
    context_object_name = 'home'           # 指定传参变量名
    extra_context={
        'title':'Home Page',
        'year':datetime.now().year,
    }
    def get_context_data (self, ** kwargs):
        context = super (). get_context_data (** kwargs)
        context ['blogs'] = Article.objects.filter(status='p')
        context ['portfolios'] = Portfolio.objects.all().filter()
        return context
        
    def get_queryset(self):
        return Portfolio.objects.all()
    
class HomeView(HomeListView):
    pass


def messages(request):
    messages = Messages.objects.get(pk=1)
    return render(request, 'blog/messages.html', {'messages': messages})
