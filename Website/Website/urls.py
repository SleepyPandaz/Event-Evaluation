from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('poll/', include('poll.urls')),
    path('Groups/', include('Groups.urls')),
    path('admin/', admin.site.urls),
]