from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Game(models.Model):
    Game= models.CharField(max_length=255, null=False, blank=True)
    player = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Consel=models.CharField(max_length=255, null=False, blank=True)
    Discription = models.TextField()