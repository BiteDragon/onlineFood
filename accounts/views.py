from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages
# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #create the user using form
            # password = form.cleaned_data['password']
            # user = form.save(commit = False)
            # user.role = User.CUSTOMER
            # user.set_password(password)
            # user.save()
            
            #create the user using create user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(first_name = first_name,last_name = last_name,email=email,username=username,password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Your account has been registered successfully")
            print("user is created")
            
            return redirect('registerUser')
        else:
            print("invalid form")
            print(form.errors)
    else :
        
         form = UserForm()
    context = {
        'form':form,
    }
    # return HttpResponse('this is a user registration form')
    return render(request, 'accounts/registerUser.html',context)
