app_name = "ChatService"
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.ChatBot.as_view(), name='chatbot'),
    url(r'^chatbot/',views.Chatting.as_view(), name='chatting')
]