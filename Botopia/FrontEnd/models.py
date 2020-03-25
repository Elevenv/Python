from django.db import models
 
class User_info(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profile_pic = models.FileField(upload_to='media/',default='none')

class Bot_info(models.Model):
    bot_name = models.CharField(max_length=50)
    bot_id = models.IntegerField()
    bot_image = models.FileField(upload_to = 'media/')
    bot_url = models.URLField(max_length=100)
    author = models.ForeignKey(User_info,on_delete=models.CASCADE)
    bot_desc = models.CharField(max_length=300)