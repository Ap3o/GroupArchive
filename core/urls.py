from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url('^$', views.main, name="main"),
    url('gallery/(?P<group_id>\d+)/', views.gallery_of_group, name='gallery'),
    url('gallery/delete-photo/', views.delete_photo, name="delete_photo"),
    url('auth/login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
        name="login"),
    url('^auth/logout/$', views.logout_user, name="logout"),
]
