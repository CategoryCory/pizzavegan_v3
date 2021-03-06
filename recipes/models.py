from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class RecipeListPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_recipes = self.get_children().live().order_by('-first_published_at')

        paginator = Paginator(all_recipes, 6)
        page = request.GET.get('page', 1)

        try:
            recipe_pages = paginator.page(page)
        except PageNotAnInteger:
            recipe_pages = paginator.page(1)
        except EmptyPage:
            recipe_pages = paginator.page(paginator.num_pages)

        context['recipe_pages'] = recipe_pages
        return context


class RecipeSinglePage(Page):
    provided_by = models.CharField(max_length=200, blank=True)
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
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('provided_by'),
        FieldPanel('body', classname='full'),
        ImageChooserPanel('featured_image'),
    ]
