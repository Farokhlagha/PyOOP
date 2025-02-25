import cv2

cap = cv2.VideoCapture("input\obama.mp4")
image_sticker = cv2.imread("input\sticker.jpeg")
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

while True:
    _, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_detector.detectMultiScale(frame_gray)

    for face in faces:
        x, y, w, h = face
        sticker = cv2.resize(image_sticker, (w, h))
        frame[y:y+h, x:x+w] = sticker


 
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break