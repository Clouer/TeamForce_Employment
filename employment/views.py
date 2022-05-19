from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from employment.forms import SignUpForm, ProfileForm, SkillForm
from .logic import update_skills
from .models import User


class SignInView(LoginView):
    """Логин"""
    redirect_authenticated_user = True
    template_name = 'employment/login.html'


class SignUpView(View):
    """Регистрация"""

    def get(self, request):
        form = SignUpForm()
        return render(request, 'employment/register.html', context={'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            User.objects.create_user(**cleaned_form)
        return redirect(reverse('login'))


class UsersView(ListView):
    """Список сотрудников - главная страница"""
    model = User
    queryset = User.objects.all()


class ProfileView(View):
    """Личный кабинет"""

    def get(self, request):
        user_form = ProfileForm()
        skill_form = SkillForm()
        return render(request, 'employment/profile.html', context={'form': user_form, 'skill_form': skill_form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(pk=request.user.id)
            cleaned_data = form.cleaned_data
            skills = cleaned_data.pop('skills')
            user.update(**cleaned_data)
            update_skills(request.user, skills)

        return redirect(reverse('profile'))


class AddSkilView(View):
    """Добавить новый навык"""

    def post(self, request):
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save()
            request.user.skills.add(skill)
        return redirect(reverse('profile'))
