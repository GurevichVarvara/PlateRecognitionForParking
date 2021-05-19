from django.urls import path
from plates_detection import views

urlpatterns = [
    path('load_plate', views.load_plate, name='load_plate'),
    path('list_of_plates', views.list_of_plates, name='list_of_plates'),
    path('stat', views.stat, name='stat'),
]