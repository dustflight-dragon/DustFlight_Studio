from django.contrib import admin
from .models import Category, Tag, Recommand, Dragon_Article_Post, Banner, Link


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')


@admin.register(Recommand)
class RecommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'recommand_name')


@admin.register(Dragon_Article_Post)
class Dragon_Article_Post_Admin(admin.ModelAdmin):
    list_display = ('id', 'dragon_article_category', 'dragon_article_title', 'dragon_article_recommand',
                    'dragon_article_author', 'dragon_article_views', 'dragon_article_publish_date')
    list_per_page = 50
    ordering = ('-dragon_article_publish_date',)
    list_display_links = ('id', 'dragon_article_title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_text_info', 'banner_image',
                    'banner_link_url', 'banner_is_active')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_name', 'link_url')
