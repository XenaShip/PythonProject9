from django.urls import path

from rest_framework.routers import SimpleRouter

from lessons.views import CourseViewSet, LessonListApiView, LessonUpdateApiView, LessonCreateApiView, \
    LessonDestroyApiView, LessonRetrieveApiView
from lessons.apps import LessonsConfig


app_name = LessonsConfig.name


router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path('lesson/', LessonListApiView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveApiView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/delete/', LessonDestroyApiView.as_view(), name='lesson_delete'),
    path('lesson/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lesson_update'),

]

urlpatterns += router.urls
