app_name = "AuthService"
from django.conf.urls import url
from . import views as Authservice_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    url('signup/', Authservice_view.UserCreate.as_view(), name='create_account'),
    url('login/',Authservice_view.Loginview.as_view(), name='login'),
    url('logout/', LogoutView.as_view(), name='logout'),
    url('', Authservice_view.HomeView.as_view(), name='home'),

]

