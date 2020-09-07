import cv2

tracker = cv2.TrackerCSRT_create()
video = cv2.VideoCapture(0)

while True:
    k,img = video.read()
    cv2.imshow("Tracking",img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
rect = cv2.selectROI(img, False)

inital = tracker.init(img, rect)
cv2.destroyWindow("ROI selector")

while True:
    ret, img = video.read()
    ret, rect = tracker.update(img)

    if ret:
        p1 = (int(rect[0]), int(rect[1]))
        p2 = (int(rect[0] + rect[2]),
              int(rect[1] + rect[3]))
        cv2.rectangle(img, p1, p2, (0,0,255), 2, 2)

    cv2.imshow("objectrack", img)
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break

