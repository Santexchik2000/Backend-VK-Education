from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.template.defaultfilters import slugify


class Contract(models.Model):
    client = models.ForeignKey('Client', verbose_name='Клиент', on_delete=models.RESTRICT, related_name='contracts')
    recipient = models.ForeignKey('Recipient', verbose_name='Получатель', on_delete=models.RESTRICT, related_name='contracts')
    route = models.ForeignKey('Route', verbose_name='Маршрут',on_delete=models.RESTRICT, related_name='contracts')
    manager = models.ForeignKey('Manager', verbose_name='Менеджер', on_delete=models.RESTRICT, related_name='contracts')
    driver = models.ForeignKey('Driver', verbose_name='Водитель', on_delete=models.RESTRICT, related_name='contracts')
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    closing_date = models.DateTimeField()
    contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    count_loader = models.PositiveSmallIntegerField()
    comment = models.CharField('Комментарий к заказу', max_length=255)


class CommonInfo(models.Model):
    fname = models.CharField('Фамилия', max_length=45)
    lname = models.CharField('Имя', max_length=45)
    login = models.CharField('Логин', max_length=25)
    email = models.EmailField(max_length=40)
    telefon = models.CharField('Телефон', max_length=12)

    class Meta:
        abstract = True


class Client(CommonInfo):
    pass


class Manager(CommonInfo):
    pass


class Driver(CommonInfo):
    car_number = models.CharField('Номер машины', max_length=12)


class Loader(CommonInfo):
    pass


class Recipient(models.Model):
    fname = models.CharField('Фамилия получателя', max_length=45)
    lname = models.CharField('Имя получателя', max_length=45)
    telefon = models.CharField('Телефон получателя', max_length=12)


class Adress(models.Model):
    city = models.CharField('Город', max_length=64)
    street = models.CharField('Улица', max_length=64)
    house = models.CharField('Дом', max_length=25)
    flat = models.CharField('Квартира', max_length=4)
    adress_sender = models.BooleanField(default=True)


class Route(models.Model):
    adress_Sender = models.ForeignKey(
        'Adress', verbose_name='Адрес отправителя', on_delete=models.RESTRICT, related_name='routes_sender')
    adress_Recipient = models.ForeignKey(
        'Adress', verbose_name='Адрес получателя', on_delete=models.RESTRICT, related_name='routes_recipient')


class LoadersList(models.Model):
    loader = models.ForeignKey(
        'Loader', verbose_name='Грузчик', on_delete=models.RESTRICT, related_name='loaders')
    contract = models.ForeignKey(
        'Contract', verbose_name='Заказ', on_delete=models.RESTRICT, related_name='loaders')
