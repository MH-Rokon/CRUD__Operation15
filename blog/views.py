from django.shortcuts import render
from posts.models import Post


def home(request):
    return render(request,'base.html')

def index(request):
    data=Post.objects.all()
    return render(request,'index.html',{'data':data})