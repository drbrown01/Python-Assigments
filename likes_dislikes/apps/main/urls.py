from django.conf.urls import url
from django.contrib import admin
from . import views
import bcrypt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^users$', views.createUser),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^posts', views.createPost),

]
