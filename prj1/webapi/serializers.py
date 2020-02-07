from rest_framework import serializers

from .models import Club, Member, Interest

class ClubSerializer(serializers.ModelSerializer):
    def create(self, data):
        return Club.objects.create(**data)

    class Meta:
        model = Club
        fields = ('id', 'name', 'email')

class ClubInstanceSerializer(serializers.ModelSerializer):

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.email = data.get('email', instance.email)

        instance.save()
        return instance

    class Meta:
        model = Club
        fields = ('id', 'name', 'email')

class MemberSerializer(serializers.ModelSerializer):

    def create(self, data):
        return Member.objects.create(**data)

    class Meta:
        model = Member
        fields = ('id', 'first', 'last', 'email', 'club')

class InterestSerializer(serializers.ModelSerializer):

    def create(self, data):
        return Interest.objects.create(**data)

    class Meta:
        model = Interest
        fields = ('id', 'member', 'name')

class MemberInstanceSerializer(serializers.ModelSerializer):
    interest = InterestSerializer(many=True, read_only=True)

    def update(self, instance, data):
        instance.first = data.get('first', instance.first)
        instance.last = data.get('last', instance.last)
        instance.email = data.get('email', instance.email)

        instance.save()
        return instance

    class Meta:
        model = Member
        fields = ('id', 'first', 'last', 'email', 'club', 'interest')

class InterestInstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = ('id', 'member', 'name')