from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404

from lessons.models import Lesson, Course, Subscription
from lessons.paginators import CustomPagination
from lessons.serializer import CourseSerializer, LessonSerializer, CourseDetailSerializer, SubscriptionSerializer
from users.permissions import IsOwner, IsModerator


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModerator,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner | ~IsModerator,)
        return super().get_permissions()


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModerator & IsOwner)


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModerator & IsOwner)


class SubscriptionAPIView(APIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)
        if subs_item.exists():
            subs_item.delete()
            message = 'Вы отписались'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Вы подписались'
        return Response({"message": message})


class SubscriptionListAPIView(ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
