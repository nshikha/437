from django import forms

from sio.models import *

class StudentForm(forms.Form):
    andrew_id = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)


    # Customizes form validation for the username field.
    def clean_andrew_id(self):
        # Confirms that the username is not already present in the
        # User model database.
        andrew_id = self.cleaned_data.get('andrew_id')
        if Student.objects.filter(andrew_id__exact=andrew_id):
            raise forms.ValidationError("A student with Andrew ID %s already exists", andrew_id)

        # Generally return the cleaned data we got from the cleaned_data
        # dictionary
        return andrew_id


class CourseForm(forms.Form):
    course_number = forms.IntegerField()
    course_name = forms.CharField(max_length = 200)
    instructor = forms.CharField(max_length = 200)

    def clean_course_number(self):
        course_number = self.cleaned_data.get('course_number')
        if (Course.objects.filter(course_number__exact=course_number)):
            raise forms.ValidationError("Course %d already exists.", course_number)

        return course_number

class RegisterForm(forms.Form):
    andrew_id = forms.CharField(max_length=20)
    course_number = forms.IntegerField()

    def clean_course_number(self):
        course_number = self.cleaned_data.get('course_number')
        if (not Course.objects.filter(course_number__exact=course_number)):
            raise forms.ValidationError("Course %s does not exist", course_number)

        return course_number

    def clean_andrew_id(self):
        # Confirms that the username is not already present in the
        # User model database.
        andrew_id = self.cleaned_data.get('andrew_id')
        if (not Student.objects.filter(andrew_id__exact=andrew_id)):
            raise forms.ValidationError("andrew ID %s does not exist", andrew_id)

        # Generally return the cleaned data we got from the cleaned_data
        # dictionary
        return andrew_id


