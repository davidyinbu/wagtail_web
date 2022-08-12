from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.models import Page,Orderable

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel,InlinePanel,MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePageCarouselImage(Orderable):
    """between 1 to 5"""
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null= True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels =[
        ImageChooserPanel("carousel_image")
    ]


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
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_sub_title"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
            ], heading="Banner Options"),
        FieldPanel("linkedin_url"),
        MultiFieldPanel(
            [
            InlinePanel("carousel_images",min_num=0,max_num=5,label="Image"),
            ],
            heading="Carousel Images"
        )

    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
