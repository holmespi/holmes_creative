from django.contrib import admin
from portfolio.models import item
from portfolio.models import freeLunch
from portfolio.models import sketch

class itemAdmin(admin.ModelAdmin):
	list_display = ('id', 'desc', 'image')

admin.site.register(item, itemAdmin)

class freeLunchAdmin(admin.ModelAdmin):
	list_display = ('id', 'desc')

admin.site.register(freeLunch, freeLunchAdmin)

class sketchAdmin(admin.ModelAdmin):
	list_display = ('id', 'desc')

admin.site.register(sketch, sketchAdmin)