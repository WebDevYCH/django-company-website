
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from django.conf.urls import url
from werobot.contrib.django import make_view
from accounts import views

from django.contrib.sitemaps.views import sitemap
from agrosite.sitemap import StaticViewSitemap, ArticleSiteMap, CategorySiteMap, TagSiteMap, UserSiteMap
from agrosite.feeds import AgrositeFeed
from django.views.decorators.cache import cache_page
import xadmin
xadmin.autodiscover()


sitemaps = {
    'blog': ArticleSiteMap,
    'Category': CategorySiteMap,
    'Tag': TagSiteMap,
    'User': UserSiteMap,
    'static': StaticViewSitemap
}

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'
handle403 = 'blog.views.permission_denied_view'

urlpatterns = [
    # add your own patterns here
    path('admin/', xadmin.site.urls, name="admin"),
    path('mdeditor/', include('mdeditor.urls')),
    path('cookies/', include('cookie_consent.urls')),
    path('', include('notice.urls')),
    path('', include('myzone.urls')),
    path('', include('home.urls')),
    path('', include('contactus.urls')),
    path('', include('about.urls')),
    path('', include('careers.urls')),
    path('', include('services.urls')),
    path('', include('portfolio.urls')),
    path('', include('blog.urls', namespace='blog')),
    path("likes/", include("likeunlike.urls", namespace="likes")),
    path('summernote/', include('django_summernote.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', AgrositeFeed()),
    path('rss/', AgrositeFeed()),
    path('comment/', include('comment.urls')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('', include('accounts.urls', namespace='account')),
    path('search/', include('haystack.urls'), name='search'),
    path('api/', include([
        path('', include('careers.api.urls')),
    ])),
    
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)