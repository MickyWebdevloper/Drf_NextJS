from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('', views.PostView.as_view()),
    path('detail/<slug:slug>', views.PostListAPIView.as_view(), name='detail')
]
