from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core import serializers
from .forms import ContactForm
from .models import Contactdb

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from test1.serializers import contactserializer
from rest_framework.decorators import api_view

# Create your views here.
def indexView(request):
    return render(request,'home.html')


def registerView(request):
    form= ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        form.save()
    context= {'form': form}
    return render(request, 'contact/register.html',context)
    
@api_view(['GET','POST'])  #decorator responsible for get and post request
def contact_list(request):  #view fn for getting and posting data
    if  request.method == 'GET':
        contacts = Contactdb.objects.all()
        
        name = request.GET.get('name',None) #get name value
        if name is not  None:
            contacts = contacts.filter(name_icontains=name)
            #icontains checks if either the name or the description field contains the value of search _items. 
        contact_serializer = contactserializer(contacts,many=True) 
        #many=true is used for getting multiple data and serialize in order
        return JsonResponse(contact_serializer.data,safe=False)
    #'safe=false for objects serialization
    
    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = contactserializer(data=contact_data) #stores the serialized data from the serializer class.
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(contact_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def contact_detail(request, pk):
    try:
        contacts = Contactdb.objects.get(pk=pk)
    except Contacts.DoesNotExit:
        return JsonResponse({'message': 'The country does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        contact_serializer = contacterializer(countries)
        return JsonResponse(contact_serializer.data)
    
    elif request.method == 'PUT':
        contact_data = JSONParser().parser(request)
        contact_serializer = contactserializer(contacts, data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data)
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        contacts.delete()
        return JsonResponse({'message':'Country was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
