

# Register your models here.from django.contrib import admin
from django.contrib import admin
from .models import Skill, Note, StudyTask

admin.site.register(Skill)
admin.site.register(Note)
admin.site.register(StudyTask)