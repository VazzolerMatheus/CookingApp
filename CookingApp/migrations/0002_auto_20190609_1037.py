# Generated by Django 2.0.5 on 2019-06-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='shortDescription',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(),
        ),
    ]
