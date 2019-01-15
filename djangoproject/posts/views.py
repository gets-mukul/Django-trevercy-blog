# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from models import Posts
# Create your views here.

posts = Posts.objects.all()[:10]

context = {
	'title' : 'Latest Posts',
	'posts': posts
}

def index(request):
	return render(request, 'posts/index.html', context)

def details(request, id):
	post = Posts.objects.get(id=id)
	context = {
		'post': post
	}
	return render(request, 'posts/details.html', context)
