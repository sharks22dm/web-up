from django.db import models


# Create your models here.
class MovProduct(models.Model):
    product = models.TextField('Наименование товара')
    total = models.IntegerField('Количество', default=1)
    status = models.CharField('Статус товара', max_length=20)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'