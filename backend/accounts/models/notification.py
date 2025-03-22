from django.db import models

from accounts.models import user

class notification_settings:
    user = models.ForeignKey( user, on_delete = models.CASCADE )
    is_email_channel = models.BooleanField( default = False )

    class Meta:
        indexes = [
            models.Index( fields = [ 'user' ]),
            models.Index( fields = [ 'is_email_channel' ]),
            models.Index( fields = [ 'user', 'is_email_channel' ]),
        ]

class notification:
    user = models.ForeignKey( user, on_delete = models.CASCADE )
    title = models.CharField( max_length = 125 )
    message = models.TextField()
    date_of_issue = models.DateTimeField( auto_now_add = True )
    expires_at = models.DateTimeField()
    is_show = models.BooleanField( default = False )

    class Meta:
        indexes = [
            models.Index( fields = [ 'user' ]),
            models.Index( fields = [ 'is_show' ]),
            models.Index( fields = [ 'date_of_issue' ]),
            models.Index( fields = [ 'user', 'is_show' ]),
            models.Index( fields = [ 'user', 'date_of_issue' ]),
            models.Index( fields = [ 'is_show', 'date_of_issue' ]),
            models.Index( fields = [ 'user', 'is_show', 'date_of_issue' ]),
        ]