from django.contrib import admin
from .models import Tutorial,Preview, PreviewLife, TutorialLife


admin.site.register(Preview)
admin.site.register(Tutorial)
admin.site.register(PreviewLife)
admin.site.register(TutorialLife)