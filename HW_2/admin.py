from django.contrib import admin
from .models import User, Product, Order


@admin.action(description='RESET')
def reset_count(model_admin, request, queryset):
    queryset.update(count=0)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registered_at']
    search_fields = ['name']
    search_help_text = 'Search by name user'
    readonly_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'count', 'added_at']
    ordering = ['count']
    actions = [reset_count]
    search_fields = ['description']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'ordered_at']
    list_filter = ['ordered_at', 'total_price']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

