from django.shortcuts import *
from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *



def welcome_page(request):
    suites = Room.objects.all()
    context = {"suites":suites}
    return render(request, "home.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def faqq(request):
    faq = FAQ.objects.all()
    if request.method == "POST":
        question = request.POST.get("question")
        fullname = request.POST.get("fullname")
        faq_obj = FAQ(question = question, fullname = fullname)
        faq_obj.save()
        messages.success(request, "Success!")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {"faq":faq}
    return render(request, "faq.html", context)


def contact(request):
    if request.method == "POST":
        message = request.POST.get("message")
        email = request.POST.get("email")
        fullname = request.POST.get("fullname")
        contact_save_obj = ContactSave(message = message, email = email, fullname = fulname)
        contact_save_obj.save()
       
    context = {}
    return render(request, "contact.html", context)


def login_page(request):
    context = {}
    return render(request, "login.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password = password)
        if user is not None:
            dlogin(request, user)
            if username == "admin" or username == "admin_user" or username == "admin2":
                return redirect("admin-welcome-page")
            else:
                return redirect("welcome-page")
        messages.error(request, "Invalid Login Details")
        return redirect("login-page")
    else:
        return redirect("login-page")


def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fullname = request.POST.get("fullname")
        cellphone = request.POST.get("cellphone")
        password = request.POST.get("password")
        user = User.objects.create_user(username = username, password = password, first_name = fullname, last_name = cellphone)
        user.save()
        wallet = Wallet(user = user, account_bal=0)
        wallet.save()
        return redirect("login-page")
    context = {}
    return render(request, "signup.html", context)
    

def logout_page(request):
    dlogout(request)
    return redirect("/")
