from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    dob = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name


class Collage(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    collage_name = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")
    collage_city = models.CharField(max_length=20)

    def __str__(self):
        return self.name.name + "-" + self.course.course_name


class Instructor(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    input=models.TextField()
    def __str__(self):
        return self.name

class Course_Instructor(models.Model):
    title = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name="courses_inst"
    )
    def __str__(self):
        return self.title
