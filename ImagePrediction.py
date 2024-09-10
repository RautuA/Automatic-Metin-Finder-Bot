from ultralytics import YOLO


model = YOLO('best.pt')  


screenx_center = 3840/2
screeny_center = 2160/2

decision = {
    "metin": False,
    
}

results = model(['Test2.png'], conf=.80, save=True)  
boxes = results[0].boxes.xyxy.tolist()
classes = results[0].boxes.cls.tolist()
names = results[0].names
confidences = results[0].boxes.conf.tolist()


for box, cls, conf in zip(boxes, classes, confidences):
    x1, y1, x2, y2 = box
    
    center_x = (x1+x2) / 2
    center_y = (y1+y2) / 2

    confidence = conf
    detected_class = cls
    name = names[int(cls)]
    
    if name=="metin":
        decision["metin"] = True
        decision["metin_location"] = (center_x, center_y)
    
    elif name == "metin":
        decision["metin"] = True
        distance = ((center_x - screenx_center) ** 2 + (center_y - screeny_center) **2) **.5
        if "metin_location" in decision:
            
            if distance < decision["metin_distance"]:
                decision["metin_location"] = (center_x, center_y)
                decision["metin_distance"] = distance
        else:
            decision["metin_location"] = (center_x, center_y)
            decision["metin_distance"] = distance
   
print(decision)