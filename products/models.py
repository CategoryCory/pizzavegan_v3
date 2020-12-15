from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class ProductListPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        product_pages = self.get_children().live().order_by('-first_published_at')
        featured_products = [pg for pg in product_pages if pg.specific.is_featured is True]
        regular_products = [pg for pg in product_pages if pg.specific.is_featured is False]
        context['product_pages'] = featured_products + regular_products
        return context


class ProductSinglePage(Page):
    subtitle = models.CharField(max_length=200, blank=True)
    body = RichTextField(features=[
        'bold',
        'italic',
        'h2',
        'h3',
        'h4',
        'ol',
        'ul',
        'blockquote',
        'hr',
        'link',
        'document-link',
        'image',
        'embed',
    ])
    is_featured = models.BooleanField(default=False)
    related_link = models.URLField(blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body', classname='full'),
        FieldPanel('is_featured'),
        FieldPanel('related_link'),
        ImageChooserPanel('featured_image'),
    ]
