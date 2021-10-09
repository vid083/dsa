import cv2 , time

video = cv2.VideoCapture(0)
first_frame = None

while True:
    check, frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame=cv2.absdiff(first_frame, gray)
    threshold_frame=cv2.dilate()