from django.shortcuts import render
from django.http import HttpResponse
from .models import posts 
# Create your views here.
def index(request):
    po=posts.objects.all()[:10]
    context={
    'title':'products',
    'posts':po
    }
    return render(request,'posts/index.html',context)
                        
   
