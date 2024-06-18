from django.contrib import admin
from .models import student_info

# Register your models here.
@admin.register(student_info)
class student_infoAdmin(admin.ModelAdmin):
    list_display=["name","sex","citizen_id","student_id","school","in_class","status"]
    list_filter=["student_id"]
    ordering = ["student_id"]
    list_per_page = 20

    search_fields=["name","citizen_id","student_id"]

    admin.site.site_header = "student_info management"#修改管理员界面header