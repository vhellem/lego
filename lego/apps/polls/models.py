from django.conf import settings
from django.db import models

from lego.apps.content.models import Content
from lego.apps.polls.permissions import PollPermissionHandler
from lego.utils.models import BasisModel

from django.utils import timezone

class Poll(BasisModel, Content):

    valid_until = models.DateTimeField(default=(timezone.now()) + timezone.timedelta(weeks=52))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'{settings.FRONTEND_URL}/polls/{self.id}/'

    class Meta:
        permission_handler = PollPermissionHandler()

class Option(BasisModel):

    name = models.CharField(max_length=255)
    votes =  models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.name

