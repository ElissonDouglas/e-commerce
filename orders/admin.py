from django.contrib import admin
from .models import Order, OrderItems

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('criado', 'nome', 'total', 'finalizado')
    
    
admin.site.register(OrderItems)
