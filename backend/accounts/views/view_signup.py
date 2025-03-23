from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from accounts.auth import authentication
from accounts.models import user
from accounts.serializers import user_serializers

class signup ( APIView ):

    def post ( self, request ):
        name = request.data.get( 'name' )
        email = request.data.get( 'email' )
        password = request.data.get( 'password' )
        user_instance: user = authentication.sigup( name = name, email = email, password = password )
        return Response({
            "user"        : user_serializers( user_instance ).data,
        })
