# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from portfolio.models import item
from portfolio.models import sketch
from portfolio.models import freeLunch

def home(request):
	context = RequestContext(request)

	posts = item.objects.all().order_by('priority')
	context_dict = {
	'link': "sketchbook",
	'link_title': "SKETCHBOOK",
	'after_link': '',
	'link2': "freelunch",
	'link_title2': "FREE LUNCH ",
	'after_link2': '',
	'page_title': ' | Home',
	'long_desc': 'Providing creative design and hype solutions. The displayed projects have been selected from various work done for clients over my career.',
	}
	context_dict['posts'] = posts
	return render_to_response('home.html', context_dict, context)

def sketchbook(request):
	context = RequestContext(request)

	posts = sketch.objects.all().order_by('priority')
	context_dict = {
	'link': "",
	'link_title': "HOME ",
	'after_link': '-> SKETCHBOOK',
	'page_title': ' | Sketchbook',
	'link2': "freelunch",
	'link_title2': "FREE LUNCH ",
	'after_link2': '',
	'long_desc': 'Here are some doodles from my sketchbook.'
	}
	context_dict['posts'] = posts
	return render_to_response('sketchbook.html', context_dict, context)

def freelunch(request):
	context = RequestContext(request)

	posts = freeLunch.objects.all().order_by('priority')
	context_dict = {
	'link': "sketchbook",
	'link_title': "SKETCHBOOK",
	'after_link': '',
	'link2': "",
	'link_title2': "HOME ",
	'after_link2': '-> FREE LUNCH',
	'page_title': ' | Free Lunch',
	'long_desc': 'Here are some totally free creative commons resources I am providing for any one who finds use in them.  No restrictions on use but consider making a donation.'
	}
	context_dict['posts'] = posts
	return render_to_response('freelunch.html', context_dict, context)

