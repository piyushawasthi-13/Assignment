from django.urls import path
from . import views
  

urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("chat/",views.Chat_Message,name="chatpage"),
    path("chat/<pk>",views.Chat_show,name="ChatShow"),
    path("send_message/<id>",views.Send_message,name="SendMessage")
]