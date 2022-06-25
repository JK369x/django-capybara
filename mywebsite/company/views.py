from django.shortcuts import render
# ใช้สำหรับการ show 
from django.http import HttpResponse 
from .models import *
#line
from songline import Sendline
from django.contrib.auth import authenticate, login
# send email
from .email_system import sendthai


def Home(request):
    allproduct = Product.objects.all() #SELECT * from product
    context = {'allproduct':allproduct}
    return render(request, 'company/home.html',context) #render html ให้หน่อย

def Service(request):
    return render(request, 'company/service.html')

def Contact(request):
    #แจ้ง user เมื่อกรอกข้อมูลไปแล้ว
    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        #copy ค่่าจาก POST แล้วจากตัวแปร data เรียกใช้ data.get เพื่อดึงตัวแปรมาเก็บไว้ใช้งานอย่างอื่นต่อ
        print(type(data))
        print(title)
        print(email)
        print(detail)
        print('=====================')
        # บันทึกลง backend 
        # Contact(title=title,emial=email,detail=detail).save() สามารถเขียนแบบนี้ก็ได้
        
        if title == '' and email == '':
            context['message'] = 'title is not null , email is not null'
            return render(request, 'company/contact.html',context)

        newrecord = ContactUs() #สร้างตัวแปรมาเรียกใช้ class จาก models
        newrecord.title = title 
        newrecord.email = email
        newrecord.description = detail
        context['message'] = 'We have received your message.'
        newrecord.save() #save ลง data base
        # แจ้ง email ตอบกลับ
        text = 'ฟหกฟหกฟหกฟหกฟหกฟหก'
        sendthai(email,'JK | Capybara',text)
        
        # send line 
       #token = 'mrcSQGfma7FIM5Fdgpj2SwtXL8HaU8TB6IxywFroNNZ'
        #m = Sendline(token)
        #m.sendtext('title:{}\nemail{}\n >>>{}'.format(title,email,detail))
    return render(request, 'company/contact.html',context)

def Login(request):
    #หน้า login
    #from django.contrib.auth import authenticate, login
    #ไป setting ด้วย
   
    context = {}
    
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')
        
        
        try:
            user = authenticate(username=username, password=password)
            login(request, user)
        except:
            context['message'] = 'username or password missing'
    return render(request, 'company/login.html',context)

def Account(request):
    accounting = ContactUs.objects.all()
    Acc_contact = {'accounting':accounting}
    return render(request, 'company/accounting.html',Acc_contact)


def Register(request):
    #หน้า login
    #from django.contrib.auth import authenticate, login
    #ไป setting ด้วย
   
    context = {}
    
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        password2 = data.get('password2')
        
        if password != password2:
            context['check_password'] = 'check password'
            return render(request, 'company/register.html',context)
        
        try:
            check_User = User.objects.get(username=username)
            context['fail_message'] = 'fail register!!'
        except:
            newuser = User()
            newuser.username = username
            newuser.email = username
            newuser.first_name = first_name
            newuser.last_name = last_name
            newuser.set_password(password)
            newuser.save()
            
            newprofile = Profile()
            newprofile.user = User.objects.get(username=username)
            newprofile.save()
            context['message'] = 'success register!!'
            text = 'ไอกันหน้าหี'
            sendthai(username,'JK | Capybara',text)
                     
        try:
            user = authenticate(username=username, password=password) #get user ล่าสุด
            login(request, user)
        except:
            context['message'] = 'username or password missing'
    return render(request, 'company/register.html',context)