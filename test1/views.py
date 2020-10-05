from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from .forms import ContactForm
from django.core.mail import send_mail

from .models import Contactdb

# Create your views here.
def indexView(request):
    contactlist = Contactdb.objects.order_by('id')
    context = {'contactlist':contactlist}
    return render(request,'home.html',context)


def registerView(request):

    form= ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        form.save()

    context= {'form': form}

    return render(request, 'contact/register.html', context)


