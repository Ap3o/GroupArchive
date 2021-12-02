from django.shortcuts import render, redirect
from django.contrib.auth import logout
from . import models


# Create your views here.
def main(request):
    gallery = models.Gallery.objects.all()
    return render(request, "main.html", {"gallery": gallery, "text": "Все фотографии, которые только есть на сайте"})


def delete_photo(request):
    pass


def logout_user(request):
    logout(request)
    return redirect("/")
