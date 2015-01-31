from django.db import models
from users.models import User
# Create your models here.

class Forums( models.Model ):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=150)
	topic_count = models.BigIntegerField()
	post_count = models.BigIntegerField()
	position = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Threads( models.Model ):
	sticky = models.BooleanField( default=False)
	forum = models.ForeignKey(Forums)
	user = models.ForeignKey(User)
	last_post_id = models.IntegerField( default = 0 )
	title = models.CharField(max_length=150)
	hits = models.BigIntegerField()
	post_count = models.BigIntegerField()
	locked = models.BooleanField( default = False )
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Post( models.Model ):
	user = models.ForeignKey(User)
	thread = models.ForeignKey(Threads)
	forum = models.ForeignKey(Forums)
	content = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
