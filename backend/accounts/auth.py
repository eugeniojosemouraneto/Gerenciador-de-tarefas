from django.contrib.auth.hashers import check_password, make_password
from rest_framework.exceptions import AuthenticationFailed, APIException

from accounts.models import user

class authentication:

    def sigin ( self, email: str | None = None, password: str | None = None ) -> user | None:
        if not email:
            raise AuthenticationFailed('Email é obrigatórios.')
        
        if not password:
            raise AuthenticationFailed('Senha é obrigatórios.')
        
        user_instance: user | None = user.get_by_email(email)

        if not user_instance:
            raise AuthenticationFailed('Usuario não encontrado.')
        
        if not check_password( password, user_instance.password ):
            raise AuthenticationFailed('Senha incorreta.')

        return user_instance

    def sigup ( self, name: str | None, email: str | None = None, password: str | None = None ) -> user | None:
        if not name:
            raise AuthenticationFailed('Nome é obrigatórios.')
        
        if not email:
            raise AuthenticationFailed('Email é obrigatórios.')
        
        if not password:
            raise AuthenticationFailed('Senha é obrigatórios.')
        
        user_instance: user | None = user.get_by_email(email)

        if user_instance:
            raise AuthenticationFailed('Usuario já existe.')
        
        password_hashers: str = make_password( password )
        return user.created(name, email, password_hashers)