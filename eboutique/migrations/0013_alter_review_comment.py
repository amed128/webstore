# Generated by Django 3.2.6 on 2021-10-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eboutique', '0012_auto_20211028_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
