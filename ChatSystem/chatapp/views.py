from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import NewUserForm,MessageForm,EmailAuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import User,Chat
from django.urls import reverse
from django.contrib.auth import logout


# user register function
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        # print(form)
        if form.is_valid():
            print("user")
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful.")
            print("success")
            return redirect("login")
        else:
            messages.error(
                request, f"Unsuccessful registration. {form.errors.as_data()}")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


# user login function
def login_request(request):
    if request.method == "POST":
        print("request")
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print(form)
            Email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(Email,password)
            user = authenticate(Email=Email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {Email}.")
                print("login")
                return redirect("chatpage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            print(form.errors.as_data())
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

#Chat User showing functon
def Chat_Message(request):
    if request.user.is_authenticated:
        user=User.objects.filter(id=request.user.pk).first()
        active_user=User.objects.all().exclude(id=user.id)
        print("activeuserr",request.user)
        return render(request,'chat.html',context={
            'users':active_user,'reciever_user':user})
    else:
        return redirect("login")

#Chat show function
def Chat_show(request,pk):
    if request.user.is_authenticated:
        user=User.objects.get(id=pk)
        reciever_msg=Chat.objects.filter(receiver=request.user,sender=user)
        send_msg=Chat.objects.filter(sender=request.user,receiver=user) 
        active_user=User.objects.all().exclude(id=request.user.id)
        return render(request,'chat.html',context={
            'users':active_user,'reciver':reciever_msg,'sender':send_msg,'reciever_user':user})
    else:
        return redirect("login")
    
#Send_message function
def Send_message(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            content = request.POST.get('message')
            sender=User.objects.get(id=request.user.id)
            reciever=User.objects.get(id=id)
            Chat.objects.create(sender=sender,receiver=reciever,message=content)
            return redirect(reverse('ChatShow', args=[id]))
        else:
            print("error")
            return redirect(reverse('ChatShow', args=[id]))
    else:
        return redirect("login")
    
    
def logout_view(request):
    logout(request)
    return redirect("login")