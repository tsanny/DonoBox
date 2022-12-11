from .views import *
from django.urls import path

app_name = "crowdfund"

urlpatterns = [
    path("", show_crowdfunds, name="show_crowdfunds"),
    path("<int:id>/", show_crowdfund, name="show_crowdfund"),
    path("funds/json/ongoing/", show_crowdfunds_json_ongoing, name="show_crowdfunds_json_ongoing"),
    path("funds/json/myfunds/", show_crowdfunds_json_by_me, name="show_crowdfunds_json_by_me"),
    path("funds/json/<int:id>/", show_crowdfund_json, name="show_crowdfund_json"),
    path("donations/json/<int:id>/", show_donations_json_by_fund, name="show_donations_json_by_fund"),
    path("funds/add/", add_crowdfund, name="add_crowdfund"),
    path("donations/add/<int:id>/", add_donation, name="add_donation"),
    path("flutter/funds/<str:fundraiser_name>", flutter_crowdfunds_by_fundraiser, name="flutter_crowdfunds_by_fundraiser")
]