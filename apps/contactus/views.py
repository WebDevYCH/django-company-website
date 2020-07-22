from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from .models import Contact, MailBook
from django.http import HttpResponseRedirect

class ContactView(CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('contactus:contact')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        self.object = None
        
        form = self.get_form()
        if form.is_valid():

            messages.info(self.request, 'Successfully submited')
            return self.form_valid(form)
        
        return render(request, 'contact/contact.html', {'form': form})
