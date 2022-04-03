from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm,SingupForm
# Create your views here.
def sing_up(request):
    form = SingupForm()
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
        return redirect('login')


    return render(request,'sing_up.html',{"form":form})
    
def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("logged in")
    return render(request, 'login.html', context={'form':form})

@login_required
def user_profile(request):  
    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Created Successfully!!!")
            form = ProfileForm(instance=profile)

    return render(request,'change_profile.html',{'form':form})


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"Logged Out!!!")
    return HttpResponse("logged Out!!")
