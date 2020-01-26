from rest_framework import serializers

from .models import Club, Member, Interest

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, data):
        return Club.objects.create(**data)

    class Meta:
        model = Club
        fields = ('id', 'name', 'email')

class ClubInstanceSerializer(serializers.HyperlinkedModelSerializer):

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.email = data.get('email', instance.email)

        instance.save()
        return instance

    class Meta:
        model = Club
        fields = ('id', 'name', 'email')

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    club_id = serializers.PrimaryKeyRelatedField(source='club', read_only='true')

    class Meta:
        model = Member
        fields = ('id', 'first', 'last', 'email', 'club_id')

class InterestSerializer(serializers.HyperlinkedModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source='member', read_only='true')

    class Meta:
        model = Interest
        fields = ('id', 'member_id', 'name')