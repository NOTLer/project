from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(
        max_length=128, default="Имя не присвоено")
    category_picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"


class Product(models.Model):
    product_name = models.CharField(max_length=200, default="Имя не присвоено")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200, default="Имя не присвоено")
    country = models.CharField(max_length=200, default="Имя не присвоено")
    size = models.CharField(max_length=10, default="Имя не присвоено")
    prise = models.SmallIntegerField(default=0)
    product_picture = models.ImageField(upload_to='images/',
                                        default='nophoto.jpg')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

# class Employee(models.Model):
#
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#     ]
#
#     first_name = models.CharField(max_length=32)
#     last_name = models.CharField(max_length=32)
#     midle_name = models.CharField(max_length=32)
#     title = models.CharField(max_length=32)
#     birthday = models.DateField()
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES) # выбор пола
#     passport_number = models.CharField(max_length=11, unique=True) # уникальное значение
#     inn = models.CharField(max_length=12, blank=True) #необязательно заполнять
#     snils = models.CharField(max_length=11, blank=True)
