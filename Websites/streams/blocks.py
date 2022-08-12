"""blocks for the web"""
from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndText(blocks.StructBlock):
    """Title and text"""
    title = blocks.CharBlock(required=True, help_text="your title")
    text = blocks.TextBlock(required=False, help_text="additional text")

    class Meta:  # no qa
        templates = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class CardBlock(blocks.StructBlock):
    """cards with imgs and buttons"""

    title = blocks.CharBlock(required=True, help_text="your title")  # name of the set of the cards

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=100)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="button url")),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "edit"
        label = "Simpler RichText"


class CTABlock(blocks.StructBlock):
    """simple call to action section"""
    title = blocks.CharBlock(required=False, max_length=50)
    text = blocks.RichTextBlock(required=False, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More',max_length=10)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class RichTextBlock(blocks.RichTextBlock):
    """rich text with all features"""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock):
    """simpler one(limited)"""

    def __init__(
            self,
            required=True,
            help_text=None,
            editor="default",
            features=None,
            validators=(),
            **kwargs,
    ):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link"
        ]

    class Meta:
        template = "streams/simple_richtext_block.html"
        icon = "edit"
        label = "Simpler RichText"
