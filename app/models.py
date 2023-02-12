from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    price = price= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def get_absolute_url(self):
        return reverse('view_posts', kwargs={"pk": self.pk})
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')


    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']