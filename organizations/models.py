from django.db import models


class DatesModelMixin(models.Model):
    """ Абстрактный класс, описывающий поля title, contact, product, debt, created,
        модели Factory, Retail, Entrepreneur наследуются от него """
    class Meta:
        abstract = True

    title = models.CharField(max_length=200, verbose_name="название")
    contact = models.OneToOneField('Contact', on_delete=models.CASCADE, verbose_name="контакты")
    product = models.ManyToManyField('Product')
    debt = models.FloatField(verbose_name='задолженность поставщику', default=0.0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


class Factory(DatesModelMixin):
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return self.title


class Retail(DatesModelMixin):
    supplier = models.ForeignKey('Factory', on_delete=models.CASCADE, verbose_name="поставщик")

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    def __str__(self):
        return self.title


class Entrepreneur(DatesModelMixin):
    supplier = models.ForeignKey('Retail', on_delete=models.CASCADE, verbose_name="поставщик")

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house = models.CharField(max_length=15, verbose_name='номер дома', blank=True)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Список контактов"

    def __str__(self):
        return f'{self.country}, {self.city}, ул.{self.street}, дом {self.house}'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель', blank=True)
    created = models.DateTimeField(verbose_name="Дата выхода продукта на рынок")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Список продуктов"

    def __str__(self):
        return self.title
