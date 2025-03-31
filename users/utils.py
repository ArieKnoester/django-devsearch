from django.db.models import Q
from .models import Profile, Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_profiles(request, profiles, per_page):
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list=profiles, per_page=per_page)
    page_range = paginator.get_elided_page_range(number=page, on_each_side=2)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)

    return page_range, profiles


# Instructor's way of limiting the number of page buttons displayed
# if the number of pages is large. While this does work, it might be
# better to use Paginator.get_elided_page_range instead.
# https://docs.djangoproject.com/en/5.1/ref/paginator/#django.core.paginator.Paginator.get_elided_page_range
def instructor_paginate_profiles(request, profiles, results):
    """
    Creates a rolling window of buttons displayed in pagination. Max 10

    For example, if there are 20 pages of profiles and the user is on
    the 6th page of profiles, display page buttons from 2 through 11.
    """
    page = request.GET.get('page')
    paginator = Paginator(object_list=profiles, per_page=results)

    try:
        profiles = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, profiles


def search_profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # Instructor for the course  did it this way
    # skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__name__icontains=search_query) # my version
        # Q(skill__in=skills) # instructor code
    )

    return profiles, search_query