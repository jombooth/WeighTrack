from django.db import models

# Create your models here.

class Batch(models.Model):
	#for tracking batches. Assume expdate in common across batch.
	batchID = models.CharField(max_length=256, unique=True)
	manufacturer = models.CharField(max_length=256)
	expDate = models.DateField(default=None)

	def __unicode__(self):
		return self.batchID + " by manufacturer: " + self.manufacturer

class TaggedItem(models.Model):
	#primary identification
	name = models.CharField(max_length=256)
	tag = models.CharField(max_length=256, unique=True)
	batch = models.ForeignKey(Batch)

	#app-related metadata
	container = models.CharField(max_length=256)
	fullWeight = models.IntegerField()
	emptyWeight = models.IntegerField()
	currentLevel = models.IntegerField()
	saleDate = models.DateField(default=None)
	#store product url for reordering
	url = models.URLField()

	def __unicode__(self):
		return self.name

class Scale(models.Model):
	scaleID = models.CharField(max_length=256)
	checkedInItems = models.CharField(max_length=2048)
	monitItems = models.CharField(max_length=2048)

	def checkIn(self,tag):
		if tag not in checkedInItems:
			checkedInItems += "**" + tag
			return True
		return False

	def monitItem(self,tag):
		if tag not in monitItems:
			monitItems += "**" + tag
			return True
		return False

	def checkout(self,tag):
		if tag in checkedInItems:
			monitItems.replace("**" + tag, '', 1)
			checkedInItems.replace("**" + tag, '', 1)
			return True
		if tag in monitItems:
			monitItems.replace("**" + tag, '', 1)
			return True
		return False


class WeighTrackR(models.Model):
	user = models.CharField(max_length=50)
	passHash = models.CharField(max_length=50)
	scales = models.CharField(max_length=2048)

	def addScale(self,s):
		if s.scaleID not in scales:
			scales += "**" + s.scaleID
			return True
		return False

	def removeScale(self, s):
		if s.scaleID in scales:
			scales.replace("**" + s.scaleID, '', 1)
			return True
		return False
