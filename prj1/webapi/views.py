from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory

from .serializers import ClubSerializer, ClubInstanceSerializer, MemberSerializer, MemberInstanceSerializer, InterestSerializer, InterestInstanceSerializer
from .models import Club, Member, Interest

import json

# Create your views here.

class ClubView(APIView):

    def get(self, request):

        clubs = Club.objects.all()
        serialize = ClubSerializer(clubs, many=True)
        return Response(serialize.data)

    def post(self, request):

        club = request.data
        serialize = ClubSerializer(data=club)

        if serialize.is_valid(raise_exception=True):
            save = serialize.save()

        return Response(status=status.HTTP_201_CREATED)


class ClubInstanceView(APIView):

    def get(self, request, club_id):

        club = Club.objects.get(pk=club_id)
        serialize = ClubInstanceSerializer(club)

        return Response(serialize.data)

    def put(self, request, club_id):

        club = Club.objects.get(pk=club_id)
        data = request.data
        serialize = ClubInstanceSerializer(instance = club, data=data, partial=True)

        if(serialize.is_valid(raise_exception=True)):
            club = serialize.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, club_id):

        club = Club.objects.get(pk=club_id)
        club_name = club.name
        club.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MemberView(APIView):

    def get(self, request, club_id):

        members = Member.objects.filter(club = club_id)
        serialize = MemberSerializer(members, many=True)

        return Response(serialize.data)

    def post(self, request, club_id):

        member = request.data
        member['club'] = club_id

        serialize = MemberSerializer(data=member)

        if serialize.is_valid(raise_exception=True):
            save = serialize.save()

        return Response(status=status.HTTP_201_CREATED)

class MemberInstanceView(APIView):

    def get(self, request, club_id, member_id):

        member = Member.objects.get(id = member_id)

        interest = Interest.objects.filter(member)

        serialize_member = MemberInstanceSerializer(member)
        serialize_interest = InterestSerializer(interest, many=True)

        serialized_m = {'member': serialize_member.data}
        serialized_i = {'interests': serialize_interest.data}

        sergroup = serialized_m, serialized_i

        return Response(sergroup)

    def put(self, request, club_id, member_id):

        member = Member.objects.get(pk=member_id)
        data = request.data
        serialize = MemberInstanceSerializer(instance = member, data=data, partial=True)

        if(serialize.is_valid(raise_exception=True)):
            member = serialize.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, club_id, member_id):

        member = Member.objects.get(pk=member_id)
        member_name = member.first + " " + member.last
        member.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class InterestView(APIView):

    def get(self, request, club_id, member_id):

        interest = Interest.objects.filter(member = Member.objects.get(pk=member_id))
        serialize = InterestSerializer(interest, many=True)

        return Response(serialize.data)

    def post(self, request, club_id, member_id):

        interest = request.data
        interest['member'] = member_id

        serialize = InterestSerializer(data=interest)

        if serialize.is_valid(raise_exception=True):
            save = serialize.save()
            member = Member.objects.get(pk=member_id)

        return Response(status=status.HTTP_201_CREATED)

class InterestInstanceView(APIView):

    def get(self, request, club_id, member_id, interest_id):

        interest = Interest.objects.get(pk=interest_id)
        interest.member = Member.objects.get(pk=member_id)
        serialize = InterestInstanceSerializer(interest)

        return Response(serialize.data)

    def delete(self, request, club_id, member_id, interest_id):

        interest = Interest.objects.get(pk=interest_id)
        interest_name = interest.name
        interest.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)