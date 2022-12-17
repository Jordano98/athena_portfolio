from django.contrib import admin

from portfolio.models import Collection,All_col,Project,Pro_Gallery 

class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('pro_name','size','created_date','collection_name')
    list_filter = ('pro_name','created_date')
    search_fields = ['pro_name']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Pro_Gallery)
admin.site.register(All_col)
admin.site.register(Collection)


# Register your models here.
