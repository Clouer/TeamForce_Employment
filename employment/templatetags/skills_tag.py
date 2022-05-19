from django import template
from employment.models import Skill

register = template.Library()


@register.simple_tag()
def get_skills():
    """Вывод всех навыков"""
    return Skill.objects.all()
