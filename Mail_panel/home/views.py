from django.shortcuts import render
from . models import Emp, Admin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required





def index(request):
    return render (request,'index.html')

def emp(request):
    return render (request,'emp.html')

@login_required
def admins(request):
    data=Emp.objects.all()
    ad=Admin.objects.all()
    return render (request,'admin.html',{'data':data,'ad':ad}) 

def details(request):
    data=Emp.objects.all()
    ad=Admin.objects.all()
    return render (request,'details.html',{'data':data,'ad':ad}) 

    

def add_mail(request):
    to=request.POST['to']
    name=request.POST['name']
    subject=request.POST['subject']
    description=request.POST['description']
    from_emp=request.POST['from_emp']

    if Emp.objects.filter(from_emp=from_emp).exists():
        messages.info(request,'Email already exists')
        return render(request,'emp.html') 
    else:
        Emp.objects.create(to=to, name=name,subject=subject,description=description,from_emp=from_emp)
        messages.success(request,'!!!!Successfully Added!!!!')
        return render(request,'emp.html') 

@login_required
def admin_panel(request):
    t=Admin()
    tid=request.POST['emp_details']
    t.emp_details=Emp.objects.get(id=tid)
    t.response=request.POST['response']
    t.save()
    data=Emp.objects.all()
    ad=Admin.objects.all()
    messages.info(request,'Response Submitted')
    return render(request,'details.html',{'data':data,'ad':ad})

 

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=name).exists():
            messages.info(request,"Username already exists")
            return render(request,'register.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return render(request,'register.html')   
        else:
            user=User.objects.create_user(username=name,email=email,password=password)
            user.save()
            messages.success(request,"Successfully Registered")
            return render(request,'login.html')
    else:
        return render(request,'register.html') 

def alogin(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully !!')
            return render(request,'index.html') 
        else:
            messages.error(request," Invalid Username or Password")
            return render(request, ("login.html"))
    else:
        return render(request, ("login.html"))

def lgout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout ')
    return render(request,'index.html')                       
                   

