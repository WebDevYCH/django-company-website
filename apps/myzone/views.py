from django.views.generic import ListView
from .models import *
from agrosite.settings import *


class TalkView(ListView):
    template_name = "myzone/talk.html"
    context_object_name = "lists"
    paginate_by = ARTICLE_PAGINATE_BY


    def get_queryset(self):
        print(self.request.POST.dict())
        return TalkContent.objects.filter(status='y')

