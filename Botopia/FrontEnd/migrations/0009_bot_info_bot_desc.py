# Generated by Django 3.0.4 on 2020-03-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0008_auto_20200321_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot_info',
            name='bot_desc',
            field=models.CharField(default='Empty', max_length=300),
            preserve_default=False,
        ),
    ]