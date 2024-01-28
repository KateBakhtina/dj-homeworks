from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if is_main:
                counter += 1
            if counter > 1:
                raise ValidationError('Основным может быть только один раздел')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    inlines = (ScopeInline,)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    pass




