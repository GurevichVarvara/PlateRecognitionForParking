from django.shortcuts import render, redirect
from datetime import datetime

from plates_detection.forms import ImageForm
from plates_detection.models import Plate


def load_plate(request):
    errors = []

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            plate = form.save(commit=False)
            plate.name = '1239AB7'
            plate.date = datetime.now()
            plate.img_title = str(int(datetime.now().timestamp()))
            plate.save()

            return render(request,
                          'plates_detection/plate_result.html',
                          {'plate': plate,
                           'recognition_result': True})

    return render(request,
                  'plates_detection/load_plate.html',
                  {'errors': errors,
                   'form': ImageForm()})


def list_of_plates(request):
    return render(request,
                  'plates_detection/list.html',
                  {'plates': Plate.objects.all(),
                   'first_plate': Plate.objects.all().first()})
