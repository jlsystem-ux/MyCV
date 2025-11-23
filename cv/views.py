from django.shortcuts import render
from .models import PersonalInfo, Skill, Experience, Education, Certification

def cv_view(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None

    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()

    skills_by_category = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill.name)

    context = {
        'personal_info': personal_info,
        'skills_by_category': skills_by_category,
        'experiences': experiences,
        'education': education,
        'certifications': certifications,
    }

    return render(request, 'cv/cv_template.html', context)
