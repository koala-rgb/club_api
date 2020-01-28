from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory

from .serializers import ClubSerializer, ClubInstanceSerializer, MemberSerializer, InterestSerializer
from .models import Club, Member, Interest

import json

# Create your views here.

class ClubView(APIView):

    def get(self, request):

        clubs = Club.objects.all()
        serialize = ClubSerializer(clubs, many=True)
        return Response(serialize.data)

    def post(self, request):

        club = request.data.get('club')
        serialize = ClubSerializer(data=club)

        if serialize.is_valid(raise_exception=True):
            save = serialize.save()

        return Response({"Operation Successful": f"Club '{save.name}' has been added"})


class ClubInstanceView(APIView):

    def get(self, request, pk):

        club = Club.objects.get(pk=pk)
        serialize = ClubInstanceSerializer(club)

        return Response(serialize.data)

    def post(self, request, pk):
        return Response({"POST method is not allowed": "If you are attempting to add a new club, please navigate to the /clubs directory"})

    def put(self, request, pk):

        club = Club.objects.get(pk=pk)
        data = request.data.get('club')
        serialize = ClubInstanceSerializer(instance = club, data=data, partial=True)

        if(serialize.is_valid(raise_exception=True)):
            club = serialize.save()

        return Response({"Operation Successful": f"Club '{club.name}' has been updated"})

    def delete(self, request, pk):

        club = Club.objects.get(pk=pk)
        club_name = club.name
        club.delete()

        return Response({"Operation Successful": f"Club '{club_name}' has been deleted"})

class MemberView(APIView):

    def get(self, request, pk):

        members = Member.objects.filter(club = Club.objects.get(pk=pk))
        serialize = MemberSerializer(members, many=True)

        return Response(serialize.data)

    def post(self, request, pk):

        member = request.data.get('member')
        member['club'] = pk

        serialize = MemberSerializer(data=member)

        if serialize.is_valid(raise_exception=True):
            save = serialize.save()

        return Response({"Operation Successful": f"Member '{save.first}' has been added"})