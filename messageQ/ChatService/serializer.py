from rest_framework import serializers
from .models import CompanyDetails,Messages

class CompanyDetails_serializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = ('Name','Contact','Website','About','Services')


class UserMessage_serializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'