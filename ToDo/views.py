from django.http import HttpResponse
from django.shortcuts import render

from .models import ToDo

# Create your views here.
def index(request):
    task = ToDo.objects.all()
    context = {
        "tasks": task,

    }

    return render(request, "ToDo/index.html", context)
     