from django.urls import path
from .views import BookAPIView

urlpattern = [
    path('', BookAPIView.as_view()),
]