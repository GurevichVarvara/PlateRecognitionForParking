from django.shortcuts import render


def load_plate(request):
    if request.method == 'POST' and request.FILES['plate']:
        print('ya')

    return render(request,
                  'plates_detection/load_plate.html')
