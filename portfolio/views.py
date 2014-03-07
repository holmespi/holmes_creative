# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from portfolio.models import item

def home(request):
	context = RequestContext(request)

	posts = item.objects.filter(sketch=False)
	context_dict = {
	'link': "sketchbook",
	'link_title': "SKETCHBOOK",
	'before_link': ''
	}
	context_dict['posts'] = posts
	return render_to_response('home.html', context_dict, context)

def sketchbook(request):
	context = RequestContext(request)

	posts = item.objects.filter(sketch=True)
	context_dict = {
	'link': "",
	'link_title': "HOME ",
	'after_link': '-> SKETCHBOOK'
	}
	context_dict['posts'] = posts
	return render_to_response('home.html', context_dict, context)
