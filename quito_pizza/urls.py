from django.urls import path

from . import views

app_name = "quito_pizza"
urlpatterns = [
    path("", views.index, name="index"),
    path("pizza/", views.list_pizza, name="list_pizza"),
    path("pizza/<int:pizza_id>/", views.pizza, name="pizza"),
    path("pizza/add/", views.add_pizza, name="add_pizza"),
    path("pizza/edit/<int:pizza_id>/", views.edit_pizza, name="edit_pizza"),
    path("pizza/delete/<int:pizza_id>/", views.delete_pizza, name="delete_pizza"),
    path("category/", views.list_category, name="list_category"),
    path("category/add/", views.add_category, name="add_category"),
    path("category/edit/<int:category_id>/", views.edit_category, name="edit_category"),
    path("category/delete/<int:category_id>/", views.delete_category, name="delete_category"),
    path("client/", views.list_client, name="list_client"),
    path("client/<int:client_id>/", views.client, name="client"),
    path("client/add/", views.add_client, name="add_client"),
    path("client/edit/<int:client_id>/", views.edit_client, name="edit_client"),
    path("client/delete/<int:client_id>/", views.delete_client, name="delete_client"),
    path("product/", views.list_product, name="list_product"),
    path("product/<int:product_id>/", views.product, name="product"),
    path("product/add/", views.add_product, name="add_product"),
    path("product/edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("product/delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path("purchase/", views.list_purchase, name="list_purchase"),
    path("purchase/add/", views.add_purchase, name="add_purchase"),
    path("purchase/<int:purchase_id>/", views.purchase, name="purchase"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]