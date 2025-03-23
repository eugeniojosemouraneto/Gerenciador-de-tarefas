from rest_framework import serializers

from accounts.models import user

class user_serializers ( serializers.ModelSerializer ):
    class Meta:
        model = user
        fields = ( 'id', 'name', 'email' )