from rest_framework.viewsets import ModelViewSet
from project.models import News
from project.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()  # pylint: disable=E1101
    serializer_class = NewsSerializer
