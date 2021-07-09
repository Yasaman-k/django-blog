from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    # age auto_now_filed nabashe khodemon bayad time set konim vali onjori khodesh set mikone
    image=models.ImageField(upload_to='%Y/%m/%d', null=True , blank=True)
    
    def __str__(self):
        return self.title 
        #return self.content
        # ina moadele post hastan toye html