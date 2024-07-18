from django.contrib import admin
from .models import Form
# Register your models here.
admin.site.site_header='Job Application Management'
admin.site.site_title="Site Admin"
admin.site.index_title="Managing The Website,Welcome Admin!"

class FormAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','occupation')
    search_fields=('first_name','last_name','email')
    list_filter=('date','occupation')
    ordering=('first_name',)
    readonly_fields=('occupation',)


admin.site.register(Form,FormAdmin)