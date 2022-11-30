from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls', namespace='apis')),
    path('api/user/', include('authapi.urls', namespace='authapi'))
]
