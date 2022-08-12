#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

#def index(request):
    #return HttpResponse("Bienvenue à la Librairie NOOR de Aïdégnon.")

def index(request):
    return render(request, "base.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("Accueil:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "/librairie/Accueil/templates/register.html",{"register_form":form})  
    #return render (request=request, template_name="/librairie/Accueil/templates/register.html", context={"register_form":form})