from django.db import models
from personal.models import Teacher, Student

class Camp(models.Model):
    contractor = models.ForeignKey(Teacher, on_delete=models.CASCADE, default="承辦人")
    applicant = models.ManyToManyField(Student, default="參加者")

    name = models.CharField(u'營隊名稱',max_length=20)
    date = models.DateTimeField('舉辦日期', null=True)
    pos = models.CharField(u'營隊地點',max_length=20)
    cost = models.IntegerField(u'費用')
    descritions = models.TextField(u'介紹',max_length=1000)

    def __str__(self):
        return self.name

# Create your models here.
