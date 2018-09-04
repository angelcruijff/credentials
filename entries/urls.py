from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
