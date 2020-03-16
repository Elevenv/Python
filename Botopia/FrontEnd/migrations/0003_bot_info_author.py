# Generated by Django 3.0.2 on 2020-03-02 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0002_bot_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot_info',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.User_info'),
            preserve_default=False,
        ),
    ]