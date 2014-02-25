from django.contrib import admin
from home.models import member

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ("First Name", {'fields': ['first_name']}),
        ("Last Name", {'fields': ['last_name']}),
        ("Grade Level", {'fields': ['grade']} )
    ]
    list_display = ("first_name", "last_name", 'grade')
    search_fields = ['last_name']
admin.site.register(member, MemberAdmin )



