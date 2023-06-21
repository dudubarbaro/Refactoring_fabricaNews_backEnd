from django.db import models
from user.models.user import User
from project.models.news import News

class SaveToRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='SaveToReads')
    news = models.ForeignKey(News, on_delete=models.PROTECT, related_name='SaveToReads')
