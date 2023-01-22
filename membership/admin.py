from django.contrib import admin
from membership.models import Member


admin.site.site_header = 'HTU Choir Administration'

class MemberAdmin(admin.ModelAdmin):
    list_display = ['membership_id', 'fname', 'part', 'registration_date']
    readonly_fields = ['membership_id']


admin.site.register(Member, MemberAdmin)
