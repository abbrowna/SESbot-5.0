import time
import urllib.request as request
import numpy as np

timetotal = 0
for i in range(10):
    before = time.time()
    resp = request.urlopen('http://192.168.0.124/photo')
    #response = request.urlopen('http://192.168.0.120:8080/shot.jpg')
    image = np.asarray(bytearray(resp.read()), dtype = "uint8")
    #image = cv2.imdecode(image,cv2.IMREAD_COLOR)
    elapsed = time.time()-before
    timetotal = timetotal+elapsed

print ('average using urllib2 {0}'.format(timetotal/10))

#timetotal = 0
#for i in range(10):
#    before = time.time()
#    response = urllib.urlopen('http://192.168.0.124/photo')
#    #response = urllib.urlopen('http://192.168.0.120:8080/shot.jpg')

#    if response:
#        print ('image received')
#    elapsed = time.time()-before
#    timetotal = timetotal+elapsed

#print ('total using urllib2 {0}'.format(timetotal/10))


