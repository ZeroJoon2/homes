from .models import *
from rest_framework import serializers
# class api_demand_list_serializer():
#     def get(self, request):
#         demand_list = tbDemands.objects.all()
#         serializer = 

class DemandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbDemands
        fields = '__all__'

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbDemands
        fields ='__all__'


class DemandsSerializer_title(serializers.ModelSerializer):
    class Meta:
        model = tbDemands
        fields = ['post_title']

class DemandsSerializer_image(serializers.ModelSerializer):
    class Meta:
        model = tbDemands
        fields = ['image1']