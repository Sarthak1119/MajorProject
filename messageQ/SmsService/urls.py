app_name = "SmsService"
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.SmsSend.as_view(),name='sms')
]