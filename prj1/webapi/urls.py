from django.urls import path

from .views import ClubView, ClubInstanceView, MemberView, MemberInstanceView, InterestView

urlpatterns = [
    path('clubs', ClubView.as_view()),
    path('clubs/<int:pk>', ClubInstanceView.as_view()),
    path('clubs/<int:pk>/members', MemberView.as_view()),
    path('clubs/<int:pk>/members/<int:pk2>', MemberInstanceView.as_view()),
    path('clubs/<int:pk>/members/<int:pk2>/interests', InterestView.as_view())
]