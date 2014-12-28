from django.shortcuts import render

students = set([])
courses = {}

# Create your views here.
def listing(request):
	courseName = request.POST.get('course')
	student = request.POST.get('student')
	if (courseName and student):
		courses[courseName].add(student)
	elif (courseName):
		courses[courseName] = set([])
	elif (student):
		students.add(student)
	else:
		pass
	return render(request, 'index.html', {'students': students, 'courses': courses})





