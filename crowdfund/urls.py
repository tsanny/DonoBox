from .views import *
from django.urls import path

app_name = "crowdfund"

urlpatterns = [
    path("", show_crowdfunds, name="show_crowdfunds"),
    path("<int:id>/", show_crowdfund, name="show_crowdfund"),
    path("json/", show_crowdfunds_json, name="show_crowdfunds_json"),
    path("json/ongoing/", show_crowdfunds_json_ongoing, name="show_crowdfunds_json_ongoing"),
    path("json/<int:id>/", show_crowdfund_json, name="show_crowdfund_json"),
]