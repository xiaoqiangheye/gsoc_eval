#Wei Qiang
#qiangwei@uw.edu


from datetime import datetime
import pytz

#task1
timestamp = 1541962108935000000 // 1000000000
date = datetime.utcfromtimestamp(timestamp)
fmt = '%Y-%m-%d %H:%M:%S %Z'
print date.strftime(fmt)
cern = pytz.timezone('Etc/GMT+2')

cernlocal = pytz.utc.localize(date,is_dst=None).astimezone(cern)

fmt = '%Y-%m-%d %H:%M:%S %Z'
print cernlocal.strftime(fmt)






## task2 and 3
import h5py
import csv
import numpy
import scipy.signal as signal
import matplotlib.pyplot as plt

#open csv File
with open('names.csv', 'wb+') as csvfile:
    writer = csv.writer(csvfile)

    def visitor(name,node):
         if isinstance(node, h5py.Dataset):
            writer.writerow([name])
           # writer.writerow([str(node.dtype), str(node.size), str(node.shape)])
            writer.writerow([])
         else:
            writer.writerow([name])
            writer.writerow([])


    #open h5 file
    f = h5py.File('1541962108935000000_167_838.h5','r')
    f.visititems(visitor)
    imagedata = f['AwakeEventData/XMPP-STREAK/StreakImage/streakImageData'][()]
    height = f['AwakeEventData/XMPP-STREAK/StreakImage/streakImageHeight'][()]
    width = f['AwakeEventData/XMPP-STREAK/StreakImage/streakImageWidth'][()]

    image = numpy.reshape(imagedata,(height[0],width[0]))

    filtered = signal.medfilt(image,3)
    plt.imshow(filtered)
    plt.savefig('image.png')
