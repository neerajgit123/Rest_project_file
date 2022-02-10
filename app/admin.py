import imp
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "father_name", "city", "dob"]


@admin.register(Collage)
class CollageAdmin(admin.ModelAdmin):
    list_display = ["name", "collage_name", "collage_city", "course"]


admin.site.register(Course)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]


@admin.register(Course_Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ["title", "rating", "instructor"]
