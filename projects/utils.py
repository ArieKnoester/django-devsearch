from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project


def paginate_projects(request, projects, per_page):
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list=projects, per_page=per_page)
    page_range = paginator.get_elided_page_range(number=page, on_each_side=2)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return page_range, projects


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query =  request.GET.get('search_query')

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(tags__name__icontains=search_query)
    )
    return projects, search_query


# NOT USED !!!
# Instructor's way of limiting the number of page buttons displayed
# if the number of pages is large. While this does work, it might be
# better to use Paginator.get_elided_page_range instead. See paginate_projects
# function above.
# https://docs.djangoproject.com/en/5.1/ref/paginator/#django.core.paginator.Paginator.get_elided_page_range
def instructor_paginate_projects(request, projects, results):
    """
    Creates a rolling window of buttons displayed in pagination. Max 10

    For example, if there are 20 pages of projects and the user is on
    the 6th page of projects, display page buttons from 2 through 11.
    """
    page = request.GET.get('page')
    paginator = Paginator(object_list=projects, per_page=results)

    try:
        projects = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, projects
