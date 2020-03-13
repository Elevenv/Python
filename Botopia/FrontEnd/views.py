import random
from django.shortcuts import render,redirect
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .models import User_info
from .models import Bot_info
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

def Homepage(request):
    global count
    count = 0
    return render(request,'Homepage.html',{'count':count})

def Login(request):
    global login_email
    global count
    login_email = request.POST['login_email']
    login_password = request.POST['login_password']
    db_object = User_info.objects.filter(email = login_email)
    if db_object:
        if db_object[0].email == login_email and db_object[0].password == login_password:
            u_info = User_info()
            username = db_object[0].name
            count = 1
            message = "Logged in Succesfully."
            request.session['userEmail'] = login_email
            return render(request,"Startsearch.html",{'message':message,'username':username,'count':count})
            # return redirect('/show_add_bot/')
        else:
            message="Incorrect Creditionals"
            return render(request,"Login.html",{'message':message})            
    else:
        message="Account does not exists."
        return render(request,"Login.html",{'message':message})

def Signup_dup(request):
    return render(request,'Signup.html')

def Login_dup(request):
    return render(request,"Login.html")

def Signup(request):    
    global user_name
    global user_email
    global user_pass    
    
    user_name = request.POST['new_Name']
    user_pass = request.POST['new_Password']
    user_email = request.POST['new_Email']
    user_pass_confirm = request.POST['confirm_Password']

    db_object_email = User_info.objects.filter(email = user_email)
    db_object_username = User_info.objects.filter(name=user_name)
    if not db_object_email:
        if db_object_username:
            message = "Username is already Exist."
        elif len(user_pass) >= 8 :
            if user_pass == user_pass_confirm:
                global_send_otp(user_email)
                return render(request,"Verify.html")
            else:
                message = "Password and Confirm Password does not matches."
        else:
            message = "Minimum Password Length Should be 8."
    else:
        message = "EmailID already exist."
    return render(request,"Signup.html",{'message':message})

def Verify(request):
    user_otp = request.POST['signup_otp']
    global server_otp
    global user_name
    global user_email
    global user_pass
    
    u_info = User_info()
    user_otp_into_int = int(user_otp)
    if user_otp_into_int == server_otp:
        status = "Account Created Succesfully.Please Login."
        u_info.name = user_name
        u_info.email = user_email
        u_info.password = user_pass
        u_info.save()
        request.session['userEmail'] = user_email
    else:
        status = "Incorrect One Time Password.Please Register Again."
    return render(request,"Login.html",{'status':status})

def Startsearch(request):
    pass
    return render(request,"Startsearch.html")

def Resend_otp(request):
    global user_email
    global_send_otp(user_email)
    return render(request,"Verify.html")

def dup_Forget_pass(request):
    return render(request,"Forget_pass.html")

def Forget_pass(request):
    global for_user_email
    for_user_email = request.POST['for_user_email']
    db_object = User_info.objects.filter(email = for_user_email)
    if db_object:
        global_send_otp(for_user_email)
        message="OTP send succesfully."
        return render(request,"Forget_pass_verify.html",{'message':message})
    else:
        message = "Account does not exists."
        return render(request,"Forget_pass.html",{'message':message})

def Forget_pass_verify(request):

    global server_otp
   
    forget_pass_otp = request.POST['forget_pass_otp']
    forget_pass_otp_into_int = int(forget_pass_otp)
    if forget_pass_otp_into_int == server_otp:
        message = "Set new Password."
        return render(request,"New_password.html",{'message':message})
    else:
        message = "Incorrect OTP."
        return render(request,"Forget_pass_verify.html",{'message':message})

def global_send_otp(a_email):
    # off_email = 'discordbottravern@gmail.com'
    # off_password = 'discordbottravern@18VK'
    # send_to_email = a_email
    # subject = 'Discord Bot Travern Verification' 
    # global server_otp
    # server_otp = int(random.randint(100000,1000000))
    # otp_into_string = str(server_otp)
    # message = 'Your verification code is : '+otp_into_string
    # msg = MIMEMultipart()
    # msg['From'] = off_email
    # msg['To'] = send_to_email
    # msg['Subject'] = subject
    # msg.attach(MIMEText(message, 'plain'))
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.starttls()
    # server.login(off_email, off_password)
    # text = msg.as_string() 
    # server.sendmail(off_email, send_to_email, text)
    # server.quit()
    # # except Exception as e:
    # #     message = "Please connect to Internet"
    # #     return redirect("Homepage.html",{'message':message})
    send_to_email = a_email
    subject = 'Discord Bot Travern Verification' 
    global server_otp
    server_otp = int(random.randint(100000,1000000))
    otp_into_string = str(server_otp)
    message = 'Your verification code is : '+otp_into_string
    send_mail(
        subject,
        message,
        'discordbottravern@gmail.com',
        [send_to_email],
        fail_silently=False,
    )

def New_password(request):

    global for_user_email

    new_pass = request.POST['new_pass']
    confirm_new_pass = request.POST['confirm_new_pass']
    
    if new_pass == confirm_new_pass:
        change_pass = User_info.objects.get(email=for_user_email)
        change_pass.password = new_pass
        change_pass.save()
        message ="Password changed succesfully."
        return render(request,"Login.html",{'message':message})
    else:
        message = "Password not matches with confirm password."
        return render(request,"New_password.html",{'message':message})

def Forget_pass_verify_resend(request):
    global for_user_email
    global_send_otp(for_user_email)
    return render(request,"Forget_pass_verify.html")

def Logout(request):
    global count
    count = 0
    del request.session['userEmail']
    return render(request,"Homepage.html")
    

def showAddBot(request):
    user_db = User_info.objects.get(email = request.session['userEmail'])
    username = user_db.name
    return render(request, 'Startsearch.html', {'username': username})

def AddBot(request):
    global login_email
    global count
    if count == 1:
        user_db = User_info.objects.get(email = request.session['userEmail'])
        # user_db = User_info.objects.filter(email = login_email)
        bot_db = Bot_info()
        bot_db.author = user_db
        bot_db.bot_name = request.POST['bot_name']
        bot_db.bot_id = request.POST['bot_id']
        # bot_db.bot_image = request.POST['bot_image']
        bot_db.bot_url = request.POST['bot_url']

        if request.method == 'POST' and request.FILES['bot_image']:
            myfile = request.FILES['bot_image']
            fs = FileSystemStorage()
            bot_db.bot_image = fs.save(myfile.name, myfile)
        bot_db.save()
        return render(request,"Homepage.html")
    else:
        message = "Please Login to Access this Page."
        return render(request,"Startsearch.html",{'message':message})

def ShowBot(request):
    global count
    if count == 1:
        user_db = User_info.objects.get(email = request.session['userEmail'])
        bot_db = Bot_info.objects.filter(author=user_db.id)
        
        # bot_name_list = []
        # bot_id_list = []
        # for i in range(0,len(bot_db)):
        #     bot_name_list.append(bot_db[i].bot_name)
        #     bot_id_list.append(bot_db[i].bot_id)

        return render(request,"Startsearch.html",{'c':bot_db})
    else:
        message = "Please Login to Access this Page."
        return render(request,"Startsearch.html",{'message':message})
def Change_password(request):
    # user_db = User_info.objects.get(email = request.session['userEmail'])
    global count 
    if count ==1 :

        new_pass = request.POST['new_pass']
        confirm_new_pass = request.POST['confrim_new_pass']
        if len(new_pass)>=8 and len(confirm_new_pass)>=8:
            if new_pass == confirm_new_pass:
                change_pass = User_info.objects.get(email = request.session['userEmail'])
                change_pass.password = new_pass
                change_pass.save()
                message ="Password changed succesfully."
                # return render(request,"userProfile.html",{'message':message})
                return redirect('/userProfile/',{'message':message})
            else:
                message = "Password not matches with confirm password."
                return render(request,"Change_password.html",{'message':message})
        else:
            message = "Password length should > 8"
            return render(request,"Change_password.html",{'message':message})
    else:
        message = "Please Login to Access this Page."
        return render(request,"Startsearch.html",{'message':message})

def dup_Change_password(request):
    global count 
    if count==1:
        return render(request,"Change_password.html")
    else:
        message = "Please Login to Access this Page"
        return render(request,"Startsearch.html",{'message':message})

def userProfile(request):
    user_data = User_info.objects.get(email = request.session['userEmail'])
    bot_data = Bot_info.objects.filter(author=user_data.id)
    return render(request,"userProfile.html",{'user_data':user_data,'bot_data':bot_data})
    # return redirect('/show_add_bot/')