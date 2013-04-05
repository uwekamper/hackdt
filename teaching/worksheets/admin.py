from django.contrib import admin
from models import *

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)

class StudentGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(StudentGroup, StudentGroupAdmin)