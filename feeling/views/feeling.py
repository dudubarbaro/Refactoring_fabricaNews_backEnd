from rest_framework.viewsets import ModelViewSet
from feeling.models import Feeling
from feeling.serializers import FeelingSerializer


class FeelingViewSet(ModelViewSet):
    queryset = Feeling.objects.all()  # pylint: disable=E1101
    serializer_class = FeelingSerializer
