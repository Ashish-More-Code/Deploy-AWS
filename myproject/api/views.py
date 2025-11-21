from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

 
def hello_world(request):
   return render(request,'index.html')

def loginUser(request):
   if request.method=='POST':
      context={}
      userName=request.POST['username']
      userPassword=request.POST['password']
      user =authenticate(username=userName,password=userPassword)
      
      if user is not None:
         login(request,user)
         return redirect('/api/hello/')
      else:
         user_status=User.objects.filter(username=userName)
         if not user_status.first().is_active:
            context['err']="User is not Activated Contact admin!"
            return render(request,'login.html',context)
         else:
            context['err']="Invalid User Name and Password!"
            return render(request,'login.html',context)
   else:
      return render(request,'login.html')
   
def logoutUser(request):
   logout(request)
   return redirect('/')
