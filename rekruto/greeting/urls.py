from django.urls import re_path

from .views import greeting


urlpatterns = [
    re_path(r'^$', greeting, name='greeting')
]


