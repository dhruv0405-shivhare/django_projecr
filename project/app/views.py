from django.shortcuts import render
from .models import Student
from .models import Login
from .models import Query


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
        if email=="dshivhare661@gmail.com" and password=='12345':
            return render(request,'dashboard.html')
        else:
            data=Login.objects.filter(admin_email=email)
            if(data):
                user=Login.objects.get(admin_email=email)
                print(user)
                mypass=user.admin_email
                if(mypass==password):
                    return render(request,'dashboard.html')
                else:        
                    return render (request,'login.html')
    else:
        return render (request,'login.html')
    
def student_list(request):
    students = Student.objects.all()

    return render(request, 'student_list.html', {'data': students})
    
def student_login(request):
        if request.method=='POST':
            email=request.POST.get('email')
            password=request.POST.get('password')
            user=Student.objects.filter(stu_email=email)
            if user:
                data=Student.objects.get(stu_email=email)
                user_data={
                    'enrollment':data.stu_enrollment,
                    'name':data.stu_name,
                    'email':data.stu_email,
                    'contact':data.stu_contact,
                    'address':data.stu_address,
                    'password':data.stu_password
                }
                print(user_data)
                pass1=data.stu_password
                if pass1==password:
                    return render(request,'student_dashboard.html')
                else:
                    msg="Enter password not match"
                    return render(request,'student_login.html',{'msg':msg})
            else:
                msg = "Email does not Exit"
                return render(request,'student_login.html',{'msg':msg})
        else:
             return render(request,'student_login.html')
    
def student_dashboard(request):
    if request.method=='POST':
       name=request.POST.get('name')
       enrollment=request.POST.get('enrollment')
       email=request.POST.get('email')
       contact=request.POST.get('contact')
       query=request.POST.get('query')
       Query.objects.create(name=name,enrollment=enrollment,email=email,contact=contact,query=query)
       query=Query.objects.all()
    return render(request,'query_list.html',{'data3':query})  

def query_list(request):
    query = Query.objects.all()

    return render(request, 'query_list.html', {'data3': query})  

def logout(request):
    
    return render(request,'index.html')



def delete1(request,pk1):
    data3 = Query.objects.get(id=pk1)
    data3.delete()
    query = Query.objects.all()
    return render(request, 'student_dashboard.html',{'data3':query})

def edit1(request,pk1):
    data3= Query.objects.get(id=pk1)
    query=Query.objects.all()
    return render(request, 'student_dashboard.html',{'data3':query,'data3':data3})

def updatedat1(request,pk1):
    if request.method=="POST":
        x = Query.objects.get(id=pk1)
        p = request.POST.get('name')
        q = request.POST.get('email')
        r = request.POST.get('city')
        s = request.POST.get('contact')
        x.stu_city = r
        x.stu_contact = s
        x.stu_email = q
        x.stu_name = p
        x.save()
        query=Query.objects.all()
        return render(request, 'student_dashboard.html',{'data3':query})

       