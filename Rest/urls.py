"""Rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("student/", StudentCreateList.as_view()),
    # path("student/<str:name>/", StduentParticuler.as_view()),
    path("course/", CourseListCreate.as_view()),
    path("collage/", CollageList.as_view()),
    path("collage_create/", CollageCreate.as_view()),
    path("test/", Temp.as_view()),
    path("collage_rpdate/<int:pk>/", CollageUpdate.as_view()),
    ##hyper Link
    path("coursehyper/<int:pk>/", Course_hyper.as_view(), name="course_details"),
    path("studenthyper/<int:pk>/", Student_hyper.as_view(), name="student"),
    path("collagehyper/", Collage_hyper.as_view()),
    path(
        "collage_details/<int:pk>/", Collage_details.as_view(), name="collage_deatils"
    ),
    path("inst/", InstructorListView.as_view()),
    path("inst/<int:pk>/", InstructorDetailView.as_view(), name="instructor-detail"),
    path("cou/", Course_InstructorListView.as_view()),
    path("cou/<int:pk>/", Course_InstructorDetailView.as_view(), name="course-detail"),
    path("home/", home),
]
