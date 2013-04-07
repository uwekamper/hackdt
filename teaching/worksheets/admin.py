from django.contrib import admin
from models import *

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)


class OverlordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Overlord, OverlordAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
