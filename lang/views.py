from django.shortcuts import render , get_object_or_404
from .models import Language , Tag , Snippet
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib.auth.models import User
from django.db.models import Count



def snippet_list(request):

	snippets = Snippet.objects.all()

	page = request.GET.get('page')
	paginator = Paginator(snippets,20)

	try:

		snippets = paginator.page(page)

	except PageNotAnInteger:

		snippets = paginator.page(1)

	except EmptyPage:

		snippets = paginator.page(paginator.num_pages)


	return render(request , 'snippet_list.html' , {'snippets':snippets,
												   'page':page})



def snippet_detail(request , snippet_id):

	snippet = get_object_or_404(Snippet , id=snippet_id)

	return render(request , 'snippet_detail.html' , {'snippet':snippet})



def language_detail(request , slug):

	language = get_object_or_404(Language , slug=slug)
	snippets = language.snippets.all()

	page = request.GET.get('page')
	paginator = Paginator(snippets,20)

	try:

		snippets = paginator.page(page)

	except PageNotAnInteger:

		snippets = paginator.page(1)

	except EmptyPage:

		snippets = paginator.page(paginator.num_pages)


	return render(request , 'language_detail.html' , {'snippets':snippets,
													  'page':page,
													  'language':language})


def language_list(request):

	languages = Language.objects.all()

	page = request.GET.get('page')
	paginator = Paginator(languages,20)

	try:

		languages = paginator.page(page)

	except PageNotAnInteger:

		languages = paginator.page(1)

	except EmptyPage:

		languages = paginator.page(paginator.num_pages)


	return render(request , 'language_list.html' , {'languages':languages,
													'page':page})





def top_authors(request):


	users = User.objects.annotate(score=Count('snippets')).order_by('score')

	page = request.GET.get('page')
	paginator = Paginator(users,20)

	try:

		users = paginator.page(page)

	except PageNotAnInteger:

		users = paginator.page(1)

	except EmptyPage:

		users = paginator.page(paginator.num_pages)


	return render(request , 'top_authors.html' , {'users':users,
												  'page':page})



def top_languages(request):


	languages = Language.objects.annotate(score=Count('snippets')).order_by('snippets')


	page = request.GET.get('page')
	paginator = Paginator(languages,20)

	try:

		languages = paginator.page(page)

	except PageNotAnInteger:

		languages = paginator.page(1)

	except EmptyPage:

		languages = paginator.page(paginator.num_pages)


	return render(request , 'top_languages.html' , {'languages':languages,
													'page':page})

