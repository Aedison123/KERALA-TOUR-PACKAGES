# admin.py
from django import forms
from django.contrib import admin
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'custom-image-class'})
        self.fields['image2'].widget.attrs.update({'class': 'custom-image-class'})

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'price', 'description', 'image', 'image2', 'days', 'is_approved')  # Added is_approved
    list_filter = ('price', 'is_approved')  # Added is_approved filter
    search_fields = ('name', 'description', 'days')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'image', 'image2', 'days', 'is_approved')  # Added is_approved
        }),
    )
    actions = ['approve_products']

    def approve_products(self, request, queryset):
        """Approve selected products."""
        updated_count = queryset.update(is_approved=True)
        self.message_user(request, f'{updated_count} products were successfully approved.')

    approve_products.short_description = 'Approve selected products'

admin.site.register(Product, ProductAdmin)
