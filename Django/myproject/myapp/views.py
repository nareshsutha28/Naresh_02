from django.shortcuts import render, redirect
from .models import Contact, Signup
import random
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    
    #     obj=Signup.objects.get(
    #             email=request.POST['email'],
    #             password=request.POST['password']
    # )
    if request.method=='POST':
        return render (request, "index.html")
    
    else:
        return render (request, "index.html")





def about1(request):
    return render (request, "about.html")

def login(request):
    if request.method=='POST':
        try:
            obj=Signup.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
            )
            request.session['email']=obj.email
            request.session['fname']=obj.fname
            request.session['lname']=obj.lname
            request.session['gender']=obj.gender
            request.session['mobile']=obj.mobile
            request.session['profile_pic']=obj.profile_pic.url
            

               
            return render (request, "header.html",{'obj':obj})
    
        except:
            msg='please enter valid email and password.'
            return render (request, "form.html",{'msg':msg})
    
    else:
        return render (request, "form.html")

            



def signup(request):
    if request.method=='POST':
        try:
            Signup.objects.get(email=request.POST['email'])
            msg="this mail id is already registered."
            return render (request, "signup.html", {'msg':msg})
        
        except:
                if request.POST['password']==request.POST['cpassword']:                
                    Signup.objects.create(
                        fname=request.POST['fname'],
                        lname=request.POST['lname'],
                        email=request.POST['email'],
                        gender=request.POST['gender'],
                        mobile=request.POST['mobile'],
                        password=request.POST['password'],
                        profile_pic=request.FILES['profile_pic']

                )
                    msg="signup form submited successfully"
                    return render (request, "form.html", {'msg':msg})
                else:
                    msg='The confirm password does not match'
                    return render (request, "signup.html", {'msg':msg})

    else:
        return render (request, "signup.html")

def contact(request):
    if request.method=='POST':
        Contact.objects.create(
            Fname=request.POST['fname'],
            Lname=request.POST['lname'],
            Email=request.POST['email'],
            Ramarks=request.POST['remarks']

        )
        contacts=Contact.objects.all().order_by('-id')[:3]

        msg="contact form submited successfully"
        return render (request, "contact.html", {'msg':msg,'contacts':contacts})
    else:
        contacts=Contact.objects.all().order_by('-id')[:3]

        return render (request, "contact.html", {'contacts':contacts})


def logout(request):
    
    del request.session['fname']
    del request.session['profile_pic']
    del request.session['lname']
    del request.session['gender']
    del request.session['mobile']
    del request.session['email']

    return render(request,"form.html")


def change_pas(request):
    if request.method=='POST':
        user=Signup.objects.get(email=request.session['email'])
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['new_cpassword']:
                user.password=request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                msg='confirm new password does not match.'
                return render(request, 'change_pas.html', {'msg':msg})
        else:
            msg='please enter valid password.'
            return render(request, 'change_pas.html', {'msg':msg})

    else:
        return render (request,'change_pas.html')



def profile(request):
    obj=Signup.objects.get(email=request.session['email'])
    if request.method == 'POST':
        obj.fname=request.POST['fname']
        obj.gender=request.POST['gender']
        obj.lname=request.POST['lname']
        obj.mobile=request.POST['mobile']
        try:
            obj.profile_pic=request.FILES['change_profile']
            
        except:
            pass
        obj.save()
        msg='updated susscessfully'

        request.session['profile_pic']=obj.profile_pic.url
        request.session['fname']=obj.fname
        request.session['lname']=obj.lname
        request.session['gender']=obj.gender
        request.session['mobile']=obj.mobile

        return render(request,'index.html', {'msg':msg})
    else:
        return render(request,'profile.html', {'obj':obj})
         
            
def forget_pas(request):
    if request.method=='POST':
        try:
            obj=Signup.objects.get(email=request.POST['email'])
            otp=random.randint(1000, 9999)
            subject = 'otp for forget password.'
            message = f'Hi {obj.fname}, your otp for forget is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [obj.email, ]
            send_mail( subject, message, email_from, recipient_list )

            return render (request, 'enter_otp.html', {'otp':otp,'email':obj.email})        

        except:
            msg='email id ypu enter is not registered.'
            return render (request, 'forget_pas.html', {'msg':msg})        

    else:
        return render (request, 'forget_pas.html')        



def enter_otp(request):
    email=request.POST['email']
    if request.method=='POST':
        if request.POST['otp']==request.POST['otp1']:
            return render(request, 'select_pas.html',{'email':email})
        else:
            msg='please enter valid otp.'
            return render(request, 'enter_otp.html', {'msg':msg})

    else:
        return render(request, 'enter_otp.html')

def new_pas(request):
    obj=Signup.objects.get(email=request.POST['email'])
    if request.method=='POST':
        if request.POST['npassword']==request.POST['c_npassword']:
            obj.password=request.POST['npassword']
            obj.save()
            msg='password updated succsefully.'
            return render(request, 'form.html',{'msg':msg})
        else:
            msg='Password and confirm password does not match.'
            return render(request, 'select_pas.html',{'msg':msg})
    else:
        return render(request, 'select_pas.html')



def send_again():
    obj=Signup.objects.get(email=request.POST['email'])
    otp=random.randint(1000, 9999)
    subject = 'otp for forget password.'
    message = f'Hi {obj.fname}, your otp for forget is {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [obj.email, ]
    send_mail( subject, message, email_from, recipient_list )
