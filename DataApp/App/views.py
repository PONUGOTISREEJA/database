from django.shortcuts import render,HttpResponse,redirect
from .models import Student

# Create your views here.
def registration(request):
    if request.method == 'POST':
        uusername=request.POST['name']
        umail=request.POST['email']
        upassword=request.POST['password']
        uconfirmpassword=request.POST['confirmpassword']
        if upassword!=uconfirmpassword:
            return HttpResponse("Password and ConfirmPassword are not Matching")
        else:
            user_registration=Student(name =uusername,email=umail,password=upassword,confirmpassword=uconfirmpassword)
            user_registration.save()
            return redirect(login1)


    return render(request,"registration.html")

def login1(request):
    if request.method=='POST':
        uusername=request.POST["name"]
        upassword=request.POST["password"]
        std=Student.objects.all()
        for i in std:
            if i.name==uusername and i.password==upassword:
                return redirect(home)
        
        
        
    return render (request,'login.html')


def home(request):


    return render(request,"homepage.html")

def logout1(request):
    logout1(request)
    return redirect(login1)



