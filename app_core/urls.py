from django.contrib import admin
from django.urls import path
from .user_views import *
from app_core.admin_views import *


app_name = "app"

urlpatterns = [

    # Users Urls ====================

    path("suites", view_suites, name = "view-suites"),
    path("suite_details/<str:suite_id>", suite_details, name = "suite-details"),
    path("payment", payment, name = "payment"),
    path("suite_request", suite_request, name = "suite-request"),
    path("room_transfer", room_transfer, name = "room-transfer"),
    path("complain", complaints, name = "complaints"),
    path("room_service", room_service, name = "room_service"),
    path("request_dashboard", request_dashboard, name = "request-dashboard"),

    # Admin Urls =======================

    path("create_package", create_package, name = "create-package"),
    path("create_wing_manager", create_wing_manager, name = "create-wing-manager"),
    path("create_wing", create_wing, name = "create-wing"),
    path("create_suite", create_suite, name = "create-suite"),
    path("create_room_service", create_room_service, name = "create-room-service"),
    
    path("manage_request", manage_request, name = "manage-request"),
    path("manage_suite_change", manage_suite_change, name = "manage-suite-change"),
    path("manage_help_request", manage_help_request, name = "manage-help-request"),
    path("manage_rule", manage_rule, name = "manage-rule"),
    path("manage_room_service", manage_room_service, name = "manage-room-service"),
    path("approve_or_disapprove/<str:ac_id>", approve_or_disapprove, name = "approve_or_disapprove"),
    path("help_request_status/<str:complain_id>", help_request_status, name = "help-request-status"),
    path("suite_change_status/<str:transfer_id>", suite_change_status, name = "suite-change-status"),
    path("room_service_request_status/<str:rors_id>", room_service_request_status, name = "room-service-request-status"),

]
