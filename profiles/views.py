from django.shortcuts import render
from profiles.forms import ProfileForm
from django.shortcuts import redirect
# Create your views here.
def add_profile(request):
    if request.method=="POST":
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_profile') 
    
    else :
        form=ProfileForm()
    return render(request,'add_profile.html',{'form':form})       
    