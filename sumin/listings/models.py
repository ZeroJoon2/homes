from django.db import models
from django.contrib.auth.models import User

HOUSE_TYPE_CHOICES = [
    ('villa', '빌라/주택'),
    ('officetel', '오피스텔'),
    ('apartment', '아파트'),
    ('commercial', '상가/사무실'),
]

TRANSACTION_TYPE_CHOICES = [
    ('monthly_rent', '월세'),
    ('jeonse', '전세'),
    ('sale', '매매'),
]

house_type = models.CharField(
    max_length=20,
    choices=HOUSE_TYPE_CHOICES,
    default='villa'
)
transaction_type = models.CharField(
    max_length=20,
    choices=TRANSACTION_TYPE_CHOICES,
    default='sale'
)
class PropertyListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # user와 매물 연결
    address = models.CharField(max_length=255, blank=True)
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
    def __str__(self):
            return self.title

class PropertyImage(models.Model):
    property_listing = models.ForeignKey('PropertyListing', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
            return f"Image for {self.property_listing.title}"

