from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class ArticlePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ArticleSinglePage',
        related_name='article_tagged_items',
        on_delete=models.CASCADE,
    )


class ArticleListPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # all_articles = self.get_children().live().order_by('-first_published_at')
        all_articles = ArticleSinglePage.objects.live().order_by('-first_published_at')

        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            all_articles = all_articles.filter(tags__slug__in=[tags])

        paginator = Paginator(all_articles, 6)
        page = request.GET.get('page', 1)

        try:
            article_pages = paginator.page(page)
        except PageNotAnInteger:
            article_pages = paginator.page(1)
        except EmptyPage:
            article_pages = paginator.page(paginator.num_pages)

        context['article_pages'] = article_pages
        return context


class ArticleSinglePage(Page):
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
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through=ArticlePageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body', classname='full'),
        FieldPanel('tags'),
        ImageChooserPanel('featured_image'),
    ]
