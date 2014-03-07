from django.contrib import admin
from portfolio.models import item


class itemAdmin(admin.ModelAdmin):
	list_display = ('desc','image')

admin.site.register(item, itemAdmin)