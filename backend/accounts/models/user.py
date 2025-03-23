from django.db import models

from django.contrib.auth.models import AbstractBaseUser

class user( AbstractBaseUser ):
    name = models.CharField( max_length = 150 )
    email = models.EmailField( unique = True )
    
    USERNAME_FIELD = 'email'

    class Meta:
        indexes = [
            models.Index( fields = [ 'id' ]),
            models.Index( fields = [ 'email' ]),
            models.Index( fields = [ 'id', 'email' ]),
        ]

    @classmethod
    def get_by_email(cls, email: str):
        try:
            return cls.objects.get( email = email )
        except cls.DoesNotExist:
            return None
        
    @classmethod
    def created(cls, name: str, email: str, password: str):
        return cls.objects.create( name = name, email = email, password = password )
    
    def __str__(self):
        return self.email
    
