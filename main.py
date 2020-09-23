import cv2 

net2 = cv2.dnn.readNet('person-detection-retail-0013.bin', 'person-detection-retail-0013.xml')
net = cv2.dnn.readNet('face-detection-adas-0001.bin', 'face-detection-adas-0001.xml')

cap = cv2.VideoCapture("video3.mp4")

font = cv2.FONT_HERSHEY_SIMPLEX

while cv2.waitKey(1) < 0:
    hasFrame, frame = cap.read()
    frame = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    if not hasFrame:
        break

    face_blob = cv2.dnn.blobFromImage(frame, size=(672, 384))
    net.setInput(face_blob)
    out_face = net.forward()

    for detection in out_face.reshape(-1, 7):
        confidence = float(detection[2])
        xmin = int(detection[3] * frame.shape[1])
        ymin = int(detection[4] * frame.shape[0])
        xmax = int(detection[5] * frame.shape[1])
        ymax = int(detection[6] * frame.shape[0])
        
        if confidence > 0.5:
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color=(0, 255, 0))
            cv2.putText(frame,'FACE',(xmin, (ymin-10)),font, 0.4,(0, 255, 255),1,cv2.LINE_AA) 

    person_blob = cv2.dnn.blobFromImage(frame, size=(672, 384))
    net2.setInput(person_blob)
    out_person = net2.forward()

    for detection in out_person.reshape(-1, 7):
        confidence2 = float(detection[2])
        xmin2 = int(detection[3] * frame.shape[1])
        ymin2 = int(detection[4] * frame.shape[0])
        xmax2 = int(detection[5] * frame.shape[1])
        ymax2 = int(detection[6] * frame.shape[0])

        if confidence2 > 0.6:
            cv2.rectangle(frame, (xmin2, ymin2), (xmax2, ymax2), color=(0, 255, 0))
            
            cv2.putText(frame,'PERSON',(xmin2, (ymin2-10)),font, 0.4,(0, 255, 255),1,cv2.LINE_AA) 
    cv2.imshow('OpenVINO face detection', frame)
