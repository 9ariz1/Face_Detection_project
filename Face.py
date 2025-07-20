import cv2
face_cap = cv2.CascadeClassifier("C:/Users/Hp/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

if not video_cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, video_data = video_cap.read()
    col =cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces :
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow("CAPTURE_FACE", video_data)

    if cv2.waitKey(10) == ord("s"):
        break

video_cap.release()
cv2.destroyAllWindows()