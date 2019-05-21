from django.shortcuts import render
from rest_framework.views import APIView
from sendsms import api
from django.contrib import messages

# Create your views here.

class SmsSend(APIView):

    def get(self,request):
        return render(request,'sms.html')

    def post(self, request):
        message = request.data.get('message')
        if api.send_sms(body=message, from_phone='+7014784612', to=['+8823962379']):
            messages.success(request,"SMS sent successfully")
        else:
            messages.error(request, "Not sent successfully!!! ")
        return render(request, 'sms.html')




