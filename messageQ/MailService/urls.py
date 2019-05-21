app_name = "MailService"
from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.SendMail.as_view(), name='mail'),
    url(r'^sent/$', views.Showsentmail.as_view(), name='sent'),
    url(r'^inbox/$', views.ShowInboxMail.as_view(), name='inbox')

]