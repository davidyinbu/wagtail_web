from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks

class flexPage(Page):
    "flexible page class"

    templates = "flex/flex_page.html"
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndText()),
            ("full_richText", blocks.RichTextBlock()),
            ("simpler_richText", blocks.SimpleRichTextBlock()),
            ("cards",blocks.CardBlock()),
            ("cta",blocks.CTABlock()),


        ],
        null=True,
        blank=True
    )



    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content")
    ]
    #add stream fields


    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
