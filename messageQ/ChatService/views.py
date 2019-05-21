from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from .serializer import CompanyDetails_serializer, UserMessage_serializer
from .models import CompanyDetails, Messages
from django.contrib import messages
# Create your views here.

class ChatBot(APIView):

    def get(self,request):
        return render(request,'chatbot.html')

    def post(self,request):
        name = request.data.get('name')
        contact = request.data.get('contact')
        website = request.data.get('web')
        about = request.data.get('about')
        services = request.data.get('service')

        serializer = CompanyDetails_serializer(data={'Name':name,'Contact':contact,'Website':website,'About':about,'Services':services})

        if serializer.is_valid():
            serializer.save()
            messages.success(request,message= "Thanks For Your Response!!")
        else:
            messages.error(request, message = "Your response is not recorded successfully \n Please Try Again !!! ")

        return render(request,'chatbot.html')


class Chatting(APIView):

    def get(self,request):
        return render(request,'chatting.html')

    def post(self, request):
        message = request.data.get('chat-msg')
        if any(word in message for word in ["bye","bye take care","Nice talking with you"]):
            Messages.objects.all().delete()
            messages.success(request, message="It was pleasure to talk with you!!!")
            return render(request,'chatting.html')
        user_check ='G'
        serializer = UserMessage_serializer(data={'user_check':user_check,'message':message})
        if serializer.is_valid():
             serializer.save()
        reply=''
        rep=''

        if all(word in message for word in  ['what', "does" ,"do"]):
            reply = CompanyDetails.objects.values_list('About')
            for r in reply:
                rep = r[0]
            user_check = 'B'

        elif any(word in message for word in ["company website", "website", "company link" ,"link"]):
            reply = CompanyDetails.objects.values_list('Website')
            for r in reply:
                rep = r[0]
            user_check= "B"

        elif any(word in message for word in ["company name", "name of your organisation"]):
            reply = CompanyDetails.objects.values_list('Name')
            for r in reply:
                rep = r[0]
            user_check = "B"

        elif any(word in message for word in ["what service", "service provide", "service", "provide"]):
            reply = CompanyDetails.objects.values_list('Services')
            for r in reply:
                rep = r[0]
            user_check = 'B'

        elif any(word in message for word in ["hi", 'hello' ,"hey there"] ):
            rep="Hi Guest !!"
            user_check='B'
        elif any(word in message for word in ["how are you"]):
            rep = "I am fine, how are you !!"
            user_check='B'
        elif any(word in message for word in ["fine","okay"]):
            rep= "Thats great !!!"
            user_check='B'
        elif any(word in message for word in ["who are you", "your name"]):
            rep = "I am Chimpi the Bot"
            user_check = 'B'
        elif any(word in message for word in ["why are your here", "why your are here", "why you"]):
            rep = "I am a software program and I am here to solve your issues \n feel free to ask any query . I try my best to answer your all queries"
            user_check='B'


        else:
            rep="Sorry I can't understand, what you are asking for!!! "
            user_check='B'

        serializer = UserMessage_serializer(data={'user_check':user_check,'message':rep})
        if serializer.is_valid():
            serializer.save()
        c = Messages.objects.all()
        return render(request, 'chatting.html',{'chat':c})






