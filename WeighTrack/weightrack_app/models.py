from django.db import models

# Create your models here.

'''class Batch(models.Model):
	#for tracking batches. Assume expdate in common across batch.
	batchID = models.CharField(max_length=256, unique=True)
	manufacturer = models.CharField(max_length=256)
	expDate = models.DateField(default=None)

	def __unicode__(self):
		return self.batchID + " by manufacturer: " + self.manufacturer'''

class TaggedItem(models.Model):
	#primary identification
	name = models.CharField(max_length=256)
	tag = models.CharField(max_length=256, unique=True)
	#batch = models.ForeignKey(Batch)

	#app-related metadata
	container = models.CharField(max_length=256)
	fullWeight = models.IntegerField()
	emptyWeight = models.IntegerField()
	currWeight = models.IntegerField()
	saleDate = models.DateField(default=None)

	#store product url for reordering
	url = models.URLField()

	def __unicode__(self):
		return self.name +' tag '+ self.tag +' currWeight ' + str(self.currWeight)

class Scale(models.Model):
	wt_id = models.CharField(max_length=256)
	rfid_l = models.CharField(max_length=2048)
	rfid_r = models.CharField(max_length=2048)
	weight = models.IntegerField()
	rfid_l_old = models.CharField(max_length=2048)
	rfid_r_old = models.CharField(max_length=2048)
	weight_old = models.IntegerField()

	def __unicode__(self):
		return self.wt_id +' left '+ self.rfid_l +' right ' + self.rfid_r + ' weight '+ str(self.weight)
