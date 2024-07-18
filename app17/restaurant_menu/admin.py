from django.contrib import admin

from .models import Item

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal','chef','status')
    list_filter=('status','meal_type')
    search_fields=('meal','description')

admin.site.register(Item,MenuItemAdmin)