from django.core.paginator import Paginator


def get_paginator(request, items, num=10):
    """Пангинация"""
    paginator = Paginator(items, num)
    num_pages = request.GET.get('page')
    return paginator.get_page(num_pages)
