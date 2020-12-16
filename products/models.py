from django.db import models
from django import forms
from django.http import Http404
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from modelcluster.fields import ParentalKey, ParentalManyToManyField


class ProductListPage(RoutablePageMixin, Page):
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

    @route(r'^category/(?P<category_slug>[-\w]*)/$', name='product_category_view')
    def category_view(self, request, category_slug):
        context = self.get_context(request)
        try:
            category = ProductCategory.objects.get(slug=category_slug)
        except Exception:
            category = None

        if category is None:
            raise Http404('The selected category does not exist.')

        context['product_pages'] = ProductSinglePage.objects.live().public().filter(categories__in=[category]).order_by('-first_published_at')
        return render(request, 'products/product_list_page.html', context)


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
    categories = ParentalManyToManyField('products.ProductCategory', blank=True)
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
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('related_link'),
        ImageChooserPanel('featured_image'),
    ]


@register_snippet
class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
