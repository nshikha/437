from django.db import models

class Student(models.Model):
    andrew_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    def __unicode__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, 
                               self.andrew_id)

class Course(models.Model):
    course_number = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    students = models.ManyToManyField(Student)
    def __unicode__(self):
        return "%s: %s" % (self.course_number, self.course_name)
