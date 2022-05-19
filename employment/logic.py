def update_skills(user, skills):
    """Редактор навыков пользователя"""
    for skill in user.skills.all():
        if skill not in skills:
            user.skills.remove(skill)

    for skill in skills:
        if skill not in user.skills.all():
            user.skills.add(skill)
