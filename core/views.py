from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from . import models


def get_groups():
    return models.Group.objects.all()


# Create your views here.
def main(request):
    gallery = models.Gallery.objects.all()
    return render(request, "gallery.html",
                  {"title": "Общая галлерея", "gallery": gallery,
                   "text": "Все фотографии, которые только есть на сайте", "groups": get_groups()})


def delete_photo(request):
    print(request.POST.get("id"))
    return JsonResponse({"text": "all good"})


def gallery_of_group(request, group_id):
    gallery = models.Gallery.objects.filter(group_id=group_id)
    return render(request, "gallery.html", {"gallery": gallery, "groups": get_groups()})


def logout_user(request):
    logout(request)
    return redirect("/")
