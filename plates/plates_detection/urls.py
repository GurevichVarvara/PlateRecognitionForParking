from django.urls import path
from plates_detection import views

urlpatterns = [
    path('load_plate', views.load_plate, name='load_plate'),
]