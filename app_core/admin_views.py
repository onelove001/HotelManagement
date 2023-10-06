from django.shortcuts import *
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


def admin_home(request):
    requestss = SuiteRequest.objects.all()
    context = {"requestss":requestss}
    return render(request, "admin_templates/admin_home.html", context)


def create_package(request):
    if request.method == "POST":
        name = request.POST.get("name")
        charge = request.POST.get("charge")
        description = request.POST.get("description")
        package_obj = Package(name=name, description=description, charge=charge)
        package_obj.save()
        messages.success(request, "Success")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {}
    return render(request, "admin_templates/create_package.html", context)


def create_wing_manager(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone_no = request.POST.get("phone_no")
        wing_manager = WingManager(first_name = first_name, last_name = last_name, email = email,  address = address, phone_no = phone_no)
        wing_manager.save()
        messages.success(request, "Success")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {}
    return render(request, "admin_templates/create_wing_manager.html", context)


def create_wing(request):
    wing_managers = WingManager.objects.all()
    if request.method == "POST":
        wing_manager = request.POST.get("wing_manager")
        wing_name = request.POST.get("wing_name")
        wing_number = request.POST.get("wing_number")
        wing_manager_obj = WingManager.objects.filter(id = wing_manager).first()
        wing = Wing(wing_manager = wing_manager_obj, wing_name = wing_name, wing_number = wing_number)
        wing.save()
        messages.success(request, "Success")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {"wing_managers":wing_managers}
    return render(request, "admin_templates/create_wing.html", context)


def create_room_service(request):
    wings = Wing.objects.all()
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        phone_number = request.POST.get("cellphone")
        wing_name = request.POST.get("wing_name")
        wing_obj = Wing.objects.filter(id = wing_name).first()
        room_service = RoomService(wing = wing_obj, first_name=first_name, last_name=last_name, phone_number=phone_number)
        room_service.save()
        messages.success(request, "Success")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {"wings":wings}
    return render(request, "admin_templates/create_room_service.html", context)


def create_suite(request):
    wings = Wing.objects.all()
    packages = Package.objects.all()
    if request.method == "POST":
        room_number = request.POST.get("room_number")
        room_tag = request.POST.get("room_tag")
        room_condition = request.POST.get("room_condition")
        package_name = request.POST.get("package_name")
        wing_name = request.POST.get("wing_name")
        wing_obj = Wing.objects.filter(id = wing_name).first()
        package_obj = Package.objects.filter(id = package_name).first()
        image1 = request.FILES["image1"]
        image2 = request.FILES["image2"]
        image3 = request.FILES["image3"]

        fs = FileSystemStorage()
        profile_image1_save = fs.save(image1.name, image1)
        profile_image2_save = fs.save(image2.name, image2)
        profile_image3_save = fs.save(image3.name, image3)

        image1_url = fs.url(profile_image1_save)
        image2_url = fs.url(profile_image2_save)
        image3_url = fs.url(profile_image3_save)

        room = Room(wing=wing_obj, package=package_obj, room_number=room_number, room_tag=room_tag, condition=room_condition, image1=image1_url, image2=image2_url, image3=image3_url, is_available=True)
        room.save()
        messages.success(request, "Success!")
        return redirect(request.META.get("HTTP_REFERER"))

    context = {"wings":wings, "packages":packages}
    return render(request, "admin_templates/create_suite.html", context)


def manage_request(request):
    context = {}
    return render(request, "admin_templates/admin_home.html", context)


def manage_suite_change(request):
    suit_changes = SuiteChange.objects.all()
    context = {"suit_changes":suit_changes}
    return render(request, "admin_templates/manage_suite_change.html", context)


def manage_help_request(request):
    help_requests = HelpRequest.objects.all()
    context = {"help_requests":help_requests}
    return render(request, "admin_templates/manage_help_request.html", context)


def manage_room_service(request):
    room_service_requests = RoomServiceRequest.objects.all()
    context = {"room_service_requests":room_service_requests}
    return render(request, "admin_templates/manage_room_service.html", context)


def manage_rule(request):
    if request.method == "POST":
        rule = request.POST.get("rule")
        guideline1 = request.POST.get("guideline1")
        guideline2 = request.POST.get("guideline2")
        guideline3 = request.POST.get("guideline3")
        guideline4 = request.POST.get("guideline4")
        guideline5 = request.POST.get("guideline5")
        guideline = Guideline(rule = rule, guideline1 = guideline1, guideline2=guideline1, guideline3=guideline3, guideline4=guideline4, guideline5=guideline5)
        guideline.save()
        messages.success(request, "Success")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {}
    return render(request, "admin_templates/manage_rule.html", context)


def approve_or_disapprove(request, ac_id):
    accomodation_req = SuiteRequest.objects.filter(id = ac_id).first()
    if accomodation_req.approved == True:
        accomodation_req.approved = False
    else:
        accomodation_req.approved = True
    accomodation_req.save()
    return redirect(request.META.get("HTTP_REFERER"))


def help_request_status(request, complain_id):
    help_request = HelpRequest.objects.filter(id = complain_id).first()
    if help_request.status == True:
        help_request.status = False
    else:
        help_request.status = True
    help_request.save()
    return redirect(request.META.get("HTTP_REFERER"))


def suite_change_status(request, transfer_id):
    transfer = SuiteChange.objects.filter(id = transfer_id).first()
    if transfer.approved == True:
        transfer.approved = False
    else:
        transfer.approved = True
    transfer.save()
    return redirect(request.META.get("HTTP_REFERER"))


def room_service_request_status(request, rors_id):
    room_service_request = RoomServiceRequest.objects.filter(id = rors_id).first()
    if room_service_request.status == True:
        room_service_request.status = False
    else:
        room_service_request.status = True
    room_service_request.save()
    return redirect(request.META.get("HTTP_REFERER"))
