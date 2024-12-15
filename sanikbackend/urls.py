from django.contrib import admin
from django.urls import path ,include

from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [

    path('admin/', admin.site.urls) , 
    path('', include('homepage.urls')),  # Include the homepage app's URLs
    path('' , include('states.urls')), 
    path('' , include ('courses.urls')),
    path('' , include('blogs.urls')) ,
    # path('' , include('news.urls')) ,
    path('' , include('blogsdata.urls')),
    path('' , include('newsdata.urls'))



] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
