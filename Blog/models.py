from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# from DjangoUeditor.models import UEditorField
class Category(models.Model):
    category_name = models.CharField('博文类别', max_length=100)
    category_index = models.IntegerField(default=999, verbose_name='类别索引')

    class Meta:
        verbose_name = '博文类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Recommand(models.Model):
    recommand_name = models.CharField('推荐空间', max_length=100)

    class Meta:
        verbose_name = '推荐空间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.recommand_name


class Dragon_Article_Post(models.Model):
    dragon_article_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    dragon_article_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='博客类别', blank=True,
                                                null=True)
    dragon_article_tags = models.ManyToManyField(Tag, verbose_name='Article_Tag', blank=True)
    dragon_article_img = models.ImageField(upload_to='article_image/%Y/%m/%d', verbose_name='文章配图', blank=True,
                                           null=True)
    dragon_article_title = models.CharField('文章标题', max_length=120)
    dragon_article_excerpt = models.TextField('Excerpt', max_length=200, blank=True)
    dragon_article_content = models.TextField()
    # dragon_article_content = UEditorField('内容', width=800, height=500,
    #                                       toolbars="full",
    #                                       imagePath="upimg/",
    #                                       filePath="upfile/",
    #                                       upload_settings={
    #                                           "imageMaxSize": 1204000},
    #                                       settings={}, command=None,
    #                                       blank=True
    #                                       )
    dragon_article_views = models.PositiveIntegerField('访问量', default=0)
    dragon_article_recommand = models.ForeignKey(Recommand, on_delete=models.DO_NOTHING, verbose_name='推荐空间',
                                                 blank=True, null=True)
    dragon_article_publish_date = models.DateTimeField('发布日期', auto_now_add=True)
    dragon_article_update_date = models.DateTimeField('更改日期', auto_now=True)

    class Meta:
        verbose_name = '文章发布'
        verbose_name_plural = verbose_name
        ordering = ('-dragon_article_publish_date',)

    def __str__(self):
        return self.dragon_article_title


class Banner(models.Model):
    banner_text_info = models.CharField('标题', max_length=50, default='')
    banner_image = models.ImageField('轮播图', upload_to='banner/')
    banner_link_url = models.URLField('图片链接', max_length=100)
    banner_is_active = models.BooleanField('是否是active', default=False)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.banner_text_info


class Link(models.Model):
    link_name = models.CharField('链接名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.link_name
