from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from . import models


def get_groups():
    # Получаем все значения из базы данных в таблице Group
    return models.Group.objects.all()


@require_http_methods(["GET"])
def main(request):
    gallery = models.Gallery.objects.all()
    return render(request, "gallery.html",
                  {"title": "Общая галлерея", "gallery": gallery,
                   "text": "Все фотографии, которые только есть на сайте", "groups": get_groups()})


@require_http_methods(["POST"])
def delete_photo(request):
    if request.is_ajax() and request.user.is_superuser:
        models.Gallery.objects.get(id=request.POST.get("id")).delete()
        return JsonResponse({"text": "Фотография удалена! Нужно обновить страницу."})


@require_http_methods(["GET"])
def gallery_of_group(request, group_id):
    gallery = models.Gallery.objects.filter(group_id=group_id)
    group = models.Group.objects.get(id=group_id)
    return render(request, "gallery.html",
                  {"gallery": gallery, "groups": get_groups(), "title": "Галерея группы " + group.name,
                   "text": group.description})


@require_http_methods(["GET"])
def logout_user(request):
    logout(request)
    return redirect("/")
