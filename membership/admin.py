from django.contrib import admin
from membership.models import Member, Contact


admin.site.site_header = 'HTU Choir Administration'

class MemberAdmin(admin.ModelAdmin):
    list_display = ['membership_id', 'fname', 'part', 'registration_date']
    readonly_fields = ['membership_id']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'phone', 'date']


admin.site.register(Member, MemberAdmin)
admin.site.register(Contact, ContactAdmin)
