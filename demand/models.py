from django.db import models
from users.models import tbUsers
# Create your models here.
house_type =[
    (1, '월세'),
    (2, '전세')
]

house_transaction_type = [
    (1, '아파트'),
    (2, '빌라'),
    (3, '단독주택'),
    (4, '다가구주택'),
    (5, '오피스텔'),

]

seoul_area = [
    (1,'강남구'),
    (2,'강동구'),
    (3,'강북구'),
    (4,'강서구'),
    (5,'관악구'),
    (6,'광진구'),
    (7,'구로구'),
    (8,'금천구'),
    (9,'노원구'),
    (10,'도봉구'),
    (11,'동대문구'),
    (12,'동작구'),
    (13,'마포구'),
    (14,'서대문구'),
    (15,'서초구'),
    (16,'성동구'),
    (17,'성북구'),
    (18,'송파구'),
    (19,'양천구'),
    (20,'영등포구'),
    (21,'용산구'),
    (22,'은평구'),
    (23,'종로구'),
    (24,'중구'),
    (25,'중랑구')    
]

class tbDemands(models.Model):
    email = models.ForeignKey(tbUsers, on_delete=models.CASCADE, db_column='email')
    house_type_code = models.IntegerField(choices=house_type)
    house_type_name = models.CharField(max_length=100, editable= False)
    house_transaction_code = models.IntegerField(choices=house_transaction_type, default= 1)
    house_transaction_name = models.CharField(max_length=100, editable= False)
    house_location_code = models.IntegerField(choices = seoul_area)
    house_location_name = models.CharField(max_length=100, editable =False)
    house_min_price = models.IntegerField()
    house_max_price = models.IntegerField()

    def save(self, *args, **kwargs):
        # 코드에 따른 이름 자동 설정
        for code, name in house_type:
            if self.house_type_code == code:
                self.house_type_name = name
                break
        # 코드에 따른 이름 자동 설정
        for code, name in house_transaction_type:
            if self.house_transaction_code == code:
                self.house_transaction_name = name
                break
        # 코드에 따른 이름 자동 설정
        for code, name in seoul_area:
            if self.house_location_code == code:
                self.house_location_name = name
                break
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "Demand"          # 단수형 이름
        verbose_name_plural = "Demands"  # 복수형 이름