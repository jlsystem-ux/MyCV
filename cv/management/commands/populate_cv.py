from django.core.management.base import BaseCommand
from cv.models import PersonalInfo, Skill, Experience, Education, Certification

class Command(BaseCommand):
    help = 'Populate the database with CV data'

    def handle(self, *args, **kwargs):
        PersonalInfo.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()

        PersonalInfo.objects.create(
            name="Luis Alberto Arboleda",
            title="Technologist in Systems Analysis | Experienced in Software Development and Quality Assurance (QA)",
            email="arboledaluisalberto28@gmail.com",
            phone="+44 7386 182877",
            location="United Kingdom",
            linkedin="https://www.linkedin.com/in/luis-arboleda-350316181",
            summary="Experienced Systems Analyst with over 3 years in software development and quality assurance (QA). Skilled in adapting to dynamic environments and managing technological projects under both traditional and agile methodologies (Scrum). Proficient in requirements analysis, functional testing, and comprehensive documentation."
        )

        soft_skills = [
            "Teamwork", "Assertive Communication", "Adaptability", "Analytical Thinking"
        ]
        for i, skill in enumerate(soft_skills):
            Skill.objects.create(category='soft', name=skill, order=i)

        methodologies = [
            "Scrum", "Waterfall", "Spiral", "Prototype", "Incremental", "Iterative"
        ]
        for i, skill in enumerate(methodologies):
            Skill.objects.create(category='methodology', name=skill, order=i)

        programming = ["PL/SQL", "PHP", "Python", "Java"]
        for i, skill in enumerate(programming):
            Skill.objects.create(category='programming', name=skill, order=i)

        databases = ["MySQL", "Oracle", "PostgreSQL"]
        for i, skill in enumerate(databases):
            Skill.objects.create(category='database', name=skill, order=i)

        tools = ["NetBeans", "Eclipse", "MySQL", "Oracle SQL", "SoapUI", "pgAdmin", "Git/GitHub", "Mantis"]
        for i, skill in enumerate(tools):
            Skill.objects.create(category='tool', name=skill, order=i)

        Experience.objects.create(
            company="Bank of the West",
            position="Environment Manager",
            start_date="May 2023",
            end_date="Present",
            description="- Managed Flexcube environment, monitored performance, and ensured quality artifacts were up to date.\n- Conducted application training, managed user profiles, and generated performance reports for internal reviews.",
            order=1
        )

        Experience.objects.create(
            company="Qvision – PHC Client",
            position="QA Functional Tester",
            start_date="February 2021",
            end_date="Present",
            description="- Identified test scope, developed test plans, and evaluated test strategies.\n- Managed project documentation, coordinated with cross-functional teams, and presented findings to stakeholders.\n- Conducted functional testing, validated test cases, and prepared technical documentation.",
            order=2
        )

        Experience.objects.create(
            company="Bank of the West",
            position="Functional QA",
            start_date="September 2020",
            end_date="February 2023",
            description="- Developed and evaluated test plans, documented results, and summarized findings for continuous improvement.\n- Collaborated on functional test planning, performed static requirement tests, and managed testing data.\n- Generated reports on test progress, presented results, and led meetings for test plan validation.",
            order=3
        )

        Education.objects.create(
            degree="Technologist in Systems Analysis",
            institution="Servicio Nacional de Aprendizaje (SENA)",
            location="Colombia",
            start_year="2018",
            end_year="2020",
            order=1
        )

        certifications_list = [
            ("Object-Oriented Programming in Java", "2021"),
            ("Fundamentals of Java Programming", "2020"),
            ("Web Development with PHP", ""),
            ("English Certification - DOTWORKS 8", ""),
        ]

        for i, (name, year) in enumerate(certifications_list):
            Certification.objects.create(name=name, year=year, order=i)

        self.stdout.write(self.style.SUCCESS('Successfully populated CV data!'))
