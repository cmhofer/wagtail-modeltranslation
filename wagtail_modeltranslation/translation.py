# coding utf-8

from modeltranslation.decorators import register
from .translator import WagtailTranslationOptions
from wagtail.wagtailcore.models import Page


@register(Page)
class PageTR(WagtailTranslationOptions):
    pass
