from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'sub-categories', SubCategoryListView, basename='sub-categoreis')
router.register(r'courses', CourseListAPIView, basename='course') 
router.register(r'single-courses', SingleCourseListAPIView, basename='singlecourse') 
router.register(r'header-courses', CourseHeaderslugAPIView, basename='headercourse') 



router.register(r'homepage-courses', HomepageCourseListAPIView, basename='homepagecourse')
router.register(r'homepage-feature-courses', HomepageFeatureCourseListAPIView, basename='homepagefeaturecourse')


router.register(r'sub-courses', SubCourseListAPIView, basename='subcourse')
router.register(r'courses-seo-data', CourseSeoDataViewSet, basename='seocoursedata')
router.register('cities-with-courses', CitiesWithCoursesView, basename='cities-with-courses'),
router.register(r'states-with-courses', StatesWithCoursesView, basename='states-with-courses'),
router.register(r'courses-slug' ,CourseslugAPIView , basename ='courses-slug')
urlpatterns = [
    path('', include(router.urls)),
]
