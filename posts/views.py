from django.shortcuts import render
from posts.forms import PostForm
from django.shortcuts import redirect
from posts.models import Post
def add_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_post')
    else :
        form=PostForm()
    return render(request,'add_post.html',{'form':form})        
        
def edit_post(request,id):
    post=Post.objects.get(pk=id)
    EditForm=PostForm(instance=post)
    if request.method=="POST":
        EditForm=PostForm(request.POST,instance=post)
        if EditForm.is_valid():
            EditForm.save()
            return redirect('index')  
             
    return render(request,'add_post.html',{'form':EditForm}) 
        

def delete_post(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect('index')              
               
