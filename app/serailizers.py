from asyncore import read
from .models import *
from rest_framework import serializers


class CollageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    course = serializers.CharField(max_length=20)
    full = serializers.SerializerMethodField()

    class Meta:
        model = Collage
        fields = ["id", "name", "collage_name", "collage_city", "course", "full"]

    def validate_name(self, name):
        try:
            name = Student.objects.get(name=name)
            return name
        except Student.DoesNotExist:
            raise serializers.ValidationError(
                {"name": "name does not exits in student class"}
            )

    def validate_course(self, course):
        try:
            course = Course.objects.get(course_name=course)
            return course
        except Course.DoesNotExist:
            raise serializers.ValidationError(
                {"course": "course does not exists in course model"}
            )

    def get_full(self, obj):
        return f"{obj.name} {obj.course}"

    def create(self, validated_data):
        n = self.validate_name(validated_data["name"])
        c = self.validate_course(validated_data["course"])
        crea = Collage.objects.create(
            name=n,
            collage_name=validated_data["collage_name"],
            collage_city=validated_data["collage_city"],
            course=c,
        )
        crea.save()
        return crea


# -------------------------------


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CollageSerializer1(serializers.ModelSerializer):
    name = StudentSerializer()
    course = CourseSerializer()
    city = serializers.SerializerMethodField()

    class Meta:
        model = Collage
        fields = ["id", "name", "collage_name", "collage_city", "course", "city"]

    def get_city(self, obj):
        abc = Student.objects.get(id=obj.name_id)
        return abc.city


class CollageSerializer2(serializers.ModelSerializer):
    # course=serializers.PrimaryKeyRelatedField(many=True,queryset=Course.objects.all())
    student_city = serializers.ReadOnlyField(source="name.city")

    class Meta:
        model = Collage
        fields = ["id", "name", "student_city", "collage_name", "collage_city"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["name"] = Student.objects.get(pk=instance.name_id).name
        data["course"] = Course.objects.get(pk=instance.course_id).course_name
        return data


class CollageHyperSerializer(serializers.HyperlinkedModelSerializer):
    course = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="course_details"
    )
    name = serializers.HyperlinkedRelatedField(read_only=True, view_name="student")
    url = serializers.HyperlinkedIdentityField(
        read_only=True, view_name="collage_deatils"
    )

    class Meta:
        model = Collage
        fields = ["url", "id", "name", "course", "collage_name", "collage_city"]


class Course_InstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course_Instructor
        fields = ["title", "rating", "instructor"]


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    courses_inst = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="course-detail"
    )

    class Meta:
        model = Instructor
        fields = "__all__"
