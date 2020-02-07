from django.urls import path

from .views import ClubView, ClubInstanceView, MemberView, MemberInstanceView, InterestView, InterestInstanceView

urlpatterns = [
    path('clubs', ClubView.as_view()),
    path('clubs/<int:club_id>', ClubInstanceView.as_view()),
    path('clubs/<int:club_id>/members', MemberView.as_view()),
    path('clubs/<int:club_id>/members/<int:member_id>', MemberInstanceView.as_view()),
    path('clubs/<int:club_id>/members/<int:member_id>/interests', InterestView.as_view()),
    path('clubs/<int:club_id>/members/<int:member_id>/interests/<int:interest_id>', InterestInstanceView.as_view())
]