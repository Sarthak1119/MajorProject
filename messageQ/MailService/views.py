from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .serializer import Sent_mail_serializer, Inbox_mail_serializer
from .models import SentMail, InboxMail
import imaplib
import email


# Create your views here.


class SendMail(APIView):

    def get(self, request):

        return render(request,'composed.html')


    def post(self,request):
        subject = request.data.get('subject')
        message = request.data.get('message') + "\n\nFor any Query please follow the below link" +"\n\nhttp://127.0.0.1:8000/chat/chatbot"
        user_id = request.user.id
        if send_mail(subject, message, settings.EMAIL_HOST_USER, ['jainsarthak.dee@gmail.com','sarthakjain187@gmail.com','kajoldhabai1119@gmail.com','s43agarwal@gmail.com'], fail_silently=False):
            serializer = Sent_mail_serializer(data={'user':user_id,'subject':subject,'message':message})
            print(serializer)
            if serializer.is_valid():
                print("hello")
                serializer.save()
            messages.success(request,message="Mail sent successfully")
        else:
            messages.error(request,"Mail doesnot send successfully")
        return render(request,'composed.html')


class Showsentmail(APIView):

    def get(self, request):
        mails = SentMail.objects.filter(user=request.user.id)
        return render(request, 'Send.html',{'mails':mails})


class ShowInboxMail(APIView):

    def get_body(self, email_message):
        for payload in email_message.get_payload():
            break
        return(payload.get_payload())


    def read_email_from_gmail(self,request):

        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login("messageqa3@gmail.com", "admin@messageQ")
        mail.list()
        mail.select('Inbox')
        user_id = request.user.id


        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):
            typ, data = mail.fetch(str(i), '(RFC822)')

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_body = self.get_body(msg)

                    serializer = Inbox_mail_serializer(data={'user':user_id,'from_user':email_from, 'rec_subject':email_subject, 'message_rec':email_body})
                    if serializer.is_valid():
                        serializer.save()

    def get(self, request):
        InboxMail.objects.all().delete()
        self.read_email_from_gmail(request)
        rec_mail = InboxMail.objects.filter(user = request.user.id)
        return render(request, 'inbox.html', {'rec_mail': rec_mail})



