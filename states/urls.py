from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *  # Import your views

router = DefaultRouter()
# Register views for state list and full state details
router.register('states', StateLimitedAPIView, basename='state-limited')  # Viewset for limited state data
router.register('cities', CitiesAPIView, basename='cities-limited')  # Viewset for limited state data
router.register('allCities', CitiesAllAPIView ,basename='all-cities')

router.register('statesdetails', StateFullAPIView, basename='state-full')  # Viewset for full state data
router.register('localitites' , LocalitiesAPIView , basename='localities-full')

urlpatterns = [
    
    path('allCities/', include(router.urls)),
    path('statesdetails/', include(router.urls)),
    path(r'states', include(router.urls)),
    path('state/', include(router.urls)),  # Include all the URLs generated by the router
    path('cities/', include(router.urls)),  # Include all the URLs generated by the router
    
]
