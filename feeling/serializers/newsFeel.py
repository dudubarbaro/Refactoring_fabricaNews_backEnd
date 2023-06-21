from rest_framework.serializers import ModelSerializer
from feeling.models import NewsFeel


class NewsFeelSerializer(ModelSerializer):
    class Meta:
        model = NewsFeel
        fields = "__all__"
