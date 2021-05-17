from django.db import models

# Create your models here.

class Work(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar')
    title = models.CharField(max_length=25,verbose_name='Basliq')
    content = models.TextField(verbose_name='Mezmun')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='Tarix')
