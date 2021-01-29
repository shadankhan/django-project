from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from skill_app.models import Profile, Project

# Create your views here.
def project(request):
	project = Project.objects.all()
	return render(request, 'all_project.html',{'project':project})

def index(request):
	return render(request, 'index.html')

def profile(request):
	return render(request, 'profile.html')

def create_profile(request):
	if request.method == 'POST' and request.FILES.iteritems():

		full_name = request.POST.get('first_name','')
		image = request.FILES['image']
		city = request.POST.get('city','')
		gender = request.POST.get('gender','')


		profile, created = Profile.objects.get_or_create(
			user = request.user,
			full_name = full_name,
			image = image,
			city = city,
			gender = gender,

			)
	else:		
		print('Not Created')
		return redirect('/skill_app/c_profile')
	
	return render(request, 'create_profile.html')