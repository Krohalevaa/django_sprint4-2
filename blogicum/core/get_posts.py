from django.utils import timezone
from django.db.models import Count


def get_posts(post_objects):
    """Посты из базы данных"""
    return post_objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).annotate(comment_count=Count('comments'))
