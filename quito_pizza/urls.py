from django.urls import path

from . import views

app_name = "quito_pizza"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]