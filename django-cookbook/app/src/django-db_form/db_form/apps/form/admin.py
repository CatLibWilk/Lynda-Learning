from django.contrib import admin
from django import forms
from .models import Form, NewsArticle

from .app_settings import ARTICLE_THEME_CHOICES

admin.site.register(Form)

## NewsArticle references from cookbook, delete when have one for existing model
class NewsArticleModelForm(forms.ModelForm):
    theme = forms.ChoiceField(
        label=NewsArticle._meta.get_field("theme").verbose_name,
        choices=ARTICLE_THEME_CHOICES,
        required=not NewsArticle._meta.get_field("theme").blank,
    )
    class Meta:
        fields = "__all__"


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
 form = NewsArticleModelForm