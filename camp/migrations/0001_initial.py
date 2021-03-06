# Generated by Django 3.2.5 on 2021-07-15 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0003_auto_20210715_0431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='營隊名稱')),
                ('date', models.DateTimeField(null=True, verbose_name='舉辦日期')),
                ('pos', models.CharField(max_length=20, verbose_name='營隊地點')),
                ('cost', models.IntegerField(verbose_name='費用')),
                ('descritions', models.TextField(max_length=1000, verbose_name='介紹')),
                ('applicant', models.ManyToManyField(default='參加者', to='personal.Student')),
                ('contractor', models.ForeignKey(default='承辦人', on_delete=django.db.models.deletion.CASCADE, to='personal.teacher')),
            ],
        ),
    ]
