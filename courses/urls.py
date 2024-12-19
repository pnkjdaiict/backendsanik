from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'sub-categories', SubCategoryListView, basename='sub-categoreis')
router.register(r'courses', CourseListAPIView, basename='course')
router.register(r'sub-courses', SubCourseListAPIView, basename='subcourse')
router.register(r'courses-seo-data', CourseSeoDataViewSet, basename='seocoursedata')
router.register('cities-with-courses', CitiesWithCoursesView, basename='cities-with-courses'),
urlpatterns = [
    path('', include(router.urls)),
]
