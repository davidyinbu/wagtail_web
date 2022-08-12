"""blocks for the web"""
from django.db import models
from wagtail.core import blocks


class TitleAndText(blocks.StructBlock):
    """Title and text"""

    title = blocks.CharBlock(required=True, help_text="your title")
    text = blocks.TextBlock(required=False, help_text="additional text")

    class Meta:  # no qa
        templates = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class RichTextBlock(blocks.RichTextBlock):
    """rich text with all features"""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"
