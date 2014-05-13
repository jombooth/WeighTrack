from django.contrib import admin
from weightrack_app.models import TaggedItem,  Scale, Order

admin.site.register(TaggedItem)
admin.site.register(Scale)
admin.site.register(Order)
