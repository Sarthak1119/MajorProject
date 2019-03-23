from rest_framework import serializers
from .models import SentMail


class Sent_mail_serializer(serializers.ModelSerializer):
    class Meta:
        model = SentMail
        fields = ('user', 'subject', 'message','date','time')