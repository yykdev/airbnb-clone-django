from django.urls import path

from rooms import views as rooms_view

app_name = "core"

urlpatterns = [
    path("", rooms_view.all_rooms, name="home"),
]
