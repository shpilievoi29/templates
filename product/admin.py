from django.contrib import admin
from product.models import Product, Category, Comment, Feedback


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category']
    ordering = ['cid']


admin.site.register(Category, CategoryAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['category', 'product', 'amount']
    list_display = ['fid', 'category', 'amount']
    ordering = ['fid']


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    fields = ['product', 'comment_user', 'comment']
    list_display = ['co_id', 'comment_user', 'comment']
    ordering = ['co_id']


@admin.register(Feedback)
class ProductAdmin(admin.ModelAdmin):
    fields = ['comment_user', 'fe_comment', 'feedback']
    list_display = ['fe_id', 'comment_user', 'fe_comment']
    ordering = ['fe_id']
