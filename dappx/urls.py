# dappx/urls.py

from django.conf.urls import url
from dappx import views

# SET THE NAMESPACE!
app_name = 'dappx'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    #url(r'^register1/$',views.register1,name='register1'),
    #url(r'^signup/$',views.signup,name='signup'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^DanceRegister/$',views.danceRegister,name='danceRegister'),#to be updated 
	url(r'^YogaRegister/$',views.yogaRegister,name='yogaRegister'),
	url(r'^MusicRegister/$',views.musicRegister,name='musicRegister'),
	url(r'^TutorRegister/$',views.TutorRegister,name='TutorRegister'),
	
]
