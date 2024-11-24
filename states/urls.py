from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *  # Import your views

router = DefaultRouter()
# Register views for state list and full state details
router.register('states', StateLimitedAPIView, basename='state-limited')  # Viewset for limited state data
router.register('statesdetails', StateFullAPIView, basename='state-full')  # Viewset for full state data
router.register('localitites' , LocalitiesAPIView , basename='localities-full')

urlpatterns = [
    path('state/', include(router.urls)),  # Include all the URLs generated by the router
    
]
