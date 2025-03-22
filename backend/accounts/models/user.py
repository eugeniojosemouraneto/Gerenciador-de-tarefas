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

    def __str__(self):
        return self.email