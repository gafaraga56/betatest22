from django.contrib import admin
from django.db import models
from django.utils import timezone, html
from django.contrib.auth import  get_user_model


User = get_user_model()

class Advertisement(models.Model):
    image = models.ImageField("Изображение", upload_to="media")
    title = models.CharField("Заговолок", max_length=180)
    description = models.TextField("Описание")
    authors = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField("Цена")
    auction = models.BooleanField("Торг", default=False)

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return html.format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y / %H:%M:%S")

    @admin.display(description='дата последнего обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return html.format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_at.strftime("%d.%m.%Y / %H:%M:%S")
    @admin.display(description='фото')
    def get_html_image(self):
        if self.image:
            return html.format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )


    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title})>'




