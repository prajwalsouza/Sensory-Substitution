
import cv2
import urllib2
import numpy as np
import sys

# Stream Video with OpenCV from an Android running IP Webcam (https://play.google.com/store/apps/details?id=com.pas.webcam)
# Code Adopted from http://stackoverflow.com/questions/21702477/how-to-parse-mjpeg-http-stream-from-ip-camera

host = "192.168.1.3:8080"
if len(sys.argv)>1:
	host = sys.argv[1]

hoststr = 'http://' + host + '/video'
print 'Streaming ' + hoststr

stream=urllib2.urlopen(hoststr)

bytes=''
while True:
	bytes+=stream.read(1024)
	a = bytes.find('\xff\xd8')
	b = bytes.find('\xff\xd9')
	if a!=-1 and b!=-1:
		jpg = bytes[a:b+2]
		bytes= bytes[b+2:]
		i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_GRAYSCALE)
		# cv2.imshow("camvideo",i)
		print(i[12,22])
		if cv2.waitKey(1) ==27:
			exit(0)


