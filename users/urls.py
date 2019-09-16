from django.urls import path
from . import views
from django.urls import include, path

app_name = 'users'

urlpatterns = [
path('event-finder/', include('eventFinderApp.urls')),
path('register/', views.Register.as_view(), name='register'),

]