from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Student
from .form import StudentForm

def homepage(request):
    return HttpResponse("<h1> Home page </h1>")
def contactpage(request):
    return render(request,'contact.html')
def aboutpage(request):
    return render(request,'about.html')

# Create your views here.


def addStudent(request):
    if request.method == 'GET':
        context = {'form':StudentForm()}
        return render(request,'add.html',context)
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(addStudent)
        else:
            return render(request, 'add.html', {'form': form})
        
def displayStudent(request):
    dbdata = Student.objects.all()
    context = {'mydata':dbdata}
    return render(request,'display.html',context)
