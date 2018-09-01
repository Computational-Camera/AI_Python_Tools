import cv2

#init an array
img = np.zeros((height,width,3), np.uint8)

#load image from file
img = cv2.imread('test.png')# add additional flag 0:for mono import, -1: 16bit
height = img.shape[0]
width  = img.shape[1]
# or  height, width, channel = image.shape
print(image.shape)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#load video
while(length):
    # Capture frame-by-frame
    ret, frame = cap.read()
    length = length - 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#write image
cv2.imwrite('img.png', img)

#resize
img = cv2.resize(img,(w2,h2))
img = cv2.pyrDown(img) #pyrUp
#pixel visit
(b,g,r) = img[x,y]

#contour to bounding box
cv2.boundingRect(seg)  # [x,y,w,h]
#countour to area
cv2.contourArea (seg)

#draw image
cv2.putText(img, "blabla", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (r,g,b), 2)
cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), 3)#, -1 solid

#color coding
img2 = cv2.applyColorMap(img, cv2.COLORMAP_JET)


