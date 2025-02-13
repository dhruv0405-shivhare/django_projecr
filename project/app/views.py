from django.shortcuts import render
from .models import Student
from .models import Login
def index(request):
    return render(request,'index.html')

def dashboard(request):
    if request.method=='POST':
      enrollment=request.POST.get('enrollment')
      name=request.POST.get('name')
      Email=request.POST.get('email')
      contact=request.POST.get('contact')
      address=request.POST.get('address')
      password=request.POST.get('password')
      cpassword=request.POST.get('cpassword')
      user=Student.objects.filter(stu_email=Email).exists()
      if user:
         msg='Email Alreay Exit'
         students = Student.objects.all()
         return render(request,'dashboard.html',{'msg':msg, 'data': students})
      else:
         if password==cpassword:
             Student.objects.create(stu_enrollment=enrollment,stu_name=name,stu_email=Email,stu_contact=contact,stu_password=password,stu_address=address)
             msg='Registration Successfully !!!'
             students = Student.objects.all()
             return render(request,'dashboard.html',{'msg':msg, 'data': students})
         else:
             msg="Password and Confirm Password Not Match"
             students = Student.objects.all()
             return render(request,'dashboard.html',{'msg':msg, 'data': students,'name':name,'email':Email,'contact':contact})
    else:
         students = Student.objects.all()
         return render(request, 'dashboard.html', {'data': students})    
    
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

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=Login.objects.filter(admin_email=email)
        if user:
            data1=Login.objects.get(admin_email=email)
            user_data={
                'name':data1.admin_name,
                'email':data1.admin_email,
                'passowrd':data1.admin_password,

            }
            print(user_data)
            pass1= data1.admin_password
            if pass1 == password:
                return render(request,'dashboard.html',{'data':user_data})
            else:
                msg = "Enter Password not Match"
                return render(request,'login.html',{'msg':msg})
        else:
            msg = "Email not Exist"
            return render(request,'login.html',{'msg':msg})    
            
    else:
        return render(request,'login.html')
        



       