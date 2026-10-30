from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(verbose_name='Слаг', unique=True, max_length=120)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(
        max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(verbose_name='Слаг', unique=True, max_length=170)
    description = models.TextField(
        verbose_name='Описание', blank=True, null=True)
    photo = models.ImageField(
        upload_to='photos/', null=True, blank=True, verbose_name='Фото')
    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='articles')
    user = models.ForeignKey(
        'auth.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автор')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
