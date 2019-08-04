# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

# dappx/admin.py

from django.contrib import admin
from dappx.models import TutorQuestion,User,AcademicStudentInfo,MusicStudentInfo,YogaStudentInfo,DanceStudentInfo
# Register your models here.

admin.site.register(AcademicStudentInfo)
admin.site.register(TutorQuestion)
admin.site.register(MusicStudentInfo)
admin.site.register(YogaStudentInfo)
admin.site.register(DanceStudentInfo)






