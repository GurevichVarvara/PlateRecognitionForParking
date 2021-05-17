from django import forms
from plates_detection.models import Plate


class ImageForm(forms.ModelForm):

    class Meta:
        model = Plate
        fields = ('image',)
