from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter
from djoser.views import UserViewSet

from users.views import UserInfoViewSet

from api import views

app_name = 'api'


router = DefaultRouter()
# router.register(
#     r'nutrients',
#     views.NutrientsViewSet,
#     basename='Nutrients'
# )
router_api = SimpleRouter()
router_api.register(r'users', UserViewSet, basename='users')
router_api.register(r'users_info', UserInfoViewSet, basename='users_info')
router_api.register(
    r'workout_session', views.WorkoutSessionViewSet, basename='workout_session'
)
router_api.register(r'sleep-down', views.SleepDownViewSet,
                    basename='sleep-down')
router_api.register(r'sleep-up', views.SleepUpViewSet, basename='sleep-up')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_api.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('calories/<int:pk>/', views.СalorieСalculationView.as_view()),
    #  path('workout_session/<int:pk>/', views.WorkoutSessionView.as_view()),
    #  path('sleep/down/', views.SleepDownViewSet.as_view({'post': 'create'})
    # path('sleep/up/', views.SleepViewSet.as_view({'post': 'sleep_up'})),
    path('video/c/<int:category_id>/d/<str:difficulty>',
         views.TrainingVideoView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('difficulty/', views.DifficultyView.as_view()),
]
