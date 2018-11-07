from rest_framework.fields import CharField

from lego.apps.comments.serializers import CommentSerializer
from lego.apps.polls.models import Poll
from lego.apps.tags.serializers import TagSerializerMixin
from lego.utils.serializers import BasisModelSerializer

class PollSerializer(TagSerializerMixin, BasisModelSerializer):

    comments = CommentSerializer(read_only=True, many=True)
    comment_target = CharField(read_only=True)

    class Meta:
        model = Poll
        fields = (
            'id', 'created_at', 'title', 'description', 'tags', 'comments', 'comment_target'
        )
