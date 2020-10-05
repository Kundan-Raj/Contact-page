from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def indexView(request):
    return render(request,'home.html')


def registerView(request):
    name=''
    email=''
    comment=''

    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        comment=form.cleaned_data.get("comment")

      #  if request.user.is_authenticated():
      #      subject= str(request.user) + "'s Comment"
        #else:
         #   subject= "A Visitor's Comment"


       # comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
       # send_mail(subject, comment, 'dlhylton@gmail.com', [email])


        context= {'form': form}

        return render(request, 'contact/register.html', context)

    else:
        context= {'form': form}
        return render(request, 'contact/register.html', context)

