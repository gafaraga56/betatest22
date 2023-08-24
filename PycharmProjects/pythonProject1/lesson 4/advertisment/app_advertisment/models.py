from django.db import models
class Advertisement(models.Model):
    title = models.CharField("Заговолок", max_length=180)
    text = models.TextField("Описание")
    authors = models.CharField("автор",max_length=64)
    date = models.DateField("дата", auto_now_add=True)
#    class Meta:
#        db_table = 'advertisements' #переименовал app_advertisement_advertisement в advertisement
    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'