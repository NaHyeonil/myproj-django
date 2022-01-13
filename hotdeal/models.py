
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Hotdeal(TimestampedModel):
    mallname = models.CharField(max_length=10, db_index=True,
                                validators=[
                                 MinLengthValidator(2)], verbose_name="쇼핑몰 이름")
    title = models.CharField(max_length=100, db_index=True, verbose_name="제목")
    price = models.CharField(max_length=100, db_index=True, verbose_name="가격")
    link = models.CharField(max_length=100, db_index=True, verbose_name="링크")
    content = models.TextField(verbose_name="내용")
    photo = models.ImageField(blank=True)
