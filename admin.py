from django.contrib import admin
from .models import Plans, News

class PlansAdmin(admin.ModelAdmin):
    list_display = ['heading', 'plan_type', 'price','description',]

class NewsAdmin(admin.ModelAdmin):
    list_display = ['heading', 'created_at','content',]

admin.site.register(Plans, PlansAdmin)
admin.site.register(News, NewsAdmin)
