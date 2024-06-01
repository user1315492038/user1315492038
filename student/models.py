from django.db import models
from django.contrib import admin

# Create your models here.
class student_info(models.Model):
    name = models.CharField(max_length=10,primary_key=True)#姓名作为主键
    sex = models.CharField(max_length=7,default="")#三种情况:male,female,unknown
    citizen_id = models.CharField(max_length=18,unique=True)#身份证号
    student_id = models.CharField(max_length=19,unique=True)#学籍号
    school = models.CharField(max_length=20,default="")#学校
    in_class = models.CharField(max_length=10,default="")#规避关键字class,班级
    status = models.CharField(max_length=10)#状态

    password = models.CharField(max_length=18,default="123456")#用于登录的密码

    @admin.display(
        boolean=True,
        ordering="student_id",
        description="Ordered by student_id"
    )

    def __str__(self):
        return self.name