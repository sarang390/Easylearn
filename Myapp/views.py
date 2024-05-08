from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Myapp.models import *


def login(request):
    return render(request,'logintemplate.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    var=Login.objects.filter(username=username,password=password)

    if var.exists():
        var2=Login.objects.get(username=username,password=password)
        request.session['lid']=var2.id
        if var2.type=='admin':
            return HttpResponse('''<script>window.location='/Myapp/homepage/'</script>''')

        elif var2.type=='user':
            return HttpResponse('''<script>window.location='/Myapp/userhome/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/Myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid');window.location='/Myapp/login/'</script>''')


def forgot(request):
    return render(request, 'forgotpswd.html')

def forgot_post(request):
    username=request.POST['textfield']
    if not Login.objects.filter(username=username).exists():
        return HttpResponse('''<script>alert('email does not exist');window.location='/Myapp/login/'</script>''')
    import smtplib
    import random
    new_pass = random.randint(00000000,99999999)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sarangshajikumar@gmail.com", "vapq zeyj jrxw rtmk")

    to = username
    subject = "Password Reset"
    body = "Your new password is " + str(new_pass)
    msg = f"Subject: {subject}\n\n\{body}"
    server.sendmail("sarangshajikumar@gmail.com", to, msg)
    server.quit()
    Login.objects.filter(username=username).update(password = new_pass)
    return HttpResponse('''<script>alert('changed');window.location='/Myapp/login/'</script>''')



def home(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    return render(request, 'Admin/adminhomeindex.html')

def homepage(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    return render(request,'Admin/Admin Homepage.html')

def admin_change_password(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    return render(request,'admin/Changepassword.html')

def admin_change_password_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    old=request.POST['textfield']
    new=request.POST['textfield2']
    confirm=request.POST['textfield3']

    var = Login.objects.filter(password=old)
    if var.exists():
        if new==confirm:
            var2=Login.objects.filter(password=old).update(password=confirm)
            return HttpResponse('''<script>alert('success');window.location='/Myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/Myapp/home/'</script>''')

    else:
        return HttpResponse('''<script>alert('not same');window.location='/Myapp/home/'</script>''')


def sent_reply(request,id):
    return render(request,'admin/Sent reply.html',{'id':id})

def sent_reply_post(request):
    id=request.POST['id']
    reply=request.POST['textarea']
    cobj=Complaint.objects.filter(pk=id).update(reply=reply,status='replied')
    return HttpResponse('''<script>alert('replied');window.location='/Myapp/viewcomplaints/'</script>''')

def view_reviews(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    var=Review.objects.all()
    return render(request,'admin/View app reviews.html',{'data':var})

def view_reviews_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    robj = Review.objects.filter(date__range=[from_date,to_date])
    return render(request, 'admin/View app reviews.html', {'data': robj})

def view_complaints(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    var=Complaint.objects.all()
    return render(request,'admin/View Complaints.html',{'data':var})

def view_complaints_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    cobj = Complaint.objects.filter(date__range=[from_date, to_date])
    return render(request,'admin/View Complaints.html',{'data':cobj})


def view_users(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    var=User.objects.all()
    return render(request,'admin/View Users.html',{'data':var})

def view_users_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    search=request.POST['textfield']
    uobj=User.objects.filter(username__icontains=search)
    return render(request,'admin/View Users.html',{'data':uobj})




# user

def user_change_password(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    return render(request,'User/Changepassword.html')

def user_change_password_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    old=request.POST['textfield']
    new=request.POST['textfield2']
    confirm=request.POST['textfield3']
    var = Login.objects.filter(password=old)
    if var.exists():
        if new == confirm:
            var2 = Login.objects.filter(password=old).update(password=confirm)
            return HttpResponse('''<script>alert('success');window.location='/Myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/Myapp/userchangepwd/'</script>''')

    else:
        return HttpResponse('''<script>alert('invalid current password');window.location='/Myapp/userchangepwd/'</script>''')

def edit_profile(request):
    uobj=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'User/Editprofile.html',{'data':uobj})

def edit_profile_post(request):
    username=request.POST['textfield']
    phone=request.POST['textfield2']
    email=request.POST['textfield3']
    gender=request.POST['RadioGroup1']
    uobj = User.objects.get(LOGIN=request.session['lid'])
    if 'fileField' in request.FILES:

        photo=request.FILES['fileField']
        fs = FileSystemStorage()
        import datetime
        date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs.save(date, photo)
        path = fs.url(date)
        uobj.photo = path
        uobj.save()

    uobj.username = username
    uobj.phone = phone
    uobj.gender = gender
    uobj.email = email
    uobj.save()
    return HttpResponse('''<script>alert('Profile updated');window.location='/Myapp/viewprofile/'</script>''')

def QnA_generation(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    return render(request,'User/QnA generation.html')

def QnA_generation_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    text=request.POST['textarea']

    from pipelines import pipeline

    # import nltk
    # nltk.download('punkt')


    ##transfromers==3.0.0

    ##nltk

    ##torch
    #
    qa = pipeline("question-generation")

    qapair = qa(text)

    print(qapair)

    return render(request, 'User/View QnA.html', {'data': qapair})

def Sent_review(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    return render(request,'User/Sentappreview.html')

def Sent_reviews_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    rating=request.POST['rate']
    review=request.POST['textfield']
    lid = request.session['lid']
    lobj = Login.objects.get(id=lid)
    uid = User.objects.get(LOGIN=lobj)
    robj = Review()
    robj.review = review
    robj.rating = rating
    import datetime
    date = datetime.datetime.now().date()
    robj.date = date
    robj.USER = uid
    robj.save()
    return HttpResponse('''<script>alert('Review sent');window.location='/Myapp/sentreview/'</script>''')

def Sent_complaint(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    return render(request,'User/Sentcomplaint.html')

def Sent_complaint_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    complaint=request.POST['textarea']
    lid=request.session['lid']
    lobj=Login.objects.get(id=lid)
    uid=User.objects.get(LOGIN=lobj)
    cobj=Complaint()
    cobj.complaint=complaint
    import datetime
    date=datetime.datetime.now().date()
    cobj.date=date
    cobj.reply='pending'
    cobj.status='pending'
    cobj.USER=uid
    cobj.save()
    return HttpResponse('''<script>alert('Complaint sent');window.location='/Myapp/sentcomplaint/'</script>''')

def Signup(request):
    return render(request,'signuptemplate.html')

def Signup_post(request):
    username=request.POST['textfield']
    phone=request.POST['textfield2']
    email=request.POST['textfield3']
    gender=request.POST['RadioGroup1']
    photo=request.FILES['fileField']
    password=request.POST['textfield4']
    confirm_password=request.POST['textfield5']
    fs=FileSystemStorage()
    import datetime
    date=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
    fs.save(date,photo)
    path=fs.url(date)
    if not Login.objects.filter(username=email).exists():
        if password==confirm_password:
            lobj=Login()
            lobj.username=email
            lobj.password=password
            lobj.type='user'
            lobj.save()

            uobj=User()
            uobj.username=username
            uobj.phone=phone
            uobj.gender=gender
            uobj.email=email
            uobj.photo=path
            uobj.LOGIN=lobj
            uobj.save()
            return HttpResponse('''<script>alert('Successful');window.location='/Myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid password');window.location='/Myapp/signup/'</script>''')
    else:
        return HttpResponse('''<script>alert('Email Already exist');window.location='/Myapp/signup/'</script>''')


def View_QnA(request):
    return render(request,'User/View QnA.html')

def View_QnA_post(request):
    from pipelines import pipeline



    qa = pipeline("question-generation")

    qapair = qa("""  A shepherd boy in a village used to take his herd of sheep across the fields near the forest. He felt this job was very dull and wanted to have some fun. One day while grazing the sheep, he shouted, "Wolf! Wolf! The wolf is carrying away a lamb!" Farmers working in the nearby fields came running for help but didn’t find any wolf. The boy laughed and replied, "It was just fun. There is no wolf here".

    The boy played a similar trick repeatedly for many days. After some days, while the shepherd boy was in the field with the herd of sheep, suddenly, a wolf came out from the nearby forest and attacked one of the lambs. The boy was frightened and cried loudly, "Wolf! Wolf! The wolf is carrying a lamb away!" The farmers thought the boy was playing mischief again. So, no one paid attention to him and didn’t come to his help.  """)

    print(qapair)

    return HttpResponse('success')

def User_home(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    return render(request,'User/userhometemplate.html')

def View_profile(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    uobj=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'User/Viewprofile.html',{'data':uobj})

def View_reply(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    cobj=Complaint.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'User/Viewreply.html',{"data":cobj})

def View_reply_post(request):
    if request.session['lid']=='':
        return redirect('/Myapp/login/')
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    cobj=Complaint.objects.filter(date__range=[from_date,to_date])
    return render(request,'User/Viewreply.html',{"data":cobj})
def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>window.location='/Myapp/login/'</script>''')


