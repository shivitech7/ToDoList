from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import ToDo

# Create your views here.
     
class NewEntryForm(forms.Form):
    f_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    l_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))

class Login(forms.Form):
    Username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))

def index(request):
    if request.user.is_authenticated:
        task = ToDo.objects.all()
        context = {
            "tasks": task,

        }
    return HttpResponse("kal aana")

    return render(request, "ToDo/index.html", context)

def home(request):
    return render(request, "ToDo/layout.html")

def registration(request):
    registration_form = NewEntryForm()
    return render(request, "ToDo/registration.html",{
        "form" : registration_form
    })

def login(request):
    form = Login()
    if request.method == "POST":
        login_form = Login(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['Username']
            password = login_form.cleaned_data['Password']
            user = authenticate(username=username, password=password)
            if user is not None:
                return render(request, "ToDo/index.html")
            return HttpResponse("Not Logged in")
    return render(request, "ToDo/login.html",{
        "form" : form
    })


def submit(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            username = form.cleaned_data['username']
            Email = form.cleaned_data['Email']
            Password = form.cleaned_data['Password']
            user = User.objects.create_user( username, Email, Password)
            user.first_name = f_name
            user.last_name = l_name
            user.save()
            return render(request, "ToDo/index.html")
        return HttpResponse("Nooo")
    return HttpResponse("!!!!!!!!!")