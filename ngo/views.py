from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from event.models import Event
from .models import *
from django.http import JsonResponse
import os

#book=openpyxl.Workbook()
#sheet=book.active

cursor=connection.cursor()
# Create your views here.
@csrf_exempt
def index(request):
    ngos=Organization.objects.all()
    #ngos = Organization.objects.raw('select * from ngo_organization')
    data={'ngos':ngos}
    return render(request, 'index.html',data)

@csrf_exempt
def register_ngo(request):
    if request.method == "POST":
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        location=request.POST['location']
        phone=request.POST['phone']
        description=request.POST['description']
        links=request.POST['links']
        logo=request.FILES['logo']
        qrCode=request.FILES['qrcode']
        if password==confirm_password:
            #org=Organization.objects.raw('''SELECT * FROM ngo_organization WHERE username='{}';'''.format(username))
            #if(len(org)>0):
            if Organization.objects.filter(username=username).exists():
                return JsonResponse({'Login':'Username taken'})
                #print("Jai")
                #messages.info(request,'Username Taken')
                #return redirect('/register-ngo/')
            #orgi=Organization.objects.raw('''SELECT * FROM ngo_organization WHERE email='{}';'''.format(email))
            #if(len(orgi)>0):
            elif Organization.objects.filter(email=email).exists():
                return JsonResponse({'Login':'Email taken'})
                #messages.info(request,'Email Taken')
                #return redirect('/register-ngo/')
            else:
                #user=Organization.objects.raw('insert into ngo_organization (username,password,email,name,location,phone,description,links,logo) values ({},{},{},{},{},{},{},{},{})'.format(username,password,email,name,location,phone,description,links,logo))
                user=Organization.objects.create_user(username=username,password=password,email=email,name=name,location=location,phone=phone,description=description,links=links,logo=logo,qrCode=qrCode)
                user.save()
                messages.info(request,'Success')
                # query='''SELECT * FROM ngo_organization;'''
                # cursor.execute(query)
                # results=cursor.fetchall()
                # i=0
                # for row in results:
                #     i += 1
                #     j = 1
                #     for col in row:
                #         cell = sheet.cell(row = i, column = j)
                #         cell.value = col
                #         j += 1
                # book.save("NGO.ods")
                return redirect('/login-ngo/')
        else:
            messages.info(request,'Password does not match')
            print("Password no")
            return redirect('/register-ngo/')
    return render(request,'register_ngo.html')

def login_ngo(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=Organization.objects.raw('''SELECT * FROM ngo_organization WHERE username='{}';'''.format(username))
        #user=Organization.objects.get(username=username)
        print(user)
        if(user[0].check_password(password)):
            auth.login(request,user[0])
            print(user[0].is_authenticated)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            print("Wrong",username,password,user)
            return redirect('/login-ngo/')
    else:
        return render(request,"login_ngo.html")

def logout_ngo(request):
    auth.logout(request)
    return redirect('/')

def ngo_page(request,nid):
    org_data=Organization.objects.raw('''SELECT * FROM ngo_organization WHERE id='{}';'''.format(nid))
    eve_data=Event.objects.raw('''SELECT * FROM event_event WHERE ngo_id_id='{}';'''.format(nid))
    data={'org_data':org_data[0],'eve_data':eve_data}
    print(data)
    return render(request,"ngo.html",data)

def get_qrCode(request,nid):
    #qr_data=Organization.objects.raw('''SELECT * FROM ngo_organization WHERE id='{}';'''.format(nid))
    qr_data=Organization.objects.get(pk=nid)
    data={'data':qr_data}
    print(qr_data)
    return render(request,"donation.html",data)

def donateList(request):
    ngos=Organization.objects.all()
    #ngos = Organization.objects.raw('select * from ngo_organization')
    data={'ngos':ngos}
    return render(request, 'donate_list.html',data)