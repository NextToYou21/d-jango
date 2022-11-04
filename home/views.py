from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(requesst):
    
    Blogdata=Blog.objects.all()
    context={"Blog":Blogdata}

    return render(requesst, "index.html", context=context)