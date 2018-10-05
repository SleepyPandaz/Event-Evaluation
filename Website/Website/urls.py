from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('poll/', include('poll.urls')),
    path('Groups/', include('Groups.urls')),
    path('Events/', include('Events.urls')),
    #path('Events_Statistics/', include('Events_Statistics.urls')),
    path('Student/', include('Student.urls')),
    path('admin/', admin.site.urls),
]