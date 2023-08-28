from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'authors', 'description', 'price',
        'created_date', 'auction', 'updated_date','get_html_image'
    ]
    list_filter = ['auction', 'created_at']
    actions = ['delete_description', 'make_auction_as_true', 'make_auction_as_false']
    fieldsets = (
        ('general', {
            'fields': ('title', 'description', 'authors','image')
        }),
        ('finance', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        }))

    class ImagesAdmin(admin.ModelAdmin):
        list_display = ('image_img', 'product',)



    @admin.action(description='Delete the description of the selected objects')
    def delete_description(self,request,queryset):
        queryset.update(text='')

    @admin.action(description='Enable the possibility of bargaining')
    def make_auction_as_true(self,request,queryset):
        queryset.update(auction=True)

    @admin.action(description='Disable the possibility of bargaining')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

admin.site.register(Advertisement,AdvertisementAdmin)