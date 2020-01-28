from django.urls import path

from .views import ClubView, ClubInstanceView, MemberView

urlpatterns = [
    path('clubs', ClubView.as_view()),
    path('clubs/<int:pk>', ClubInstanceView.as_view()),
    path('clubs/<int:pk>/members', MemberView.as_view())
]