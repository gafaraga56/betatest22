from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Advertisement
from django.core import validators
from django.forms import CharField
import  re

#title = forms.CharField(max_length=64,
  #                     widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
   #                     )
#description = forms.CharField(widget=forms.Textarea(
 #   attrs={"class": "form-control form-control-lg"}
#))
#price = forms.DecimalField(widget=forms.NumberInput(
 #   attrs={"class": "form-control form-control-lg"}
#))
#auction = forms.BooleanField(required=False,
 #                            widget=forms.CheckboxInput({"class": "form-check-input"}))
#image = forms.ImageField(widget=forms.FileInput(
 #   attrs={"class": "form-control form-control-lg"}
#))


# Create the form class.
class AdvertisementForm(ModelForm):
     class Meta:
         model = Advertisement
         fields = ("title", "description", "image", "price", "auction")
     def clean_title(self):
         title = self.cleaned_data['title']
         if title.startswith('?'):
             raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
         return title
     class SlugField(CharField):
         default_validators = [validators.validate_slug]



     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
         self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
         self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
         self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
         self.fields['auction'].widget.attrs['class'] = 'form-check-input'



# Creating a form to add an article.# Creating a form to change an existing article.
article = Advertisement.objects.get(pk=1)

form = AdvertisementForm(instance=article)
