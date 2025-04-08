from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .utils import search_profiles, paginate_profiles
from .models import Profile, Message
from .forms import CustomUserCreationForm, ProfileForm, SkillForm


def login_user(request):

    if request.user.is_authenticated:
        return redirect('all-profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, message="Username does not exist.")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect(request.GET.get('next', 'all-profiles'))
            else:
                messages.error(request, message="Username or password is incorrect.")

    return render(request, template_name='users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, message="Logout successful.")
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, message='User account was created!')
            login(request, user=user)
            return redirect('edit-account')
        else:
            messages.error(request, message='Please resolve the errors below.')

    context = {'page': page, 'form': form}
    return render(request, template_name='users/login_register.html', context=context)


def all_profiles(request):
    profiles, search_query = search_profiles(request)
    page_range, profiles = paginate_profiles(request, profiles, per_page=6)

    context = {
        'profiles': profiles,
        'search_query': search_query,
        'page_range': page_range,
    }
    return render(
        request,
        template_name='users/profiles.html',
        context=context
    )


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    # Get related skills and put into separate lists
    # by whether the skill's 'description' field has a value.
    # These two lists will be used in the user-profile.html
    # template.
    description_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {
        'profile': profile,
        'description_skills': description_skills,
        'other_skills': other_skills
    }
    return render(
        request,
        template_name='users/user-profile.html',
        context=context
    )


@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects
    }
    return render(request, template_name='users/account.html', context=context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    context = {'form': form}

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, message='Account was updated successfully.')
            return redirect('account')

    return render(request, template_name='users/profile_form.html', context=context)


@login_required(login_url='login')
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()
    context = {'form': form}

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, message='Skill was created successfully.')
            return redirect('account')

    return render(request, template_name='users/skill_form.html', context=context)


@login_required(login_url='login')
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    context = {'form': form}

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            skill.save()
            messages.success(request, message='Skill was updated successfully.')
            return redirect('account')

    return render(request, template_name='users/skill_form.html', context=context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill_to_delete = profile.skill_set.get(id=pk)
    context = {
        'object': skill_to_delete,
    }

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill_to_delete.delete()
            messages.success(request, message='Skill was deleted successfully.')
            return redirect('account')

    return render(request, template_name='delete-template.html', context=context)


@login_required(login_url='login')
def inbox(request):
    profile =  request.user.profile
    # messages is the 'related_name' we gave the foreign key in the Messages model
    # this is why we use 'profile.messages.all()' instead of profile.messages_set.all()
    profile_messages = profile.messages.all()
    unread_count = profile_messages.filter(is_read=False).count()
    context = {
        'profile_messages': profile_messages,
        'unread_count': unread_count
    }

    return render(request, template_name='users/inbox.html', context=context)