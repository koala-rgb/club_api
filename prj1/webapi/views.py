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

        try:
            club = Club.objects.get(pk=club_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialize = ClubInstanceSerializer(club)

        return Response(serialize.data)

    def put(self, request, club_id):

        try:
            club = Club.objects.get(pk=club_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serialize = ClubInstanceSerializer(instance = club, data=data, partial=True)

        if(serialize.is_valid(raise_exception=True)):
            club = serialize.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, club_id):

        try:
            club = Club.objects.get(pk=club_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        club.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MemberView(APIView):

    def get(self, request, club_id):

        try:
            members = Member.objects.filter(club = club_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

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

        try:
            member = Member.objects.get(pk=member_id)
            interest = Interest.objects.filter(member=member)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialize_member = MemberInstanceSerializer(instance=member)

        return Response(serialize_member.data)

    def put(self, request, club_id, member_id):

        try:
            member = Member.objects.get(pk=member_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serialize = MemberInstanceSerializer(instance = member, data=data, partial=True)

        if(serialize.is_valid(raise_exception=True)):
            member = serialize.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, club_id, member_id):

        try:
            member = Member.objects.get(pk=member_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        member.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class InterestView(APIView):

    def get(self, request, club_id, member_id):

        try:
            interest = Interest.objects.filter(member = member_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialize = InterestSerializer(interest, many=True)

        return Response(serialize.data)

    def post(self, request, club_id, member_id):

        interest = request.data

        try:
            interest['member'] = member_id
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialize = InterestSerializer(data=interest)

        if serialize.is_valid(raise_exception=True):
            save = serialize.save()
            try:
                member = Member.objects.get(pk=member_id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_201_CREATED)

class InterestInstanceView(APIView):

    def get(self, request, club_id, member_id, interest_id):

        try:
            interest = Interest.objects.get(pk=interest_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            interest.member = Member.objects.get(pk=member_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialize = InterestInstanceSerializer(interest)

        return Response(serialize.data)

    def delete(self, request, club_id, member_id, interest_id):

        try:
            interest = Interest.objects.get(pk=interest_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        interest.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)