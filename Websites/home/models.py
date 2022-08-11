from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    """the home page model"""
    templates = "home/home_page.html"

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_sub_title = RichTextField(features=["bold","italic"],null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    linkedin_url = models.URLField(max_length=100,blank=True,null=True)
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null= True,
        blank= True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_sub_title"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
        FieldPanel("linkedin_url"),

    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
