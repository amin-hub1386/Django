from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Api import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('api/', include(router.urls)),
]
