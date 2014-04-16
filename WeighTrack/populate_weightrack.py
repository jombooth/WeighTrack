import os
import datetime
def populate():
	bat1 = add_batch(142353, "Hood Farms")
	bat2 = add_batch(101010, "Garlic Valley")

	ti1 = add_TI(bat2, "Garlic Bread", "00110011", "bag", 200, 120, 200, datetime.datetime.now(), "fake.com")
	ti2 = add_TI(bat1, "Milk", "11010111", "bag", 500, 100, 500, datetime.datetime.now(), "milkshake.com")

	s1 = add_scale("aardvark1230", "**" + "00110011" + "**" + "11010111", "**" + "00110011" + "**" + "11010111")

	WT = add_WT("Jo", "cheese", "aardvark1230")


def add_batch(bID, manuf, exp = datetime.datetime.now()+datetime.timedelta(days=7)):
	b = Batch.objects.get_or_create(batchID=bID, manufacturer=manuf, expDate=exp)[0]
	return b

def add_TI(bat, itemname, itemtag, bottle, full, empty, current, sale, itemurl):
	ti = TaggedItem.objects.get_or_create(batch=bat, name=itemname, tag=itemtag, container=bottle, fullWeight=full, emptyWeight=empty, currentLevel=current, saleDate=sale, url=itemurl)[0]
	return ti

def add_scale(sID, checkedin, monitored):
	sc = Scale.objects.get_or_create(scaleID=sID, checkedInItems=checkedin, monitItems=monitored)[0]
	return sc

def add_WT(userID, mypass, myscales):
	wt = WeighTrackR.objects.get_or_create(user=userID, passHash=mypass, scales=myscales)[0]
	return wt

if __name__ == '__main__':
    print "Starting wt_db population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeighTrack.settings')
    from weightrack_app.models import Batch, TaggedItem, Scale, WeighTrackR
    populate()