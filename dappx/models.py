# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# dappx/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TutorQuestion(models.Model):

    email=models.EmailField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)
    Highest_degree=models.CharField(max_length = 200, blank = True, null = True)
    Upload_certificate=models.ImageField(upload_to = 'Upload_certificate',blank = True)
    state = models.CharField(max_length = 200, blank = True, null = True)
    city = models.CharField(max_length = 200, blank = True, null = True)
    Subjects_you_wish_to_teach = models.CharField(max_length = 200, blank = True, null = True)
    What_is_the_minimum_tenure_you_wish_to_teach_with_us = models.CharField(max_length = 200, blank = True, null = True)
    What_languages_you_speak = models.CharField(max_length=200, blank=True, null = True)
    Give_us_a_short_description_about_yourself = models.TextField(max_length = 500, blank = True, null = True)
    Level_of_targeted_students = models.CharField(max_length = 200, blank = True, null = True)
    #Your_Specialities = models.CharField(max_length = 200, blank = True, null = True)
    Prior_teaching_experience = models.CharField(max_length=200, blank=True, null=True)
    Preferred_time = models.CharField(max_length=200, blank=True, null=True)
    Payment_expectation_per_hour = models.CharField(max_length=200, blank=True, null=True)
    what_are_your_expectations_from_findatution = models.CharField(max_length=300, blank=True, null=True)
    domain = models.CharField(max_length = 200, blank = True, null = True)


class AcademicStudentInfo(models.Model):
    
	email=models.EmailField(max_length=200, blank=True, null=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	#state = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	Your_Board = models.CharField(max_length=200, blank=True, null=True)
	Your_class = models.CharField(max_length=200, blank=True, null=True)
	Language_You_Speak = models.CharField(max_length=200, blank=True, null=True)
	Subject_You_want_to_study = models.CharField(max_length=200, blank=True, null=True)
	Preferred_time = models.CharField(max_length=200, blank=True, null=True)
	Stream = models.CharField(max_length=200, blank=True, null=True)

class YogaStudentInfo(models.Model):
    
	email=models.EmailField(max_length=200, blank=True, null=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	#state = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	What_Yoga_form_want_to_learn= models.CharField(max_length=200, blank=True, null=True) #we will give choices of all or selected yoga asanas.
	Preferred_time = models.CharField(max_length=200, blank=True, null=True)

class MusicStudentInfo(models.Model):
    
	email=models.EmailField(max_length=200, blank=True, null=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	#state = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	What_would_you_like_to_learn = models.CharField(max_length=200, blank=True, null=True) #we will give choices of instrument and classical/western vocals
	Preferred_time = models.CharField(max_length=200, blank=True, null=True)
	
class DanceStudentInfo(models.Model):
    
	email=models.EmailField(max_length=200, blank=True, null=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	#state = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	Danceform_You_want_to_learn = models.CharField(max_length=200, blank=True, null=True) #we will give choices of all type of dance forms
	Preferred_time = models.CharField(max_length=200, blank=True, null=True)
	

'''class TutionPointRegister(models.Model):

    email=models.EmailField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
	#profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    Subjects_you_teach = models.CharField(max_length=200, blank=True, null=True)
    What_is_the_minimum_time_you_wish_to_be_with_us = models.CharField(max_length=200, blank=True, null=True)
    What_languages_your_teachers_know = models.CharField(max_length=200, blank=True, null=True)
    Give_us_a_short_description_about_your_institute = models.TextField(max_length=500, blank=True, null=True)
    Level_of_target_students = models.CharField(max_length=200, blank=True, null=True)
    Your_Specialities = models.CharField(max_length=200, blank=True, null=True)
    How_old_is_your_institute = models.CharField(max_length=200, blank=True, null=True)
	#Fee_for_courses = models.CharField(max_length=200, blank=True, null=True)
    what_are_your_expectations_from_findatution = models.CharField(max_length=300, blank=True, null=True)
'''

def __str__(self):
  return self.user.username
