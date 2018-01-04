





from django.contrib.auth.models import User
from main.models import Student, HostelPS
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):

    for name, login, hostel, room, bitsId, bDay, phone, email, address, parentName, parentPhone, parentEmail, admit, gender, bloodGroup in profiles:
        rev_login = login[0:5] + '0' + login[5:]
        try:
            user = User.objects.get(username = rev_login)
            student = Student.objects.get(user=user)
            if hostel == 'Graduate' or hostel == 'Thesis' or hostel == 'PS2' or hostel == '':
                acadstudent = False
                status = 'Graduate' if hostel == '' else hostel
                psStation = room
                hostel = ''
                room = ''
            else:
                acadstudent = True
                status = 'Student'
                psStation = ''
            
            hostelps = HostelPS.objects.create(student=student, acadstudent=acadstudent, status=status, psStation=psStation, hostel=hostel, room=room)
            hostelps.save()
        except Exception as e:
            print(rev_login+ ' ' + str(e))
            continue

    return HttpResponse("Done")