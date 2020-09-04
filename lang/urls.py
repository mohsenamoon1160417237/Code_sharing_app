from django.urls import path
from . import views


urlpatterns = [

	path('' , views.snippet_list , name='snippet_list'),
	path('snippet/<int:snippet_id>/' , views.snippet_detail , name='snippet_detail'),
	path('language/<slug:slug>/' , views.language_detail , name='language_detail'),
	path('languages/' , views.language_list , name='language_list'),
	path('top_authors/' , views.top_authors , name='top_authors'),
	path('top_languages/' , views.top_languages , name='top_languages'),

]