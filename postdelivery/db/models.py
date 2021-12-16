from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
USER = get_user_model()


class Contract(models.Model):
    client = models.ForeignKey(USER, verbose_name='Клиент',
                               on_delete=models.RESTRICT, related_name='client_contracts')
    recipient = models.ForeignKey(
        'Recipient', verbose_name='Получатель', on_delete=models.RESTRICT, related_name='contracts')
    route = models.ForeignKey('Route', verbose_name='Маршрут',
                              on_delete=models.RESTRICT, related_name='contracts')
    manager = models.ForeignKey(USER, verbose_name='Менеджер',
                                on_delete=models.RESTRICT, related_name='manager_contracts')
    driver = models.ForeignKey(USER, verbose_name='Водитель',
                               on_delete=models.RESTRICT, related_name='drive_contracts')
    creation_date = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True, editable=False)
    closing_date = models.DateTimeField(verbose_name='Дата закрытия')
    contract_price = models.DecimalField(verbose_name='Цена контракта',max_digits=10, decimal_places=2)
    count_loader = models.PositiveSmallIntegerField(verbose_name='Количество грузчиков')
    comment = models.CharField('Комментарий к заказу', max_length=255)
    loaders = models.ManyToManyField(USER, verbose_name='Список грузчиков', related_name='loader_contracts')

    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'


class Recipient(models.Model):
    fname = models.CharField('Фамилия получателя', max_length=45)
    lname = models.CharField('Имя получателя', max_length=45)
    telefon = models.CharField('Телефон получателя', max_length=12)

    def __str__(self) -> str:
        return f"{self.fname} {self.lname} {self.telefon}"

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


class AdressSender(models.Model):
    city = models.CharField('Город', max_length=64)
    street = models.CharField('Улица', max_length=64)
    house = models.CharField('Дом', max_length=25)
    flat = models.CharField('Квартира', max_length=4)

    def __str__(self) -> str:
        return f"{self.id} {self.city} {self.street} {self.house} {self.flat}"
    class Meta:
        verbose_name = 'Адрес отправителя'
        verbose_name_plural = 'Адреса отправителей'


class AdressRecipient(models.Model):
    city = models.CharField('Город', max_length=64)
    street = models.CharField('Улица', max_length=64)
    house = models.CharField('Дом', max_length=25)
    flat = models.CharField('Квартира', max_length=4)

    def __str__(self) -> str:
        return f"{self.id} {self.city} {self.street} {self.house} {self.flat}"
    class Meta:
        verbose_name = 'Адрес получателя'
        verbose_name_plural = 'Адреса получателей'


class Route(models.Model):
    adress_Sender = models.ForeignKey(
        'AdressSender', verbose_name='Адрес отправителя', on_delete=models.RESTRICT, related_name='routes_sender')
    adress_Recipient = models.ForeignKey(
        'AdressRecipient', verbose_name='Адрес получателя', on_delete=models.RESTRICT, related_name='routes_recipient')

    def __str__(self) -> str:
        return f"{self.id} {self.adress_Sender} {self.adress_Recipient}"
    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

# class LoadersList(models.Model):
#     loader = models.ForeignKey(
#         USER, verbose_name='Грузчик', on_delete=models.RESTRICT, related_name='loaders')
#     contract = models.ForeignKey(
#         'Contract', verbose_name='Заказ', on_delete=models.RESTRICT, related_name='loaders')
