from random import choice

from rest_framework import viewsets

from lego.apps.permissions.api.views import AllowedPermissionsMixin
from lego.apps.polls.models import Poll
from lego.apps.polls.serializers import PollSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class =  PollSerializer
