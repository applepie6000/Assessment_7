from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def student(request):
    return render(request, 'student.html')
def teacher3(request):
    return render(request, 'teacher3.html')

