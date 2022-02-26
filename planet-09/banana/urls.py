from django.urls import path
from banana import views

urlpatterns = [
    path('', views.banana_landing, name='banana_landing')
]
