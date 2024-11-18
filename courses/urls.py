from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'courses', CourseListAPIView, basename='course')
router.register(r'sub-courses', SubCourseListAPIView, basename='subcourse')
router.register('cities-with-courses', CitiesWithCoursesView, basename='cities-with-courses'),
urlpatterns = [
    path('', include(router.urls)),
]