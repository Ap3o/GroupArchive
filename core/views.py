from django.shortcuts import render
from . import models


# Create your views here.
def main(request):
    gallery = models.Gallery.objects.all()
    return render(request, "main.html", {"gallery": gallery})
