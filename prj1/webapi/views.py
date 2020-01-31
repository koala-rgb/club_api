from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory

from .serializers import ClubSerializer, ClubInstanceSerializer, MemberSerializer, MemberInstanceSerializer, InterestSerializer
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

        return Response({"Operation Successful": f"Member '{save.first} {save.last}' has been added"})

class MemberInstanceView(APIView):

    def get(self, request, pk, pk2):

        member = Member.objects.filter(id = pk2)
        serialize = MemberInstanceSerializer(member, many=True)

        return Response(serialize.data)

    def put(self, request, pk, pk2):

        member = Member.objects.get(pk=pk2)
        data = request.data.get('member')
        serialize = MemberInstanceSerializer(instance = member, data=data, partial=True)

        if(serialize.is_valid(raise_exception=True)):
            member = serialize.save()

        return Response({"Operation Successful": f"Member '{member.first} {member.last}' has been updated"})

    def delete(self, request, pk, pk2):

        member = Member.objects.get(pk=pk2)
        member_name = member.first + " " + member.last
        member.delete()

        return Response({"Operation Successful": f"Member '{member_name}' has been deleted"})

class InterestView(APIView):

    def get(self, request, pk, pk2):

        interest = Interest.objects.filter(member = Member.objects.get(pk=pk2))
        serialize = InterestSerializer(interest, many=True)

        return Response(serialize.data)

    def post(self, request, pk, pk2):

        interest = request.data.get('interest')
        interest['member'] = pk2

        serialize = InterestSerializer(data=interest)

        if serialize.is_valid(raise_exception=True):
            save = serialize.save()
            member = Member.objects.get(pk=pk2)

        return Response({"Operation Successful": f"{save.name} has been added to '{member.first} {member.last}'s interests"})