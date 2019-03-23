from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .serializer import Sent_mail_serializer
from .models import SentMail

# Create your views here.


class SendMail(APIView):

    def get(self, request):
        return render(request, 'mail.html')

    def post(self,request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        user_id = request.user.id
        if send_mail(subject, message, settings.EMAIL_HOST_USER, ['recipient_mail'], fail_silently=False):
            serializer = Sent_mail_serializer(data={'user':user_id,'subject':subject,'message':message})
            if serializer.is_valid():
                serializer.save()
            messages.success(request,message="Mail sent successfully")
        else:
            messages.error(request,"Mail doesnot send successfully")
        return render(request,'mail.html')


class Showsentmail(APIView):

    def get(self, request):
        mails = SentMail.objects.filter(user=request.user.id)
        print(mails)
        return render(request, 'sent.html',{'mails':mails})



