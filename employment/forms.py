from django import forms
from django.forms import CheckboxSelectMultiple

from .models import User, Skill


class SignUpForm(forms.ModelForm):
    """Форма регистрации"""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class ProfileForm(forms.ModelForm):
    """Форма личного кабинета"""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'languages', 'hobbies', 'skills']

    # Many to Many поле в форму
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=CheckboxSelectMultiple
    )


class SkillForm(forms.ModelForm):
    """Форма навыка"""

    class Meta:
        model = Skill
        fields = ['tag', 'name']
