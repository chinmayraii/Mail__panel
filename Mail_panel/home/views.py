from django.shortcuts import render
from . models import Emp, Admin
from django.contrib import messages
from admin_views.admin import AdminViews



def index(request):
    return render (request,'index.html')

def emp(request):
    return render (request,'emp.html')

def admins(request):
    return render (request,'admin.html') 

def details(request):
    data=AdminViews.objects.all()
    return render (request,'details.html',{'data':data}) 

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

def admin_panel(request):
    t=Admin()
    tid=request.POST['emp_details']
    t.emp_details=Emp.objects.get(id=tid)
    t.response=request.POST['response']
    t.save()
    data=Emp.objects.all()
    ad=Admin.objects.all()
    messages.info(request,'added')
    return render(request,'details.html',{'data':data,'ad':ad})
                   

