from django.db import models
from django.contrib.auth.models import User
from users.models import tbUsers
from django.db.models import UniqueConstraint
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
class tbSupply(models.Model):
    email = models.ForeignKey(tbUsers, on_delete=models.CASCADE, db_column='email')
    post_title = models.CharField(max_length=100, default = '제목을 입력해주세요')
    house_type_code = models.IntegerField(choices=house_type)
    house_type_name = models.CharField(max_length=100)
    house_transaction_code = models.IntegerField(choices=house_transaction_type, default= 1)
    house_transaction_name = models.CharField(max_length=100)
    house_location_code = models.IntegerField(choices = seoul_area)
    house_location_name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # 코드에 따른 이름 자동 설정
        for code, name in house_type:
            print(f'house_type:{house_type}')
            print(f'code:{code}')
            print(f'name:{name}')
            if self.house_type_code == code:
                self.house_type_name = name
                print('**************')
                print('하나씩 확인')
                print(f'self.house_type_code{self.house_type_code}')
                print(f'self.house_type_name{self.house_type_name}')
                print('**************')
                
                break
        # 코드에 따른 이름 자동 설정
        for code, name in house_transaction_type:
            if self.house_transaction_code == code:
                self.house_transaction_name = name
                print('**************')
                print('하나씩 확인')
                print(f'self.house_transaction_code{self.house_transaction_code}')
                print(f'self.house_transaction_name{self.house_transaction_name}')
                print('**************')
                break
        # 코드에 따른 이름 자동 설정
        for code, name in seoul_area:
            if self.house_location_code == code:
                self.house_location_name = name
                print('**************')
                print('하나씩 확인')
                print(f'self.house_location_code{self.house_location_code}')
                print(f'self.house_location_name{self.house_location_name}')
                print('**************')
                break
        # 확인용 출력문 추가
        print('여기 확인')
        print('********************')
        print(f"house_type_name: {self.house_type_name}")
        print(f"house_transaction_name: {self.house_transaction_name}")
        print(f"house_location_name: {self.house_location_name}")
        print('********************')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email.email


class PropertyListing(models.Model):
    list_id = models.ForeignKey(tbSupply, on_delete=models.CASCADE, db_column='supply_id')
    # 기본 키가 아닌 특정 필드를 참조하려면 to_field 사용
    email = models.ForeignKey(tbUsers, on_delete=models.CASCADE, db_column='email', to_field='email')
    address = models.TextField(blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    height  = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    rooms = models.IntegerField(default=0)
    bath = models.IntegerField(default=0)
    is_park = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    owner_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    surround = models.TextField(blank=True)
    etc = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='supply_images/', null = True)
    image2 = models.ImageField(upload_to='supply_images/', null = True)
    image3 = models.ImageField(upload_to='supply_images/', null = True)
    image4 = models.ImageField(upload_to='supply_images/', null = True)
    image5 = models.ImageField(upload_to='supply_images/', null = True)
    image6 = models.ImageField(upload_to='supply_images/', null = True)
    image7 = models.ImageField(upload_to='supply_images/', null = True)
 

    def __str__(self):
        return f"{self.list_id}"  # 원하는 형식으로 수정 가능

# class PropertyImage(models.Model):
#     property_listing = models.ForeignKey('PropertyListing', on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='property_images/')

#     def __str__(self):
#         return f"Image for {self.property_listing.title}"

