from django.db import models

from accounts.models import user

class category_task ( models.Model ):
    name = models.CharField( max_length = 200 )
    user = models.ForeignKey( user, on_delete = models.CASCADE )

    class Meta:
        indexes = [
            models.Index( fields = [ 'user' ]),
        ]

    def __str__(self) -> str:
        return self.name