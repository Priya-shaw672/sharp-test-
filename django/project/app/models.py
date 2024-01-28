from django.db import models
import uuid

# Create your models here.
'''class Login(models.Model):
    email=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=156)
    confirm_password=models.CharField(max_length=156)

    class Meta: #above class property,meta is rootclass ,it is keyword in django 
        db_table="userinfo"


    class Meta:
        db_table="submitquestions" '''
class Exam (models.Model):
        Question =models.CharField(max_length=255)
        option1=models.CharField(max_length=255)
        option2=models.CharField(max_length=255)
        option3=models.CharField(max_length=255)
        option4=models.CharField(max_length=255)
        correct=models.CharField(max_length=255)
        
        #class Meta:    
         #   db_table="exam"
class Gk (models.Model):
        Question =models.CharField(max_length=255)
        option1=models.CharField(max_length=255)
        option2=models.CharField(max_length=255)
        option3=models.CharField(max_length=255)
        option4=models.CharField(max_length=255)
        correct=models.CharField(max_length=255)
        marks=models.CharField(max_length=255)             


class Django (models.Model):
        Question =models.CharField(max_length=255)
        option1=models.CharField(max_length=255)
        option2=models.CharField(max_length=255)
        option3=models.CharField(max_length=255)
        option4=models.CharField(max_length=255)
        correct=models.CharField(max_length=255)
        marks=models.CharField(max_length=255) 

                               