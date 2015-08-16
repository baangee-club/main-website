from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
import json
from django.template.context_processors import csrf
import datetime

def handler404(request):
	return render(request,'error.html',{'heading':'Error 404','content':'Requested URL '+request.build_absolute_uri()+' not found'})

def handler500(request):
	return render(request,'error.html',{'heading':'Error 500','content':'Internal server error.'})

def handler403(request):
	return render(request,'error.html',{'heading':'Error 403','content':'permission denied.'})

def handler400(request):
	return render(request,'error.html',{'heading':'Error 400','content':'Bad request.'})

def index(request):
	data={}
	data.update(csrf(request))
	if request.method=='POST':
		data={}
		form=MessageForm(request.POST)
		if form.is_valid():
			email=form.cleaned_data['email']
			try:
				guest=Guest.objects.get(email=email)
			except:
				guest=Guest(name=form.cleaned_data['name'],email=email)
				guest.save()
			msg=form.save(commit=False)
			msg.author=guest
			msg.save()
			form=MessageForm()
			data['msg']='Thank You '+guest.name+', we have received your message and will responce as requied.'
		else:
			data['errors']=form.errors
			data['msg']='There are errors in form.'
		return HttpResponse(json.dumps(data),content_type="application/json")
	else:
		form=MessageForm()
		data['programmes']=Programme.objects.all()
		data['form']=form
		data['informations']=Information.objects.all().order_by("creation_time")
		data['today']=datetime.date.today()
		data['contact_persons']=ContactPerson.objects.all()
		return render(request,'index.html',data)

'''
		form=MessageForm(request.POST)
		if form.is_valid():
			email=form.cleaned_data['email']
			try:
				guest=Guest.objects.get(email=email)
			except:
				guest=Guest(name=form.cleaned_data['name'],email=email)
				guest.save()
			msg=form.save(commit=False)
			msg.author=guest
			msg.save()
			form=MessageForm()
			data['msg']='Thank You '+guest.name+', we have received your message and will responce as requied.'
'''
def album(request,album_id=0):
	data={}
	album=Album.objects.get(pk=album_id)
	data['album']=album
	return render(request,'album.html',data)

def soach(request):
	data={}
	soach_list=Soach.objects.order_by('creation_time')[::-1]
	data['soach_list']=soach_list
	return render(request,'soach.html',data)

def gallery(request):
	data={}
	albums=Album.objects.all()
	data['albums']=albums
	return render(request,'gallery.html',data)
	
def article_list(request):
	data={}
	data['articles']=Article.objects.order_by('creation_time')[::-1]
	return render(request,'article_list.html',data)
	
def article(request,article_id=1):
	data={}
	data['article']=Article.objects.get(pk=article_id)
	return render(request,'article.html',data)
