from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
# Create your views here.
from django.views.generic import ListView
# Create your views here.
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )