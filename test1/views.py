from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core import serializers
from .forms import ContactForm
from django.core.mail import send_mail

from .models import Contactdb

# Create your views here.
def indexView(request):
    contactlist = Contactdb.objects.all()
    context = {'contactlist':contactlist}
    return render(request,'home.html')


#def registerView(request):
 #   form= ContactForm(request.POST or None)
  #  if form.is_valid():
   #     name = form.cleaned_data['name']
    #    form.save()
    #context= {'form': form}
    #return render(request, 'contact/register.html', context)
    

def registerView(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = ContactForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
