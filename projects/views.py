from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm, ReviewForm
from .utils import search_projects, paginate_projects


# Create your views here.
def all_projects_page(request):
    projects, search_query = search_projects(request)
    page_range, projects = paginate_projects(request, projects, per_page=6)

    context = {
        'projects': projects,
        'search_query': search_query,
        'page_range': page_range
    }

    return render(
        request,
        template_name='projects/projects.html',
        context=context
    )


def project_page(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    form = ReviewForm()
    context = {
        'project': project,
        'tags': tags,
        'form': form,
    }

    # Need to update project vote count and ratio
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()

        messages.success(request, message='Your review was successfully submitted.')


    return render(
        request,
        template_name='projects/single-project.html',
        context=context
    )


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    context = {
        'form': form,
        'profile': profile
    }

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    return render(
        request,
        template_name='projects/project-form.html',
        context=context
    )


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form
    }
    return render(
        request,
        template_name='projects/project-form.html',
        context=context
    )


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project_to_delete = profile.project_set.get(id=pk)
    context = {
        'object': project_to_delete,
    }

    if request.method == 'POST':
        project_to_delete.delete()
        return redirect('account')

    return render(
        request,
        template_name='delete-template.html',
        context=context
    )