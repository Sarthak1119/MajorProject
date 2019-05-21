from rest_framework import serializers
from .models import SentMail, InboxMail


class Sent_mail_serializer(serializers.ModelSerializer):
    class Meta:
        model = SentMail
        fields = ('user', 'subject', 'message','date','time')

class Inbox_mail_serializer(serializers.ModelSerializer):
    class Meta:
        model = InboxMail
        fields = ('user', 'from_user', 'rec_subject','message_rec')