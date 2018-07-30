from django.contrib import admin
from .models import Tutorial, Preview, LifeResume, LifeContent


# admin.site.register(Images)
admin.site.register(Preview)
admin.site.register(Tutorial)
admin.site.register(LifeResume)
admin.site.register(LifeContent)
