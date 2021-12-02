from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url('^$', views.main, name="main"),
    url('delete-photo/', views.delete_photo, name="delete_photo"),
    url('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
        name="login"),
    url('^logout/$', views.logout_user, name="logout"),
]
