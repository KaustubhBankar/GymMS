from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from GymSystem import urls
from . models import *
from django.contrib import messages




# Create your views here.

def About(request):
    return render(request,'about.html')

# def Contact(request):
#     return render(request,'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    enquiry=Enquiry.objects.all()
    plan=Plan.objects.all()
    equipment=Equipment.objects.all()
    member=Member.objects.all()
    e1 = 0
    p1 = 0
    eq1 = 0
    m1 = 0
    for i in enquiry:
        e1+=1
    for i in plan:
        p1+=1
    for i in equipment:
        eq1+=1
    for i in member:
        m1+=1
    d = {'e1':e1,'p1':p1,'eq1':eq1,'m1':m1}


    return render(request,'index.html',d)

def Login(request):
    error = ""
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pwd')
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                return render(request,'index.html')
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}

    return render(request,'login.html',d)


def Logout_admin(request):
    
    # if not request.user.is_staff:
        # return redirect('login')
    logout(request)
    return redirect('login')

def Add_Enquiry(request):
    error = ""
    
    if not request.user.is_staff:
        return redirect('login')
    # enq = Enquiry.objects.all()
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            enq = Enquiry(name=n,contact=c,emailid=e,age=a,gender=g)
            enq.save()
            error = "no"
        except Exception as e:
            print(f'------------------{e}')
            error = "yes"


    d = {'error':error}

    return render(request,'add_enquiry.html',d)

def View_Enquiry(request):
    
    if not request.user.is_staff:
        return redirect('login')
    enq = Enquiry.objects.all()
    

    d = {'enq':enq}

    return render(request,'view_enquiry.html',d)

def Delete_Enquiry(request,pid):
    
    if not request.user.is_staff:
        return redirect('login')
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')


def Add_Equipment(request):
    error = ""
    
    if not request.user.is_staff:
        return redirect('login')
    # enq = Enquiry.objects.all()
    if request.method=="POST":
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        de = request.POST['description']
        try:
            enq = Equipment(name=n,price=p,unit=u,date=d,description=de)
            enq.save()
            error = "no"
        except Exception as e:
            print(f'------------------{e}')
            error = "yes"


    d = {'error':error}

    return render(request,'add_equipment.html',d)

def View_Equipment(request):
    
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.all()
    

    d = {'equipment':equipment}

    return render(request,'view_equipment.html', d)

def Delete_Equipment(request,pid):
    
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')

def Add_Plan(request):
    error = ""
    
    if not request.user.is_staff:
        return redirect('login')
    # enq = Enquiry.objects.all()
    if request.method=="POST":
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        # d = request.POST['date']
        # de = request.POST['description']
        try:
            enq = Plan(name=n,amount=a,duration=d)
            enq.save()
            error = "no"
        except Exception as e:
            print(f'------------------{e}')
            error = "yes"


    d = {'error':error}

    return render(request,'add_plan.html',d)

def View_Plan(request):
    
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.all()
    

    d = {'plan':plan}

    return render(request,'view_plan.html', d)

def Delete_Plan(request,pid):
    
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')


def Add_Member(request):
    error = ""
    
    if not request.user.is_staff:
        return redirect('login')
    plan1 = Plan.objects.all()
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        p = request.POST['plan']
        g = request.POST['gender']
        j = request.POST['joindate']
        ex = request.POST['expiredate']
        i = request.POST['initialamount']
       
        plan=Plan.objects.filter(name=p).first()
        try:
            enq = Member(name=n,contact=c,emailid=e,age=a,plan=plan,gender=g,joindate=j,expiredate=ex,initialamount=i)
            enq.save()
            error = "no"
        except Exception as e:
            print(f'------------------{e}')
            error = "yes"


    d = {'error':error,'plan':plan1}

    return render(request,'add_member.html',d)

def View_Member(request):
    
    if not request.user.is_staff:
        return redirect('login')
    member = Member.objects.all()
    

    d = {'member':member}

    return render(request,'view_member.html', d)

def Delete_Member(request,pid):
    
    if not request.user.is_staff:
        return redirect('login')
    Member = Member.objects.get(id=pid)
    member.delete()

    return redirect('view_member')






def ContactUs(request):

    if request.method == "POST":
        try:
            name = request.POST['name']
            emailid = request.POST['emailid']
            contact = request.POST['contact']
            subject = request.POST['subject']
            message = request.POST['message']
            cnt = Contact(
                name = name,
                emailid = emailid,
                contact = contact,
                subject = subject,
                message = message
            )
            cnt.save()
            messages.success(request,"Submitted Successfully")
            return render(request,'contact.html')
        except Exception as e:
            messages.error(request,"Failed to submit")
            return render(request,'contact.html')
    else:
        return render(request,'contact.html')


def Edit_Enquiry(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect(admin_login)
    user = request.user
    enquiry = Enquiry.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        e1 = request.POST['email']
        a1 = request.POST['age']
        g1 = request.POST['gender']

        enquiry.name = n1
        enquiry.mobile = m1
        enquiry.email = e1
        enquiry.age = a1
        enquiry.gender = g1
        try:
            enquiry.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_Enquiry.html', locals())


def Edit_Plan(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect(admin_login)
    user = request.user
    plan = Plan.objects.get(id=pid)
    if request.method == "POST":
        p1 = request.POST['name']
        a1 = request.POST['amount']
        d1 = request.POST['duration']

        plan.name = p1
        plan.amount = a1
        plan.duration = d1
        try:
            plan.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_Plan.html', locals())

def Edit_Equipment(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect(admin_login)
    user = request.user
    equipment = Equipment.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        p1 = request.POST['price']
        u1 = request.POST['unit']
        d1 = request.POST['description']

        equipment.name = n1
        equipment.price = p1
        equipment.unit = u1
        equipment.description = d1
        try:
            equipment.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_Equipment.html', locals())

def Edit_Member(request,pid):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    error = ""
    user = request.user
    member = Member.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        c1 = request.POST['contact']
        e1 = request.POST['email']
        g1 = request.POST['gender']
        i1 = request.POST['initamount']

        member.name = n1
        member.contact = c1
        member.email = e1
        member.gender = g1
        member.initamount = i1
        try:
            member.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_Member.html', locals())


