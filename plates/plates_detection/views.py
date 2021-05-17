from django.shortcuts import render
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
                  'plates_detection/load_plate.html',
                  {'errors': errors,
                   'form': ImageForm()})
