from django.shortcuts import render


def load_plate(request):
    return render(request,
                  'plates_detection/load_plate.html')
