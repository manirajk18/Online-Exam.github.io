# Generated by Django 4.0.3 on 2022-07-18 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examinee', '0003_examinee_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinee',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='examinee',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='examinee',
            name='rollno',
            field=models.CharField(max_length=20),
        ),
    ]
