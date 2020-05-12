from django.urls import path
from . import views

app_name = "rooms"


urlpatterns = [
    path('detail/<int:id>/', views.room_detail, name='detail'),
]