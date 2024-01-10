
from django.shortcuts import render, redirect
from .forms import StudentForm, TeacherForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'Home.html')

def career(request):
    return render(request, 'Career.html')

def curriculum(request):
    return render(request, 'Curriculum.html')

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other desired page
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'Student_registration.html', {'form': form})

def trainer(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the home page after a successful form submission
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, 'Trainer_registration.html', {'form': form})
