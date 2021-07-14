from django.db import models
from django.conf import settings

class Event(models.Model):
    unit = models.CharField(u'單位',max_length=20)
    date = models.DateTimeField('日期', null=True)
    title = models.CharField(u'標題',max_length=50)

    def __str__(self):
        return self.title

class Message(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )

    date = models.DateTimeField('日期', null=True)
    message = models.CharField(u'留言',max_length=1000)

    def __str__(self):
        return self.user.username
