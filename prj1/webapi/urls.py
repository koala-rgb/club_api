from django.urls import path

from .views import ClubView

urlpatterns = [
    path('clubs/', ClubView.as_view()),
    path('clubs/<int:pk>', ClubView.as_view())
]