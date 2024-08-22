from django.urls import path
from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig
from users.views import PayViewSet, UserListApiView, UserRetrieveApiView, UserCreateApiView, UserDestroyApiView, \
    UserUpdateApiView

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', PayViewSet)

urlpatterns = [
    path('user/', UserListApiView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveApiView.as_view(), name='user_retrieve'),
    path('user/create/', UserCreateApiView.as_view(), name='user_create'),
    path('user/<int:pk>/delete/', UserDestroyApiView.as_view(), name='user_delete'),
    path('user/<int:pk>/update/', UserUpdateApiView.as_view(), name='user_update'),

]

urlpatterns += router.urls
