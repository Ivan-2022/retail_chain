from django.contrib import admin
from .models import Factory, Retail, Entrepreneur, Contact, Product


@admin.action(description='очистить задолженность')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.0)


class FactoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'contact', 'debt']
    search_fields = ['title', 'contact']


admin.site.register(Factory, FactoryAdmin)


class RetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'contact', 'supplier', 'debt']
    search_fields = ['title', 'contact']
    actions = [clear_debt]


admin.site.register(Retail, RetailAdmin)


class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ['title', 'contact', 'supplier', 'debt']
    search_fields = ['title', 'contact']
    actions = [clear_debt]


admin.site.register(Entrepreneur, EntrepreneurAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'country', 'city', 'street', 'house']
    search_fields = ['email', 'country', 'city']
    ordering = ['city']


admin.site.register(Contact, ContactAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'model', 'created']
    search_fields = ['title']


admin.site.register(Product, ProductAdmin)
