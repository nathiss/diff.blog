from django.contrib.sitemaps import Sitemap
from app.models import Post, UserProfile, Topic, Search
from app.json_views.search import do_search

import datetime

def get_changefreq_from_last_updated_time(updated_on):
    today = datetime.datetime.now(datetime.timezone.utc)
    seconds_since_last_updated = (today - updated_on).total_seconds()

    if seconds_since_last_updated <= 60 * 60:
        return "hourly"
    if seconds_since_last_updated <= 60 * 60 * 24:
        return "daily"
    if seconds_since_last_updated <= 60 * 60 * 24 * 7:
        return "weekly"
    return "monthly"

class TopicSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Topic.objects.filter()

    def lastmod(self, topic):
        last_post = Post.objects.filter(topics=topic).order_by('-updated_on').first()
        if last_post is not None:
            return last_post.updated_on
        return None

    def changefreq(self, topic):
        last_post = Post.objects.filter(topics=topic).order_by('-updated_on').first()

        if last_post is None:
            return "monthly"

        return get_changefreq_from_last_updated_time(last_post.updated_on)

class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter()

    def lastmod(self, obj):
        return obj.updated_on

class UserSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return UserProfile.objects.filter()

    def lastmod(self, profile):
        last_post = Post.objects.filter(profile=profile).order_by('-updated_on').first()
        if last_post is not None:
            return last_post.updated_on
        return None

    def changefreq(self, profile):
        last_post = Post.objects.filter(profile=profile).order_by('-updated_on').first()

        if last_post is None:
            return "monthly"

        return get_changefreq_from_last_updated_time(last_post.updated_on)

class SearchSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Search.objects.filter().exclude(query__exact="")

    def lastmod(self, search):
        posts = do_search(search.query, 1)
        if posts:
            return posts[0].updated_on
        return None

    def changefreq(self, search):
        posts = do_search(search.query, 1)
        if posts:
            return get_changefreq_from_last_updated_time(posts[0].updated_on)
        return "monthly"

sitemaps = {
    "post": PostSitemap,
    "user": UserSitemap,
    "tag": TopicSitemap,
    "search": SearchSitemap
}
