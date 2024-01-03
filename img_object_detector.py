import cv2
from ultralytics import YOLO
from PIL import Image

img = cv2.imread('./test/2a319efa-pic52_jpg.rf.32d68562a3dce00b52647b81c182ba7c.jpg')

model = YOLO('best.pt')

results = model.predict(img)

# Both part 1 and 2 do the same thing. One is hardcoded and another is using method suggested by ultralytics

# part 1
for r in results:
    boxes = r.boxes
    class_ids = boxes.cls
    confidence = boxes.conf
    xyxys = boxes.xyxy
    
    i = 0
    for xyxy in xyxys:
        cv2.rectangle(img, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0,255,0), 2)
        
        label = r.names[int(class_ids[i])]

        i +=1
        w, h = cv2.getTextSize(label, 0, 2, 1)[0]

        p1 = (int(xyxy[0]), int(xyxy[1]))
        outside = p1[1] - h >= 3
        p2 = (p1[0] + w, p1[1] - h - 1 if outside else p1[1] + h + 1)

        cv2.rectangle(img, p1, p2, (113,236,232), -1, cv2.LINE_AA)
        cv2.putText(img, label, (p1[0], p1[1]-2 if outside else p1[1]+h+2), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255))
        
cv2.imshow('Image', img)
cv2.waitKey(0)

# Part 2
""" for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image """