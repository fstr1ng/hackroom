from django.contrib import admin

from .models import Policy, Category, File, Signature, SubSign, Option 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass


class FileInline(admin.StackedInline):
    model = File
    extra = 1
class SignatureInline(admin.StackedInline):
    model = Signature
    extra = 1
@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    radio_fields = {'type': admin.HORIZONTAL}
    readonly_fields = ('created_ts', 'updated_ts')
    fieldsets = (
        ('Timestamps', {
            'fields': (('created_ts', 'updated_ts'),),
            'classes': ('collapse',)
        }),
        ('Title', {
            'fields': (('name', 'issue'),'type'),
        }),
        ('Information', {
            'fields': ('categories', 'description', 'example'),
        }),
        ('Options', {
            'fields': ('active',),
        }),
    )
    inlines = [FileInline, SignatureInline]
    list_display = ('__str__', 'type','created_ts', 'updated_ts', 'active')
    list_editable = ('active',)
    list_filter = ('type', 'active', 'categories',)


@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    pass#filter_horizontal = ('options','subsigns')


@admin.register(SubSign)
class SubSignAdmin(admin.ModelAdmin):
    pass

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass
