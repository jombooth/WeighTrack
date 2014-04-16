from django.contrib import admin
from weightrack_app.models import TaggedItem, Batch, Scale, WeighTrackR

admin.site.register(TaggedItem)
admin.site.register(Batch)
admin.site.register(Scale)
admin.site.register(WeighTrackR)