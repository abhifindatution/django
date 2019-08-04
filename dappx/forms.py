#dappx/forms.py

from django import forms
from dappx.models import YogaStudentInfo,MusicStudentInfo,DanceStudentInfo,TutorQuestion,AcademicStudentInfo
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import backends, get_user_model
from django.db.models import Q


from django.contrib.auth.models import User


from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings

###################################
"""  DEFAULT SETTINGS + ALIAS   """
###################################


try:
    am = settings.AUTHENTICATION_METHOD
except:
    am = 'both'
try:
    cs = settings.AUTHENTICATION_CASE_SENSITIVE
except:
    cs = 'both'

#####################
"""   EXCEPTIONS  """
#####################


VALID_AM = ['username', 'email', 'both']
VALID_CS = ['username', 'email', 'both', 'none']

if (am not in VALID_AM):
    raise Exception("Invalid value for AUTHENTICATION_METHOD in project "
                    "settings. Use 'username','email', or 'both'.")
if (cs not in VALID_CS):
    raise Exception("Invalid value for AUTHENTICATION_CASE_SENSITIVE in project "
                    "settings. Use 'username','email', 'both' or 'none'.")

############################
"""  OVERRIDDEN METHODS  """
############################


class DualAuthentication(ModelBackend):
    """
    This is a ModelBacked that allows authentication
    with either a username or an email address.
    """

    def authenticate(self, username=None, password=None):
        UserModel = get_user_model()
        try:
            if ((am == 'email') or (am == 'both')):
                if ((cs == 'email') or cs == 'both'):
                    kwargs = {'email': username}
                else:
                    kwargs = {'email__iexact': username}

                user = UserModel.objects.get(**kwargs)
            else:
                raise
        except:
            if ((am == 'username') or (am == 'both')):
                if ((cs == 'username') or cs == 'both'):
                    kwargs = {'username': username}
                else:
                    kwargs = {'username__iexact': username}

                user = UserModel.objects.get(**kwargs)
        finally:
            try:
                if user.check_password(password):
                    return user
            except:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a non-existing user.
                UserModel().set_password(password)
                return None

    def get_user(self, username):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=username)
        except UserModel.DoesNotExist:
            return None

    def get_user(self, username):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=username)
        except UserModel.DoesNotExist:
            return None
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class AcademicStudentInfoForm(forms.ModelForm):
    CHOICES = (('CBSE', 'CBSE'),('ICSE', 'ICSE'),('State Board', 'State Board'),)

    CHOICES2=(('12TH','12TH'),
         ('11TH','11TH'),('10','10TH'),
         ('9','9TH'),('8','8TH'),
         ('7','7TH'),('6','6TH'),)
    ##CHOICES3 = (
	##			('Direct', 'Direct To Tutor'),
     ##           ('WithUs', 'via FindaTutor'),
		##		)##
    CHOICES4=(
				('Morning', 'Morning'),
                ('Afternoon', 'Afternoon'),
				('Evening','Evening'),
				)
    ##CHOICES5=(
	##			('Haryana','Haryana'),
			##	('Uttar pradesh','Uttar pradesh'),
			##	('Uttarakhand','Uttarakhand'),
##
    CHOICES6=(
				('Noida', 'Noida'),
                ('Gurgaon', 'Gurgaon'),
				('New Delhi','New Delhi'),
				('Old Delhi','Old Delhi'),
				('Roorkee','Roorkee'),
				('Haridwar','Haridwar'),
				('Rishikesh','Rishikesh'),
			)
    email=forms.EmailField(widget=forms.TextInput(attrs={'required': True}))
    Your_Board = forms.ChoiceField(choices=CHOICES)
    Subject_You_want_to_study = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    city = forms.ChoiceField(choices=CHOICES6)
    Preferred_time = forms.ChoiceField(choices=CHOICES4)
    #Fee_Payment = forms.ChoiceField(choices=CHOICES3)
    Your_class = forms.ChoiceField(choices=CHOICES2)
    class Meta():
        model = AcademicStudentInfo
        fields = ('email','profile_pic','city','Your_Board','Your_class','Language_You_Speak',
                  'Subject_You_want_to_study',
                   'Preferred_time', 'Stream')

class YogaStudentInfoForm(forms.ModelForm):
    
	CHOICES4=(
				('Morning', 'Morning'),
                ('Afternoon', 'Afternoon'),
				('Evening','Evening'),
				)
	CHOICES6=(
				('Noida', 'Noida'),
                ('Gurgaon', 'Gurgaon'),
				('New Delhi','New Delhi'),
				('Old Delhi','Old Delhi'),
				('Roorkee','Roorkee'),
				('Haridwar','Haridwar'),
				('Rishikesh','Rishikesh'),
			)
	email=forms.EmailField(widget=forms.TextInput(attrs={'required': True}))
	What_Yoga_form_want_to_learn= forms.CharField(widget=forms.TextInput(attrs={'required': True}))
	city = forms.ChoiceField(choices=CHOICES6)
	Preferred_time = forms.ChoiceField(choices=CHOICES4)
	class Meta():
		model = YogaStudentInfo
		fields = ('email','city',
                  'What_Yoga_form_want_to_learn',
                   'Preferred_time')
    

class MusicStudentInfoForm(forms.ModelForm):
    
	CHOICES4=(
				('Morning', 'Morning'),
                ('Afternoon', 'Afternoon'),
				('Evening','Evening'),
				)
	CHOICES6=(
				('Noida', 'Noida'),
                ('Gurgaon', 'Gurgaon'),
				('New Delhi','New Delhi'),
				('Old Delhi','Old Delhi'),
				('Roorkee','Roorkee'),
				('Haridwar','Haridwar'),
				('Rishikesh','Rishikesh'),
			)
	CHOICES7=(
				('Singing', 'Classical singing'),
                ('Guitar', 'Guitar'),
				('Drum','Drum'),
				('Violin','Violin'),
				('others','others'),
				
			)
	email=forms.EmailField(widget=forms.TextInput(attrs={'required': True}))
	What_would_you_like_to_learn= forms.ChoiceField(choices=CHOICES7)
	city = forms.ChoiceField(choices=CHOICES6)
	Preferred_time = forms.ChoiceField(choices=CHOICES4)
	class Meta():
		model = MusicStudentInfo
		fields = ('email','city',
                  'What_would_you_like_to_learn',
                   'Preferred_time')
class DanceStudentInfoForm(forms.ModelForm):
    
	CHOICES4=(
				('Morning', 'Morning'),
                ('Afternoon', 'Afternoon'),
				('Evening','Evening'),
				)
	CHOICES6=(
				('Noida', 'Noida'),
                ('Gurgaon', 'Gurgaon'),
				('New Delhi','New Delhi'),
				('Old Delhi','Old Delhi'),
				('Roorkee','Roorkee'),
				('Haridwar','Haridwar'),
				('Rishikesh','Rishikesh'),
			)
	CHOICES7=(
				('Western', 'Western'),
                ('Classical', 'classical'),
			)
	email=forms.EmailField(widget=forms.TextInput(attrs={'required': True}))
	Danceform_You_want_to_learn = forms.ChoiceField(choices=CHOICES7)
	city = forms.ChoiceField(choices=CHOICES6)
	Preferred_time = forms.ChoiceField(choices=CHOICES4)
	class Meta():
		model = DanceStudentInfo
		fields = ('email','city',
                  'Danceform_You_want_to_learn',
                   'Preferred_time')




class TutorQuestionForm(forms.ModelForm):
    CHOICES2 = (('0-3 Months', '0-3 Months'),('3-6 months','3-6 months'),('6-12 months','6-12 months'),
                ('Longer than a year','Longer than a year'))
    What_is_the_minimum_tenure_you_wish_to_teach_with_us= forms.ChoiceField(choices=CHOICES2)

    
    Options1=(('English','English'),
              ('Hindi','Hindi'),
              ('Punjabi','Punjabi'),
              ('Kannada','Kannada'),)
    What_languages_you_speak= forms.ChoiceField(choices=Options1)
    #forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect())
    
    OPTIONS2 = (
                ("1-3", "1st-3rd Class"),
                ("4-5", "4th-5th Class"),
                ("6-8", "6th-8th Class"),
                ("9-10","9th-10th Class"),
                ("11-12","11th-12th Class")
                )

    OPTIONS4= (
				('Morning', 'Morning'),
                ('Afternoon', 'Afternoon'),
				('Evening','Evening'),
				)
    OPTIONS5= (
				('Haryana','Haryana'),
				('Uttar pradesh','Uttar pradesh'),
				('Uttarakhand','Uttarakhand')
			  )
    OPTIONS6=(
				('Noida', 'Noida'),
                ('Gurgaon', 'Gurgaon'),
				('New Delhi','New Delhi'),
				('Old Delhi','Old Delhi'),
				('Roorkee','Roorkee'),
				('Haridwar','Haridwar'),
				('Rishikesh','Rishikesh')
				
			 )
    OPTIONS7=(
				('Mathematics', 'Mathematics'),
                ('Physics', 'Physics'),
				('Chemistry','Chemistry'),
				('Biology','Biology'),
				('English','English'),
				('Hindi','Hindi'),
				('History','History'),
				('Civics','Civics'),
				('Geography','Geography'),
				('Sanskrit','Sanskrit'),
				('Accounts','Accounts'),
				('Economics','Economics'),
				('Other','Other'),
				
			 )
    OPTIONS9=(
				('Academics', 'Academics'),
                ('Yoga Teacher', 'Yoga Teacher'),
				('Music Teacher','Music Teacher'),
				('Dance Teacher','Dance Teacher'),
				
				
			 )
				
    Level_of_targeted_students = forms.MultipleChoiceField(choices=OPTIONS2,initial='0',
            widget=forms.CheckboxSelectMultiple(),
            required=True,
            label='Level of targeted students',
        )
    email=forms.EmailField(widget=forms.TextInput(attrs={'required': True}))
    state = forms.ChoiceField(choices=OPTIONS5)
    city = forms.ChoiceField(choices=OPTIONS6)
    domain = forms.ChoiceField(choices=OPTIONS9)
    Subjects_you_wish_to_teach = forms.ChoiceField(choices=OPTIONS7)
    Preferred_time=forms.ChoiceField(choices=OPTIONS4)
    Give_us_a_short_description_about_yourself = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    class Meta():
        model = TutorQuestion
        fields = ('email','profile_pic','Highest_degree','Upload_certificate','city','state','Subjects_you_wish_to_teach',
                  'What_is_the_minimum_tenure_you_wish_to_teach_with_us','What_languages_you_speak',
                  'Give_us_a_short_description_about_yourself','Level_of_targeted_students',
                  'Prior_teaching_experience','Preferred_time','Payment_expectation_per_hour',
                  'what_are_your_expectations_from_findatution')

'''class TutionPointRegisterForm(forms.ModelForm):
    CHOICES3 = (('0-3 Months', '0-3 Months'), ('3-6 months', '3-6 months'), ('6-12 months', '6-12 months'),
                ('Longer than a year', 'Longer than a year'))
    What_is_the_minimum_time_you_wish_to_be_with_us = forms.ChoiceField(choices=CHOICES3)

    Options3 = (('English', 'English'),
                ('Hindi', 'Hindi'),
                ('Punjabi', 'Punjabi'),
                ('Kannada', 'Kannada'),)
    # forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect())
    What_languages_your_teachers_know = forms.ChoiceField(choices=Options3)
    OPTIONS4 = (
        ("1-3", "1st-3rd Class"),
        ("4-5", "4th-5th Class"),
        ("6-8", "6th-8th Class"),
        ("9-10", "9th-10th Class"),
        ("11-12", "11th-12th Class")
    )
    OPTIONS5= (
				('Haryana','Haryana'),
				('Uttar pradesh','Uttar pradesh'),
				('Uttarakhand','Uttarakhand')
			  )
    OPTIONS6=(
				('Noida', 'Noida'),
                ('Gurgaon', 'Gurgaon'),
				('New Delhi','New Delhi'),
				('Old Delhi','Old Delhi'),
				('Roorkee','Roorkee'),
				('Haridwar','Haridwar'),
				('Rishikesh','Rishikesh')
				
			 )
    OPTIONS7=(
				('Mathematics', 'Mathematics'),
                ('Physics', 'Physics'),
				('Chemistry','Chemistry'),
				('Biology','Biology'),
				('English','English'),
				('Hindi','Hindi'),
				('History','History'),
				('Civics','Civics'),
				('Geography','Geography'),
				('Sanskrit','Sanskrit'),
				('Accounts','Accounts'),
				('Economics','Economics'),
				('Other','Other'),
				
			 )
    Level_of_target_students = forms.MultipleChoiceField(choices=OPTIONS4,initial='0',
            widget=forms.CheckboxSelectMultiple(),
            required=True,
            label='Level of targeted students',
        )
    
    email=forms.EmailField(widget=forms.TextInput(attrs={'required': True}))
    state = forms.ChoiceField(choices=OPTIONS5)
    city = forms.ChoiceField(choices=OPTIONS6)
    Subjects_you_teach=forms.ChoiceField(choices=OPTIONS7)
    
    class Meta():
        model = TutionPointRegister
        fields = ( 'email','state', 'city', 'Subjects_you_teach'
                  , 'What_is_the_minimum_time_you_wish_to_be_with_us', 'What_languages_your_teachers_know'
                  , 'Give_us_a_short_description_about_your_institute', 'Level_of_target_students', 'Your_Specialities'
                  , 'How_old_is_your_institute',  'what_are_your_expectations_from_findatution'
                  )
'''


