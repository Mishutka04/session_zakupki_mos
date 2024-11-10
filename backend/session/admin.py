from django.contrib import admin
from .models import Violation


@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display = ('name', 'example', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'example')
    actions = ['make_active', 'make_inactive']

    # Действия для массового включения и отключения нарушений
    @admin.action(description='Включить выбранные нарушения')
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Отключить выбранные нарушения')
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
