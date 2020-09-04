from django.db import models
from django.urls import reverse
from pygments import lexers , formatters , highlight
from django.contrib.auth.models import User
#from markdown import markdown
import datetime



class Language(models.Model):


	name 		  = models.CharField(max_length=100)
	slug 		  = models.SlugField(unique=True , blank=True)
	language_code = models.CharField(max_length=50)
	mime_type     = models.CharField(max_length=100)

	class Meta:

		ordering = ['name']

	def __str__(self):

		return self.name


	def get_absolute_url(self):

		return reverse('lang_detail' , args=[self.slug])

	def get_lexer(self):

		return lexers.get_lexer_by_name(self.language_code)

	def get_absolute_url(self):

		return reverse('language_detail' , args=[self.slug])
		




class Tag(models.Model):

	name 	= models.CharField(max_length=50 , unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return self.name



class Snippet(models.Model):


	title 	 		 = models.CharField(max_length=225)
	language 		 = models.ForeignKey(Language , on_delete=models.CASCADE , related_name='snippets')
	author   		 = models.ForeignKey(User , on_delete=models.CASCADE , related_name='snippets')
	description 	 = models.TextField() #In this field we the user can create objects of Tag class
	description_html = models.TextField(editable=False)
	code             = models.TextField()
	highlighted_code = models.TextField(editable=False)  
	pub_date         = models.DateTimeField(editable=False)
	updated_date     = models.DateTimeField(editable=False)


	def __str__(self):

		return self.title

	class Meta:

		ordering = ['-pub_date']


	def highlight(self):

		return highlight(self.code ,
						 self.language.get_lexer(),
						 formatters.HtmlFormatter(linenos=True)
						 )


	def save(self , force_insert=False , force_update=False):

		if not self.id:

			pub_date = datetime.datetime.now()

		self.updated_date = datetime.datetime.now()
		self.description_html = markdown(self.description)
		self.highlighted_code = self.highlight()

		super(Snippet,self).save(force_insert , force_update)


	def get_absolute_url(self):

		return reverse('snippet_detail' , args=[self.id])



		