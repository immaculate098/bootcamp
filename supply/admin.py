# admin.py

from django.contrib import admin
from .models import Item, Supply, Issuing

# Register your models here.
admin.site.register(Item)
admin.site.register(Supply)
admin.site.register(Issuing)
