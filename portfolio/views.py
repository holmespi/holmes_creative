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
	'before_link': '',
	'page_title': ' | Home',
	'long_desc': 'Providing creative design and hype solutions. The displayed projects has been selected from various work done for clients over my career.',
	}
	context_dict['posts'] = posts
	return render_to_response('home.html', context_dict, context)

def sketchbook(request):
	context = RequestContext(request)

	posts = item.objects.filter(sketch=True).order_by('-id')
	context_dict = {
	'link': "",
	'link_title': "HOME ",
	'after_link': '-> SKETCHBOOK',
	'page_title': ' | Sketchbook',
	'long_desc': 'Here are some doodles from my sketchbook.'
	}
	context_dict['posts'] = posts
	return render_to_response('home.html', context_dict, context)
