from django.contrib import admin
from app.models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id','author','restimage','restname','restsite']
