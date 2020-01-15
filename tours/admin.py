from django.contrib import admin
from .models import *

'''----------------------------COMMENTS------------------------'''


class CommentAdmin(admin.ModelAdmin):
    list_display = ('tour', 'author', 'date')
    list_filter = ('tour', 'author', 'date')


admin.site.register(Comment, CommentAdmin)

'''-----------------------IMAGES--------------------------'''


class TourImageInline(admin.TabularInline):
    model = Images
    extra = 3


'''-------------------------TOURS------------------------------'''


class TourAdmin(admin.ModelAdmin):
    list_filter = ('title', 'category',)
    list_display = ('title', 'category',)
    inlines = [TourImageInline, ]


admin.site.register(Tour, TourAdmin)


'''-----------------------------CATEGORY------------------'''


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


admin.site.register(Category, CategoryAdmin)
