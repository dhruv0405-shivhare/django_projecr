from django.db import models

class Student(models.Model):
    stu_enrollment=models.CharField(max_length=50)
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField(unique=True)
    stu_contact=models.IntegerField()
    stu_address=models.CharField(max_length=50)
    def __str__(self):
        return self.stu_name
    


class Registration(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact=models.IntegerField()
    password=models.CharField(max_length=50)
    cpassword=models.CharField(max_length=50)
    def __str__(self):
        return self.name    