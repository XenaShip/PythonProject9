from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lessons.models import Lesson, Course


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lessons = SerializerMethodField()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lesson = LessonSerializer()

    def get_lessons_count(self, lesson):
        return Lesson.objects.filter.count(course=lesson.course)

    class Meta:
        model = Course
        fields = ('name', 'description', 'lessons_count')

