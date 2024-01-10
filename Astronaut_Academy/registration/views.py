from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return render(request,'Home.html')


def career(request):
    return render(request,'Career.html')

def curriculum(request):
    return render(request,'Curriculum.html')

def student(request):
    return render(request,'Student_registration.html')

def trainer(request):
    return render(request,'Trainer_registration.html')