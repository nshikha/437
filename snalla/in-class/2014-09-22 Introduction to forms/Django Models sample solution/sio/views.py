from django.shortcuts import render
from django.db import transaction

from models import *
from forms import *

def make_view(request, messages):
    context = {}
    context['studentForm'] = StudentForm()
    context['courseForm'] = CourseForm()
    context['registerForm'] = RegisterForm()
    context['courses'] = Course.objects.all()
    context['messages'] = messages
    return render(request, 'sio.html', context)

def home(request):

    return make_view(request, [])

@transaction.atomic
def create_student(request):
    form = StudentForm(request.POST)

    if not form.is_valid():
        return render(request, 'sio.html', context)

    new_student = Student(andrew_id=form.cleaned_data['andrew_id'],
                          first_name=form.cleaned_data['first_name'],
                          last_name=form.cleaned_data['last_name'])
    new_student.save()

    return make_view(request, ["Added %s" % new_student])

@transaction.atomic
def create_course(request):
    form = CourseForm(request.POST)

    if not form.is_valid():
        return render(request, 'sio.html', context)

    new_course = Course(course_number=form.cleaned_data['course_number'],
                        course_name=form.cleaned_data['course_name'],
                        instructor=form.cleaned_data['instructor'])
    new_course.save()

    return make_view(request, ["Added %s" % new_course])

@transaction.atomic
def register_student(request):
    form = RegisterForm(request.POST)

    if not form.is_valid():
        return render(request, 'sio.html', context)

    course = Course.objects.get(course_number=form.cleaned_data['course_number'])
    student = Student.objects.get(andrew_id=form.cleaned_data['andrew_id'])
    course.students.add(student)
    course.save()

    messages = []
    messages.append('Added %s to %s' % (student, course))
    return make_view(request, messages)
