import markdown
from .models import *
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.shortcuts import render, get_object_or_404, HttpResponse
from agrosite.settings import *
import os


class ArticleListView(ListView):
    template_name = 'blogs/blog_list.html'  
    context_object_name = 'posts'           
    paginate_by = ARTICLE_PAGINATE_BY  

    def get_queryset(self):
        return Post.objects.filter(status='p')



class IndexView(ArticleListView):
    pass


class ArchivesView(ArticleListView):
    template_name = 'blogs/archives.html'
    paginate_by = None



class TagsView(ListView):
    model = Tag
    template_name = 'blogs/tags.html'
    context_object_name = 'tags'



class TagListView(ArticleListView):
    template_name = 'blogs/tag_list.html'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        self.tag_name = tag.name
        return Post.objects.filter(tag=tag, status='p')

    def get_context_data(self, **kwargs):
        kwargs['tag_name'] = self.tag_name
        return super(TagListView, self).get_context_data(**kwargs)



class Categories(ArticleListView):
    template_name = 'blogs/category_list.html'
    paginate_by = None

    def get_context_data(self, **kwargs):
        self.cate_count = Category.objects.all().count()
        kwargs['cate_count'] = self.cate_count
        return super(Categories, self).get_context_data(**kwargs)



class CategoryView(ArticleListView):
    template_name = 'blogs/category.html'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        self.cate_name = cate.name
        return Post.objects.filter(category=cate, status='p')

    def get_context_data(self, **kwargs):
        kwargs['cate_name'] = self.cate_name
        return super(CategoryView, self).get_context_data(**kwargs)


def article(request, pk):
    post = get_object_or_404(Post, pk=pk)
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

    relative_posts = Post.objects.filter(category_id=post.category_id, status='p').exclude(pk=pk).order_by('?')[:4]

    context = {}
    context['post'] = post
    context['author'] = author
    context['category'] = category
    context['relative_posts'] = relative_posts
    return render(request, 'blogs/single_post.html', context)



def file_test(request):
    file_path = os.path.join(STATIC_ROOT, "1.txt")
    file = open(file_path, "rb")
    response = HttpResponse(file)
    print(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=1.txt'
    return response



