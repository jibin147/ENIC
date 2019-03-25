from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Ereg, Login, Freg, jobs, news


def index(request):
    return render(request, 'index.html')


def loginform(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def fregister(request):
    return render(request, 'fregister.html')


def jobs(request):
    return render(request, 'job.html')


def admin(request):
    return render(request, 'admin.html')


def message(request):
    return render(request, "message.html")


def state(request):
    return render(request, 'state.html')


def add(request):
    if request.method == 'POST':
        fname = request.POST.get('FirstName')
        lname = request.POST.get('LastName')
        address = request.POST.get('Address')
        gender = request.POST.get('Gender')
        dob = request.POST.get('DateofBirth')
        phno = request.POST.get('PhoneNumber')
        email = request.POST.get('email')
        Qualification = request.POST.get('Qualification')
        cname = request.POST.get('CompanyName')
        techid = request.POST.get('Technology')
        framework = request.POST.get('framework')
        cmpnyadd = request.POST.get('CompanyAddress')
        dist = request.POST.get('District')
        state = request.POST.get('State')
        password = request.POST.get('password')
        exp = request.POST.get('Experience')
        image = request.FILES['Image']
        obj1 = Login()
        obj1.uname = email
        obj1.password = password
        obj1.role = 'employee'
        obj1.status = 1
        obj1.save()
        obj = Ereg()
        obj.fname = fname
        obj.lname = lname
        obj.address = address
        obj.gender = gender
        obj.dob = dob
        obj.phno = phno
        obj.email = email
        obj.qualification = Qualification
        obj.cname = cname
        obj.techid = techid
        obj.framework = framework
        obj.cmpnyadd = cmpnyadd
        obj.dist = dist
        obj.state = state
        obj.password = password
        obj.exp = exp
        obj.image = image
        obj.lid = obj1
        obj.save()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')


def free(request):
    if request.method == 'POST':
        fname = request.POST.get('FirstName')
        lname = request.POST.get('LastName')
        address = request.POST.get('Address')
        gender = request.POST.get('Gender')
        dob = request.POST.get('DateofBirth')
        phno = request.POST.get('PhoneNumber')
        email = request.POST.get('email')
        Qualification = request.POST.get('Qualification')
        techid = request.POST.get('Technology')
        framework = request.POST.get('framework')
        dist = request.POST.get('District')
        state = request.POST.get('State')
        password = request.POST.get('password')
        image = request.FILES['Image']
        obj2 = Login()
        obj2.uname = email
        obj2.password = password
        obj2.role = 'freelancer'
        obj2.status = 1
        obj2.save()
        obj = Freg()
        obj.fname = fname
        obj.lname = lname
        obj.address = address
        obj.gender = gender
        obj.dob = dob
        obj.phno = phno
        obj.email = email
        obj.qualification = Qualification
        obj.techid = techid
        obj.framework = framework
        obj.dist = dist
        obj.state = state
        obj.password = password
        obj.image = image
        obj.lid = obj2
        obj.save()
        return render(request, 'login.html')
    else:
        return render(request, 'fregister.html')


def log(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        if (Login.objects.filter(uname=uname, password=password).exists()):
            logins = Login.objects.filter(uname=uname, password=password)
            for value in logins:
                user_id = value.id
                usertype = value.role
                userstatus = value.status
                if usertype == 'employee' and userstatus == 1:
                    role = request.session["role"] = 'employee'

                    return render(request, 'employee/employee.html', {'user': role, 'id': user_id})
                elif usertype == 'freelancer' and userstatus == 1:
                    role = request.session["role"] = 'freelancer'
                    return render(request, 'freelancer/freelancer.html', {'user': role, 'id': user_id})

                else:
                    context = {"error": "incorrect user name or password"}
                    return render(request, "login.html", context)
            else:
                template = loader.get_template("login.html")
                context = {"error": "incorrect information"}
                return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template("login.html")
            context = {}
            return HttpResponse(template.render(context, request))


def updates(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        company = request.POST.get('company')
        category = request.POST.get('category')
        department = request.POST.get('department')
        experience = request.POST.get('experience')
        technology = request.POST.get('technology')
        obj1 = jobs()
        obj1.name = name
        obj1.description = description
        obj1.company = company
        obj1.category = category
        obj1.department = department
        obj1.experience = experience
        obj1.technology = technology
        obj1.save()
        return render(request, 'job.html')
    else:
        return render(request, 'index.html')


def today(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        status = request.POST.get('status')
        obj = news()
        obj.title = title
        obj.description = description
        obj.date = date
        obj.status = status
        obj.save()
        return render(request, 'admin.html')
