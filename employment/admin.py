from django.contrib import admin

from employment.models import User, Skill


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass
