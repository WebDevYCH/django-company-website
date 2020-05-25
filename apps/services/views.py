from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpRequest
from datetime import datetime

def services(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'services/services.html',
        {
            'title':'services',
            'message':'Your application services page.',
            'year':datetime.now().year,
        }
    )
