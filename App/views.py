import random

from django.http import HttpResponse
from django.shortcuts import render

from App.models import Student


def add_student(request):
    student = Student()
    student.s_name = "小花%d" % random.randrange(100)
    student.save()
    data = {
        "student": student,
    }
    return render(request, "student.html",context=data)


def get_students(request):
    students = Student.objects.all()

    return render(request, 'get_students.html', {'students': students})