from django.db import models
from personal.models import Teacher, Student

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default="教師")
    student = models.ManyToManyField(Student, default="學生")

    CATEGORY = (('國文', '國文'),('數學', '數學'),('英文', '英文'),('自然', '自然'),('社會', '社會'),('技術', '技術'))
    categories = models.CharField(u'科目',choices=CATEGORY,max_length=10,default='請選擇科目')
    name = models.CharField(u"課程名稱",max_length=20)
    descritions = models.CharField("介紹",max_length=5000)
    image = models.ImageField(u'課程封面',upload_to='picture/%Y/%m/%d/')
    lessons = models.IntegerField(u"課堂數")
    cost = models.IntegerField(u"T幣")

    def __str__(self):
        return self.name

# Create your models here.
