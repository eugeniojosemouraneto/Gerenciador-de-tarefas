from django.db import models

from accounts.models import user
from task.models import category_task

class task( models.Model ):
    user = models.ForeignKey( user, on_delete = models.CASCADE )
    title = models.CharField( max_length = 175 )
    description = models.TextField()
    create_at = models.DateTimeField( auto_now_add = True )
    star_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField( default = False )
    category = models.ForeignKey( category_task, on_delete = models.CASCADE )

    class Meta:
        indexes = [
            models.Index( fields = [ 'user'] ),
            models.Index( fields = [ 'user', 'category'] ),
            models.Index( fields = [ 'star_date', 'end_date'] ),
            models.Index( fields = [ 'is_completed'] ),
        ]
