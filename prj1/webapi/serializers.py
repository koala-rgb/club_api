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
    member_id = serializers.PrimaryKeyRelatedField(source='member', read_only='true')

    class Meta:
        model = Interest
        fields = ('id', 'member_id', 'name')