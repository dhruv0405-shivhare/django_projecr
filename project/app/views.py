from django.shortcuts import render
from .models import Student
from .models import Registration
def index(request):
    return render(request,'index.html')

def registration(request):
         if request.method=='POST':
             name=request.POST.get('name')
             email=request.POST.get('email')
             contact=request.POST.get('contact')
             password=request.POST.get('password')
             cpassword=request.POST.get('cpassword')
             user=Registration.objects.filter(email=email)
             if user:
                 msg='Email Alreay Exit'
                 return render(request,'registration.html',{'msg':msg})
             else:
                 if password==cpassword:
                     Registration.objects.create(name=name,email=email,contact=contact,password=password)
                     msg='Registration Successfully !!!'
                     return render(request,'login.html',{'msg':msg})
                 else:
                     msg="Password and Confirm Password Not Match"
                     return render(request,'registration.html',{'msg':msg,'name':name,'email':email,'contact':contact})
         else:
             return render(request,'registration.html')        

def login(request):
        if request.method=='POST':
             email=request.POST.get('email')
             password=request.POST.get('password')
             user=Registration.objects.filter(email=email)
             if user:
                  data=Registration.objects.get(email=email)
                  user_data={
                       'name':data.name,
                       'email':data.email,
                       'contact':data.contact,
                       'password':data.password,
                  }
                  print(user_data)
                  pass1=data.password
                  if pass1==password:
                       return render(request,'dashboard.html',{'data':user_data})
                  else:
                       msg = "Enter Password Does Not Match"
                       return render(request,'login.html',{'msg':msg})
             else:
                  msg="Email Not Exit"
                  return render(request,'registration.html',{'msg':msg})
        else:
             return render(request,'login.html')
        
def dashboard(request):
    stu = Student.objects.all()
    print(stu)
    return render(request, 'dashboard.html',{'data':stu.values(),'data2':"kuch nhi"})


def delete(request,pk):
    data = Student.objects.get(id=pk)
    data.delete()
    stu = Student.objects.all()
    return render(request, 'dashboard.html',{'data':stu})

def edit(request,pk):
    data= Student.objects.get(id=pk)
    stu=Student.objects.all()
    return render(request, 'dashboard.html',{'data':stu,'data1':data})

def updatedat(request,pk):
    if request.method=="POST":
        x = Student.objects.get(id=pk)
        p = request.POST.get('name')
        q = request.POST.get('email')
        r = request.POST.get('city')
        s = request.POST.get('contact')
        x.stu_city = r
        x.stu_contact = s
        x.stu_email = q
        x.stu_name = p
        x.save()
        stu=Student.objects.all()
        return render(request, 'dashboard.html',{'data':stu})       