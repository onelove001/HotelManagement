from django.shortcuts import *
from .models import *
from django.contrib import messages


def view_suites(request):
    suites = Room.objects.all()
    user = request.user
    wallet = Wallet.objects.get(user = user)
    context = {"user": user, "suites":suites, "wallet":wallet}
    return render(request, 'user/view_suites.html', context)


def suite_details(request, suite_id):
    suite = Room.objects.get(id = suite_id)
    guidelines = Guideline.objects.all().first()
    print(guidelines)
    context = {"suite":suite, "guidelines":guidelines}
    return render(request, "user/suite_details.html", context)


def suite_request(request):
    user_obj = request.user
    wallet = Wallet.objects.get(user = user_obj)
    if request.method == "POST":
        suite = request.POST.get("room_id")
        nights = request.POST.get("nights")
        suite_obj = Room.objects.get(id = suite)
        new_charge = int(nights) * suite_obj.package.charge
        if wallet.account_bal >= new_charge:
            suite_request_obj = SuiteRequest(user = user_obj, room = suite_obj, nights=nights)
            suite_request_obj.save()
            wallet.account_bal -= new_charge
            wallet.save()
            suite_obj.user = user_obj
            suite_obj.is_available = False
            suite_obj.save()
            messages.success(request, "Successfully Applied For This Room, Please proceed to your dashboard for your request confirmation!")
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "Sorry! You do not have a enough balance in your wallet to apply for this room!")
            return redirect(request.META.get("HTTP_REFERER"))


def payment(request):
    wallet = Wallet.objects.get(user = request.user)
    user = request.user
    if request.method == "POST":
        card_number = request.POST.get("card_number")
        full_name = request.POST.get("fullname")
        cvv = request.POST.get("cvv")
        expire = request.POST.get("expire")
        amount = request.POST.get("amount")
        deposit = Deposit(user = user, full_name = full_name, card_number = card_number, cvv = cvv, expire = expire, amount = amount)
        deposit.save()
        wallet.account_bal += int(amount)
        wallet.save()
        messages.success(request, "Success!")
        return redirect(request.META.get("HTTP_REFERER"))

    context = {}
    return render(request, "user/payment.html", context)


def room_transfer(request):
    user = request.user
    wallet = Wallet.objects.filter(user = user).first()
    is_roomed = False
    rooms = []
    rooms_ = Room.objects.filter(is_available=True)
    if len(SuiteRequest.objects.filter(user = user, approved=True)) > 0:
        is_roomed = True
        rooms = Room.objects.filter(is_available=False, user=user)
        if request.method == "POST":
            reason = request.POST.get("reason")
            room_from = request.POST.get("room_from")
            room_to = request.POST.get("room_to")
            room_from_obj = Room.objects.get(id = room_from)
            room_to_obj = Room.objects.get(id = room_to)
            if room_to_obj.package.charge >= room_from_obj.package.charge and wallet.account_bal >= room_to_obj.package.charge:
                suit_req = SuiteRequest.objects.get(user = user, room = room_from)
                letf_bal = room_to_obj.package.charge - room_from_obj.package.charge
                wallet.account_bal -= letf_bal * suit_req.nights
                wallet.save()

                room_transfer_obj = SuiteChange(user = user, reason = reason, room_from = room_from_obj, room_to = room_to_obj)
                room_transfer_obj.save()

                suit_req.room = room_to_obj
                suit_req.save()

                room_to_obj.is_available = False
                room_to_obj.user = user
                room_to_obj.save()

                room_from_obj.is_available = True
                room_from_obj.user = None
                room_from_obj.save()

                messages.success(request, "Successfully requested for room transfer. Please continue to check your dashboard for your request confirmation!")
                return redirect(request.META.get("HTTP_REFERER"))
            else:
                messages.error(request, "Sorry, you can't apply for this room due to insufficient balance")
                return redirect(request.META.get("HTTP_REFERER"))

    context = {"is_roomed":is_roomed, "user":user, "rooms":rooms, "rooms_":rooms_}
    return render(request, "user/room_transfer.html", context)


def guest_stay(request):
    is_student = False
    is_roomed = False
    student_user = Student_Account.objects.filter(user = request.user).first()
    if student_user:
        is_student = True
    if Accomodation_Request.objects.filter(student = student_user, approved=True).first():
        is_roomed = True

    if request.method == "POST":
        full_name = request.POST.get("guest_name")
        address = request.POST.get("address")
        reason = request.POST.get("reason")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        
        if GuestStayRequest.objects.filter(student = student_user).first():
            messages.error(request, "You cannot apply for more than one guest stay")
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            guest = GuestStayRequest(student = student_user, full_name=full_name, address=address, reason=reason, date_from=date_from, date_to=date_to)
            guest.save()
            messages.success(request, "Submitted Request Successfully, please check your dashboard for approval")
            return redirect(request.META.get("HTTP_REFERER"))


    context = {"is_student":is_student, "is_roomed":is_roomed}
    return render(request, "student/guest_stay.html", context)


def complaints(request):
    user = request.user
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        complain = HelpRequest(user = user, subject = subject, message = message)
        complain.save()
        messages.success(request, "Your ticket has being opened. Check your dashboard for response!")
    context = {"user":user}
    return render(request, "user/complain.html", context)
            

def room_service(request):
    user = request.user
    is_roomed = False
    rooms = Room.objects.filter(user = user, is_available=False)
    print(rooms)
    if request.method == "POST":
        room_id = request.POST.get("room_option")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        if len(rooms) > 0:
            is_roomed = True
            room_obj = Room.objects.get(id = room_id)
            room_s = RoomServiceRequest(user = user, room = room_obj, subject=subject, message=message)
            room_s.save()
            messages.success(request, "Request Sent!")
        else:
            messages.error(request, "You are not yet a customer")
    context = {"user":user, "rooms":rooms}
    return render(request, "user/room_service.html", context)
        

def request_dashboard(request):
    user = request.user
    room_service = RoomServiceRequest.objects.filter(user = request.user)
    suite_change = SuiteChange.objects.filter(user = user)  
    help_requests = HelpRequest.objects.filter(user = user)
    suite_requests = SuiteRequest.objects.filter(user = user)
    context = {"suite_change":suite_change, "help_requests":help_requests, "suite_requests":suite_requests, "room_service":room_service}
    return render(request, "user/request_dashboard.html", context)



