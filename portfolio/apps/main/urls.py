from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='IndeX'),
    url(r'^index$', views.index),
    url(r'^testimonials$', views.testimonials),
    url(r'^test$', views.test),
]
