from django.contrib import admin
from viewshare.apps.augment.models import ListPattern, AugmentationErrorCode
from viewshare.apps.augment.forms import ListPatternForm


class ListPatternAdmin(admin.ModelAdmin):
    form = ListPatternForm
    list_display = ("title", "description")
admin.site.register(ListPattern, ListPatternAdmin)


class AugmentationErrorCodeAdmin(admin.ModelAdmin):
    list_display = ("error",)
admin.site.register(AugmentationErrorCode, AugmentationErrorCodeAdmin)
