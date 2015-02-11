from django.db import models

# Models of drScratch

class AnonProject(models.Model):
	identifier = models.IntegerField()	
	date = models.DateField()
	points = models.IntegerField()
	level = models.TextField()

class AnonMastery(models.Model):
	myproject = models.ForeignKey(AnonProject)
	abstraction = models.IntegerField()
	paralel = models.IntegerField()
	logic = models.IntegerField()
	synchronization = models.IntegerField()
	flowcontrol = models.IntegerField()
	interactivity = models.IntegerField()
	representation = models.IntegerField()
	scoring = models.IntegerField()	

class File(models.Model):
    filename = models.CharField(max_length=100)

class Dashboard(models.Model):
	user = models.TextField()
	frelease = models.DateField()

class Project(models.Model):
	name = models.TextField()
	version = models.IntegerField()
	points = models.IntegerField()
	level = models.TextField()
	path = models.TextField()
	fupdate = models.TextField()
	dashboard = models.ForeignKey(Dashboard)
	
class Attribute(models.Model):
	myproject = models.ForeignKey(Project)
	character = models.TextField()
	orientation = models.IntegerField()
	position = models.IntegerField()
	costume = models.IntegerField()
	visibility = models.IntegerField()
	size = models.IntegerField()

class Dead(models.Model):
	myproject = models.ForeignKey(Project)
	character = models.TextField()
	blocks = models.IntegerField()

class Duplicate(models.Model):
	myproject = models.ForeignKey(Project)
	numduplicates = models.IntegerField()

class Sprite(models.Model):
	myproject = models.ForeignKey(Project)
	character = models.TextField()

class Mastery(models.Model):
	myproject = models.ForeignKey(Project)
	abstraction = models.IntegerField()
	paralel = models.IntegerField()
	logic = models.IntegerField()
	synchronization = models.IntegerField()
	flowcontrol = models.IntegerField()
	interactivity = models.IntegerField()
	representation = models.IntegerField()
	points = models.IntegerField()	

class Comment(models.Model):
	user = models.TextField()
	text = models.TextField()
	date = models.DateField()

class Activity(models.Model):
	text = models.TextField()
	date = models.DateField()



	
