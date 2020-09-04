from django.db import models
from lang.models import Snippet
from django.contrib.auth.models import User



class Rating(models.Model):

	CHOICES = [

		('downvote',-1),
		('upvote' , 1)

	]

	snippet = models.ForeignKey(Snippet , on_delete=models.CASCADE , related_name='ratings')
	user    = models.ForeignKey(User , on_delete=models.CASCADE , related_name='ratings')
	date    = models.DateTimeField(auto_now_add=True)
	rating  = models.IntegerField(choices=CHOICES , default=0)


	def __str__(self):

		return self.snippet


