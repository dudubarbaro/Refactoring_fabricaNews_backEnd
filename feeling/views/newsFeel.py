from rest_framework.viewsets import ModelViewSet

from feeling.models import NewsFeel
from feeling.serializers import NewsFeelSerializer


class NewsFeelViewSet(ModelViewSet):
    queryset = NewsFeel.objects.all()  # pylint: disable=E1101
    serializer_class = NewsFeelSerializer
