from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from DjangoUeditor.models import UEditorField

#网站内容配置页面
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目导航'
        verbose_name_plural = '栏目导航'
        ordering = ['name']  # 排序

class Article(models.Model):
    title = models.CharField('标题',max_length=70)
    column = models.ForeignKey(Column, verbose_name='归属栏目')
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '内容管理'
        verbose_name_plural = '内容管理'

class Category(models.Model):
    name = models.CharField('新闻分类',max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '新闻分类'
        verbose_name_plural = '新闻分类'

class Post(models.Model):
    title = models.CharField('标题',max_length=70)
    body = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    modified_time = models.DateTimeField('发布时间',)
    source_link = models.CharField(max_length=200)
    excerpt = models.CharField('文章摘要',max_length=200, blank=True)
    category = models.ForeignKey(Category,related_name="cate",verbose_name='新闻分类')
    author = models.ForeignKey(User,verbose_name='作者')


    def get_absolute_url(self):
        return reverse('nepuapp:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻发布'
        verbose_name_plural = '新闻发布'

class Paper(models.Model):
    select_post = models.ForeignKey(Post, related_name='select_post')
    SELECT_REASON = (
        ('校园新闻', '校园新闻'),
        ('通知公告', '通知公告')
    )
    select_reason = models.CharField(choices=SELECT_REASON, max_length=100, null=False)

    def __str__(self):
        return self.select_reason + '-' + self.select_post.title