from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "designation", "brand")
    list_filter = ("name", "designation")

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return  request.user is not None and obj is not None
    
    def has_view_permission(self, request, obj=None):
        return True
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "date_ordered", "processed", "transaction_id")
    
    def has_add_permission(self, request):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return  request.user is not None and obj is not None
    
    def has_view_permission(self, request, obj=None):
        return True

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedProduct)
admin.site.register(ShippingProduct)

