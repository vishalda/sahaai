from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages
from event.models import Event
from ngo.models import Organization
import os

#book=openpyxl.Workbook()
#sheet=book.active

cursor=connection.cursor()
# Create your views here.
def create_event(request,nid):
    if nid!=request.user.id or request.method!="POST":
        messages.info(request,'You are not authorized to create an event')
        return redirect('/')
    location=request.POST['location']
    venue=request.POST['venue']
    name=request.POST['name']
    description=request.POST['description']
    ngo=Organization.objects.get(pk=nid)
    cred_points=int(request.POST['cred_points'])
    events = Event.objects.create(location=location,venue=venue,ngo_id=ngo,name=name,description=description,cred_points=cred_points)
    events.save()
    # query='''SELECT * FROM event_event;'''
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
    # book.save("Event.ods")
    return redirect('/ngo/{}'.format(nid))

def event_details(request,eid):
    eve_data=Event.objects.raw('''SELECT * FROM event_event WHERE id={};'''.format(eid))
    data={'eve_data':eve_data[0]}
    return render(request,'event_detail.html',data)