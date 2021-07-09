from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm
from django.http import  HttpResponse
from django.contrib.auth import  login,logout

def signupView(request):
    if request.method== 'POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return HttpResponse('user has been created!')
    
    else:      
        form=UserCreationForm()
        return render(request,'account/signup.html',{'form':form})

def loginView(request):
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            
            return redirect('/testappurl')

    form=AuthenticationForm()
    return render(request,'account/login.html',{'form':form})

def logoutView(request):
    if request.method=="POST":
        logout(request)
        return redirect('/testappurl')
    

    # else:

    #     form=AuthenticationForm()
    #     return render(request,'account/login.html',{'form':form})
            
    # else:
    #     form=UserCreationForm()
    #     return render(request,'account/login.html',{'form':form})



