from django.contrib import admin
from .models import Pizza, Client, Purchase, Purchase_Detail, Product, Category
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Purchase_Detail)
class Pucharse_detailAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass



