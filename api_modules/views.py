from django.shortcuts import render
from django.http import HttpResponse
from api_modules.index import index as index1
from api_modules.timetable import timetable as timetable1
from api_modules.attendance import attandence as attendance1
from api_modules.assignments import assignments as assignment1
from api_modules.curriculum import curriculum as curriculum1
from api_modules.exam_schedule import exam as exam1
from api_modules.marks import marks as marks1
from api_modules.grade_history import grade_history as grade_history1
from api_modules.grade_semwise import grade_semwise as grade_semwise1
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.
@csrf_exempt
def home(request):
    reg_no=request.POST["reg_no"]
    password=request.POST["password"]
    sem=request.POST["sem"]
    s=index1(reg_no,password,sem)
    x=timetable1(sem,s[1],s[0])
    return HttpResponse(json.dumps(x, sort_keys=True, indent=4), content_type="application/json")

@csrf_exempt
def attandence(request):
    reg_no=request.POST["reg_no"]
    password=request.POST["password"]
    sem=request.POST["sem"]
    s=index1(reg_no,password,sem)
    x=attendance1(sem,s[1],s[0])
    return HttpResponse(json.dumps(x, sort_keys=True, indent=4), content_type="application/json")

@csrf_exempt
def assignment(request):
    reg_no=request.POST["reg_no"]
    password=request.POST["password"]
    sem=request.POST["sem"]
    s=index1(reg_no,password,sem)
    x=assignment1(sem,s[1],s[0])
    return HttpResponse(json.dumps(x, sort_keys=True, indent=4), content_type="application/json")

@csrf_exempt
def curriculum(request):
    reg_no=request.POST["reg_no"]
    password=request.POST["password"]
    sem=request.POST["sem"]
    s=index1(reg_no,password,sem)
    x=curriculum1(sem,s[1],s[0])
    return HttpResponse(json.dumps(x, sort_keys=True, indent=4), content_type="application/json")

@csrf_exempt
def exam(request):
    reg_no=request.POST["reg_no"]
    password=request.POST["password"]
    sem=request.POST["sem"]
    s=index1(reg_no,password,sem)
    x=exam1(sem,s[1],s[0])
    return HttpResponse(json.dumps(x, sort_keys=True, indent=4), content_type="application/json")

@csrf_exempt
def grade_history(request):
    reg_no=request.POST["reg_no"]
    password=request.POST["password"]
    sem=request.POST["sem"]
    s=index1(reg_no,password,sem)
    x=grade_history1(sem,s[1],s[0])
    return HttpResponse(json.dumps(x, sort_keys=True, indent=4), content_type="application/json")

@csrf_exempt
def grade_semwise(request):
    reg_no=request.POST["reg_no"]
    password=request.POST["password"]
    sem=request.POST["sem"]
    s=index1(reg_no,password,sem)
    x=grade_semwise1(sem,s[1],s[0])
    return HttpResponse(json.dumps(x, sort_keys=True, indent=4), content_type="application/json")

@csrf_exempt
def marks(request):
    reg_no=request.POST["reg_no"]
    password=request.POST["password"]
    sem=request.POST["sem"]
    s=index1(reg_no,password,sem)
    x=marks1(sem,s[1],s[0])
    return HttpResponse(json.dumps(x, sort_keys=True, indent=4), content_type="application/json")
