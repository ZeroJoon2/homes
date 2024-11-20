from django.db import models


# Create your models here.
class tbUsers(models.Model):
    email = models.CharField(unique=True, primary_key=True, max_length=40)
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=50)
    # isUse = models.charField(max_length= 1)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "users"  # 단수형 이름
        verbose_name_plural = "users"  # 복수형 이름
