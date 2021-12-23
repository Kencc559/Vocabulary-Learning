from django.db import models
from users.models import User

# Create your models here.

class Vocab(models.Model):
    vocab = models.CharField("vocabulary", max_length=30, null=False)
    vocab_type = models.CharField("vocab_type", max_length=10)
    chinese = models.TextField()
    audio = models.ImageField(upload_to='audio/')
    image = models.ImageField(upload_to='image/')
    user = models.ForeignKey(User, null=True, on_delete="models.CASCADE")