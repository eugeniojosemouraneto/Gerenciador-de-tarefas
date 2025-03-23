from django.urls import path

from accounts.views import *


urlpatterns = [
    path( 'signin', signin.as_view() ),
    path( 'signup', signup.as_view() ),
]
