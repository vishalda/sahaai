from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from volunteer.models import Volunteers
from django.db import connection
from event.models import Event
from django.contrib import messages
import os

#book=openpyxl.Workbook()
#sheet=book.active

# Create your views here.
cursor=connection.cursor()
@csrf_exempt
def create_volunteer(request):
    if(request.method=="POST"):
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        email_id=request.POST['email']
        phone_no=request.POST['phone']
        gender=request.POST['gender']
        if(password==confirm_password):
            event_id=Event.objects.get(pk=1)
            query='''INSERT INTO volunteer_volunteers (password,username,name,email_id,phone_no,gender,event_id_id,credit) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');'''.format(password,username,name,email_id,phone_no,gender,1,0)
            cursor.execute(query)
        else:
            messages.info(request,'Failed')
            return redirect('/')
        # query='''SELECT * FROM volunteer_volunteers;'''
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
        # book.save("Volunteer.ods")
        return redirect('/')

def enroll_volunteer(request,eid):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        query='''SELECT password FROM volunteer_volunteers WHERE username='{}';'''.format(username)
        cursor.execute(query)
        data=cursor.fetchall()
        print(data[0][0])
        if data[0][0]==password:
            query='''UPDATE volunteer_volunteers SET event_id_id={} WHERE username='{}';'''.format(eid,username)
            cursor.execute(query)
            # query='''SELECT * FROM volunteer_volunteers;'''
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
            # book.save("Volunteer.ods")
            return redirect('/')
        messages.info(request,"Failed")
        return redirect('/')

def user_list(request):
    #v_list=Volunteers.objects.raw('SELECT * FROM volunteer_volunteers')
    v_list=Volunteers.objects.all().order_by('id')
    data={'v_list':v_list}
    return render(request,'volunteer.html',data)

def assign_cred_points(request,eid,points):
    query='''UPDATE volunteer_volunteers SET credit=credit+{} WHERE event_id_id='{}';'''.format(points,eid)
    cursor.execute(query)
    # query='''SELECT * FROM volunteer_volunteers;'''
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
    # book.save("Volunteer.ods")
    return redirect('/')