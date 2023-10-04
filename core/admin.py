from django.contrib import admin
from django.db import models
from .models import HomeContact, Owner, Skill, Testimonials, Images, Services, Contact, Category, FeatureService, WidgetItem
from ckeditor.widgets import CKEditorWidget
from django.utils.html import mark_safe

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'portfolio_link', 'designation', 'created_at', 'display_owner_image')
    list_filter = ("created_at",)
    search_fields = ['name', 'designation']

    def display_owner_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; border-radius: 50%;">')
        else:
            return 'No Image'

    display_owner_image.short_description = 'Owner Image'

class ImageAdmin(admin.ModelAdmin):
    list_display = ('display_logo', 'display_about', 'display_hero', 'created_at')
    list_filter = ("created_at",)

    def display_logo(self, obj):
        return self.display_image(obj.logo_file)

    def display_about(self, obj):
        return self.display_image(obj.about_file)

    def display_hero(self, obj):
        return self.display_image(obj.hero_file)

    def display_image(self, file_field):
        if file_field:
            return mark_safe(f'<img src="{file_field.url}" style="width: 50px; height: 50px; border-radius: 50%;">')
        else:
            return 'No Image'

    display_logo.short_description = 'Logo Image'
    display_about.short_description = 'About Image'
    display_hero.short_description = 'Hero Image'


class WidgetItemAdmin(admin.ModelAdmin):
    list_display = ('number', 'label', 'created_at')
    list_filter = ("created_at",)
    search_fields = ['number', 'label']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ("created_at",)
    search_fields = ['name', 'description']

class FeatureServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'created_at')
    list_filter = ("created_at",)
    search_fields = ['title', 'icon_class']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'display_service_picture')
    list_filter = ("created_at",)
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')}
    }

    def display_service_picture(self, obj):
        if obj.uploaded_file:
            return mark_safe(f'<img src="{obj.uploaded_file.url}" style="width: 50px; height: 50px; border-radius: 50%;">')
        else:
            return 'No Image'

    display_service_picture.short_description = 'Services Image'

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'created_at')
    list_filter = ("created_at",)
    search_fields = ['name', 'percentage']

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'quote', 'created_at', 'display_testimonial_picture')
    list_filter = ("created_at",)
    search_fields = ['name', 'created_at']

    def display_testimonial_picture(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; border-radius: 50%;">')
        else:
            return 'No Image'

    display_testimonial_picture.short_description = 'Testimonials Image'


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone')
    list_filter = ("created_at",)
    search_fields = ['first_name', 'email', 'message']

class HomeContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'message')
    list_filter = ("created_at",)
    search_fields = ['email', 'phone']

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(WidgetItem, WidgetItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FeatureService, FeatureServiceAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(HomeContact, HomeContactAdmin)