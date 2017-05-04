import cv2

print(cv2.__version__)
vidcap = cv2.VideoCapture('http://172.27.196.62:8090/cam1.mjpeg')
success,image = vidcap.read()
count = 0
success = True
while success:
	success,image = vidcap.read()
	print 'Read a new frame: ', success
	cv2.imwrite("static/frame%d.jpg" % count, image)     # save frame as JPEG file
	count += 1
	break

print(cv2.__version__)
vidcap = cv2.VideoCapture('http://172.27.196.62:8090/cam2.mjpeg')
success,image = vidcap.read()
count = 1
success = True
while success:
	success,image = vidcap.read()
	print 'Read a new frame: ', success
	cv2.imwrite("static/frame%d.jpg" % count, image)     # save frame as JPEG file
	count += 1
	break

print(cv2.__version__)
vidcap = cv2.VideoCapture('http://172.27.196.62:8090/cam3.mjpeg')
success,image = vidcap.read()
count = 2
success = True
while success:
	success,image = vidcap.read()
	print 'Read a new frame: ', success
	cv2.imwrite("static/frame%d.jpg" % count, image)     # save frame as JPEG file
	count += 1
	break

print(cv2.__version__)
vidcap = cv2.VideoCapture('http://172.27.253.213:8090/cam1.mjpeg')
success,image = vidcap.read()
count = 3
success = True
while success:
	success,image = vidcap.read()
	print 'Read a new frame: ', success
	cv2.imwrite("static/frame%d.jpg" % count, image)     # save frame as JPEG file
	count += 1
	break

print(cv2.__version__)
vidcap = cv2.VideoCapture('http://172.27.144.107:8090/cam1.mjpeg')
success,image = vidcap.read()
count = 4
success = True
while success:
	success,image = vidcap.read()
	print 'Read a new frame: ', success
	cv2.imwrite("static/frame%d.jpg" % count, image)     # save frame as JPEG file
	count += 1
	break
