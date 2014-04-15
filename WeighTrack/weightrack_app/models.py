from django.db import models

# Create your models here.

class Batch(models.Model):
	#for tracking batches. Assume expdate in common across batch.
	batchID = models.CharField(max_length=256, unique=True)
	manufacturer = models.CharField(max_length=256)
	expDate = models.DateField(default=None)

	def __unicode__(self):
		return self.manufacturer + " Batch: " + self.manufacturer

class TaggedItem(models.Model):
	#primary identification
	name = models.CharField(max_length=256)
	tag = models.CharField(max_length=256, unique=True)
	batch = models.ForeignKey(Batch)

	#app-related metadata
	container = models.CharField(max_length=256)
	fullWeight = models.IntegerField()
	emptyWeight = models.IntegerField()
	saleDate = models.DateField(default=None)
	#store product url for reordering
	url = models.URLField()

	def __unicode__(self):
		return self.name