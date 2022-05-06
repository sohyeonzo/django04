from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pic=models.ImageField(upload_to="user/%y/%m")
    age=models.IntegerField(default=1)
    comment=models.TextField()  # 이 부분은 원래 없는 거여서 넣어준 거임

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/user/noimage.png"
    