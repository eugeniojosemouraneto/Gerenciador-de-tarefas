from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from accounts.auth import authentication
from accounts.models import user
from accounts.serializers import user_serializers

class signin ( APIView ):

    def post ( self, request ):
        email = request.data.get( 'email' )
        password = request.data.get( 'password' )
        user_instance: user = authentication.sigin( email = email, password = password ) 
        token = RefreshToken.for_user( user_instance )
        return Response({
            "user"        : user_serializers( user_instance ).data,
            "refresh"     : str(token.refresh),
            "acess_token" : str(token.access_token)
        })
