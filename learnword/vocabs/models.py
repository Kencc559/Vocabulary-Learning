from django.db import models
from users.models import User

# Create your models here.

class Vocab(models.Model):
    id = models.AutoField(primary_key=True)
    vocab = models.CharField("vocabulary", max_length=30, null=False)
    vocab_type = models.CharField("vocab_type", max_length=10)
    chinese = models.TextField()
    audio = models.ImageField(upload_to='audio/')
    image = models.ImageField(upload_to='images/')
    created_time = models.DateTimeField(auto_now_add=True)
    review_cycle = models.CharField('review_cycle', max_length=9999,default='0')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, null=True)

class Learningweb(models.Model):
    id = models.AutoField(primary_key=True)
    webname = models.CharField("webname", max_length=30)
    webaddr = models.CharField("webaddr", max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, null=True)

