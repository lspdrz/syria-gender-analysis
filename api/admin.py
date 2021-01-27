from django.contrib import admin

from api.models import FacebookPost


class ScrapedDataAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FacebookPostAdmin(ScrapedDataAdmin):
    model = FacebookPost


admin.site.register(FacebookPost, FacebookPostAdmin)
