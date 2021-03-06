from django.db import models
from django.conf import settings
from django.db import models

class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )

    @property
    def showIdentity(self):
        return "Teacher"

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )

    @property
    def showIdentity(self):
        return "Student"

    def __str__(self):
        return self.user.username

class Coin(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )

    coin = models.IntegerField(u"T幣數", default=5)

    @property
    def showBalance(self):
        return self.coin

    def __str__(self):
        return self.user.username

