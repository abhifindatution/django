from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect

from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.conf import settings
from django.contrib import messages


from .forms import ContactForm

# Create your views here.

def index(request) :
    return render(request, 'index.html')
def about(request) :
    return render(request, 'about.html')
def blog(request) :
    return render(request, 'blog.html')
def blogs(request) :
    return render(request, 'blog-single.html')

def courses(request) :
    return render(request, 'courses.html')
def pricing(request) :
    return render(request, 'index.html')
def teacher(request) :
    return render(request, 'teacher.html')



def contact(request):

	if request.method == 'POST':
		name = request.POST['name']
		cemail = request.POST['cemail']
		institute = request.POST['institute']
		message = request.POST['message']
		template = get_template('cnt_template.txt')
		context = {
				'name':name,
				'email':cemail,
				'institute':institute,
				'message':message
		}
		content = template.render(context)

		email = EmailMessage(company, content, cemail,[settings.EMAIL_HOST_USER]) #email to admin
		email.send()
		sub = "From:Find A Tution"
		msg = 'Thank you for contacting us. We will get back to you soon'
		email2 = EmailMessage(sub, msg, settings.EMAIL_HOST_USER,[cemail]) #email to user
		email2.send()
		messages.success(request, 'Your query has been successfully submitted.')
		return redirect('/contact')
		#return HttpResponse("<h2>Success....</h2>")
	context = {}
	return render(request,'contact.html',context)

	
