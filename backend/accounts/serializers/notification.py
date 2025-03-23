from rest_framework import serializers

from accounts.models import notification_settings, notification

class notification_settings_serializers ( serializers.ModelSerializer ):
    class Meta:
        model = notification_settings
        fields = ( 'id', 'user', 'is_email_channel' )


class notification_serializers ( serializers.ModelSerializer ):
    class Meta:
        model = notification
        fields = ( 'id', 'user', 'title', 'message', 'date_of_issue', 'expires_at', 'is_show' )