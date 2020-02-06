from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView,DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ApplyJobForm
import markdown
from apps.blog.models import Post, Portfolio, TeamExpert
from apps.blog.models import Category,Job,Applicant
import django.utils.timezone as timezone
from django.utils.decorators import method_decorator

class ArticleListView(ListView):
    template_name = 'mysite/index.html'  # 指定页面模板
    context_object_name = 'home'           # 指定传参变量名
    extra_context={
        'title':'Home Page',
        'year':datetime.now().year,
    }
    
    def get_queryset(self):
        queryset = {'blogs': Post.objects.filter(status='p'), 
                    'portfolio': Portfolio.objects.all().filter()}
        return queryset


    
    
class HomeView(ArticleListView):
    pass

def article(request, pk):
    post = get_object_or_404(Post, pk=pk,)
    author = User.objects.get(id=post.author_id)
    category = Category.objects.get(id=post.category_id)
    post.increase_views()  
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.fenced_code',

    ])

    post.body = md.convert(post.body)
    if strip_tags(md.toc).strip() == '':
        post.toc = ''
    else:
       post.toc = md.toc

    # 获取相关文章
    relative_posts = Post.objects.filter(category_id=post.category_id, status='p').exclude(pk=pk).order_by('?')[:4]

    context = {}
    context['post'] = post
    context['author'] = author
    context['category'] = category
    context['relative_posts'] = relative_posts
    return render(request, 'mysite/blogs/article.html', context)

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mysite/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
class AboutView(ListView):
    template_name = 'mysite/about.html'  # 指定页面模板
    context_object_name = 'experts'           # 指定传参变量名
    extra_context={
        'title':'About Page',
        'year':datetime.now().year,
    }
    
    def get_queryset(self):
        queryset =  TeamExpert.objects.filter(status='p')
        return queryset

def services(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mysite/services.html',
        {
            'title':'services',
            'message':'Your application services page.',
            'year':datetime.now().year,
        }
    )

class PortfolioListView(ListView):
    """Renders the about page."""
    template_name = 'mysite/portfolio.html'  # 指定页面模板
    context_object_name = 'lists'           # 指定传参变量名
    extra_context={
        'title':'Home Page',
        'year':datetime.now().year,
    }
    
    def get_queryset(self):
        return Portfolio.objects.all()
    
class JobDetailsView(DetailView):
    model = Job
    template_name = 'mysite/jobs/details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class JobView(ListView):
    model = Job
    template_name = 'mysite/jobs/home.html'
    context_object_name = 'jobs'
    extra_context = {
        'title': 'career'
    }
    def get_queryset(self):
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        return context

class ApplyJobView(CreateView):
    model = Applicant
    form_class = ApplyJobForm
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Successfully applied for the job!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('mysite:home'))

    def get_success_url(self):
        return reverse_lazy('mysite:job_description', kwargs={'id': self.kwargs['job_id'],'slug': self.slug})

    # def get_form_kwargs(self):
    #     kwargs = super(ApplyJobView, self).get_form_kwargs()
    #     print(kwargs)
    #     kwargs['job'] = 1
    #     return kwargs

    def form_valid(self, form):
        # check if user already applied
        applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class SearchView(ListView):
    model = Job
    template_name = 'mysite/jobs/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(location__contains=self.request.GET['location'],
                                         title__contains=self.request.GET['position'])


class JobListView(ListView):
    model = Job
    template_name = 'mysite/jobs/jobs.html'
    context_object_name = 'jobs'
    paginate_by = 5