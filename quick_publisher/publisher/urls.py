from django.urls import re_path

from .views import *

urlpatterns = [
    re_path(r'^(?P<slug>[a-zA-Z0-9\-]+)', view_post, name='view_post')
]