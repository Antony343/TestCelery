from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('verify/<slug:uuid>/', verify, name='verify'),
    path('home/', TemplateView.as_view(template_name='main/home.html'), name='home'),

]
