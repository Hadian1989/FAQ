from django.contrib import admin
from django.urls import path, include
from .models import *

admin.site.site_header = 'FAQ Dashboard'


# Register your models here.
# urlpatterns = [
# path('admin/', admin.site.urls),
# path('', include('pages.urls')), # new
# ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # readonly_fields = ['',]
    list_display = ('name','parent')
    list_filter = ['name', 'parent']
    list_per_page = 20
    actions_selection_counter = True
    # date_hierarchy = 'name'
    search_fields = ('name','parent')
    ordering = ('name', )