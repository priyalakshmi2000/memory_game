from django.db import models
from django.contrib.auth.models import User

class score1(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateField()
    score=models.IntegerField()
    user_name=models.CharField(max_length=50)
    #def __str__(self):
        #return f"{self.user_name}"
class payment3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=50)
    pay=models.CharField(max_length=50)
    amount=models.IntegerField()
    date_created=models.DateField()

class payment4(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=50)
    pay=models.CharField(max_length=50)
    amount=models.IntegerField()
    date_created=models.DateField()

class score2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateField()
    score=models.IntegerField()
    user_name=models.CharField(max_length=50)
class score3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateField()
    score=models.IntegerField()
    user_name=models.CharField(max_length=50)
class score4(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateField()
    score=models.IntegerField()
    user_name=models.CharField(max_length=50)

mydic={"empid":1,"empname":"priya"}
    
