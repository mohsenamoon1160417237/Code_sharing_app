from django.contrib import admin
from .models import Language , Tag , Snippet



@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):

	list_display = ['name' , 'slug' , 'language_code' , 'mime_type']
	list_filter  = ['name' , 'mime_type']


admin.site.register(Tag)


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):

	list_display = ['title' , 'language' , 'author' , 'description' , 'code' , 'pub_date' , 'updated_date']
	list_filter = ['title' , 'language' , 'author' , 'pub_date' , 'updated_date']
	
