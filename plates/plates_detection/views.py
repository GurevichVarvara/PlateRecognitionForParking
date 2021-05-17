from django.shortcuts import render


def load_plate(request):
    return render(request, 'base.html')
