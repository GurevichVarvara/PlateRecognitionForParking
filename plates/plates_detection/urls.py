from django.urls import path, include
from plates_detection import views

urlpatterns = [
    path('load_plate', views.load_plate, name='load_plate'),
    path('list_of_plates', views.list_of_plates, name='list_of_plates'),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]