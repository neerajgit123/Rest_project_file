from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .serailizers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

class StudentCreateList(APIView):
    def get(self, request):
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)


class StduentParticuler(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = "name"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


from rest_framework.generics import ListCreateAPIView


class CourseListCreate(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


from rest_framework.generics import CreateAPIView


class CollageList(APIView):
    def get(self, request):
        data = Collage.objects.all()

        serializer = CollageSerializer1(data, many=True)
        return Response(serializer.data)


class CollageCreate(CreateAPIView):

    queryset = Collage.objects.all()
    serializer_class = CollageSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def post(self,request):
    #     serializer=CollageSerializer1(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


from rest_framework.generics import ListCreateAPIView



class Page(PageNumberPagination):
    page_size=1

class Temp(ListCreateAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer2
    pagination_class = Page


from rest_framework.generics import UpdateAPIView


class CollageUpdate(UpdateAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer


from rest_framework.generics import RetrieveAPIView


class Course_hyper(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Student_hyper(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Collage_details(RetrieveAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer1


class Collage_hyper(ListCreateAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageHyperSerializer


from rest_framework import generics


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class Course_InstructorListView(generics.ListCreateAPIView):
    serializer_class = Course_InstructorSerializer
    queryset = Course_Instructor.objects.all()


class Course_InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Course_InstructorSerializer
    queryset = Course_Instructor.objects.all()


from django.core.paginator import Paginator


def home(request):
    collage = Collage.objects.all().order_by("id")
    paginator = Paginator(collage, 2, orphans=2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # print('paginator',paginator)
    # print('page_number',page_number)
    # print('page_obj',page_obj)
    context = {"page_obj": page_obj}
    return render(request, "app\home.html", context)

