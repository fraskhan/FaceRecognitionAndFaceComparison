import cv2
import os

video_capture = cv2.VideoCapture(1)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")


def generate_dataset():
    check = 0
    cv2.putText(img, 'Capturing Image..', (50, 50), cv2.FONT_HERSHEY_COMPLEX, .5, (0, 255, 0), 2)
    cv2.putText(img, 'Please wait and stay within the image frame', (50, 70), cv2.FONT_HERSHEY_COMPLEX, .5, (0, 255, 0),
                2)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = faceCascade.detectMultiScale(gray_img, 1.1, 10)
    coordinate = []

    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Face", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 1, cv2.LINE_AA)
        coordinate = [x, y, w, h]

    print(coordinate)

    if len(coordinate) == 4:
        roi_img = img[coordinate[1]:coordinate[1] + coordinate[3], coordinate[0]:coordinate[0] + coordinate[2]]
        user_id = 1
        try:
            os.mkdir("Images/" + "Test")
        except OSError as error:
            print(error)

        cv2.imwrite("Images/" + "Test" + "/Image" + str(user_id) + "" + str(img_id) + ".jpg", roi_img)
        check = 1

    return check


img_id = 1
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    a = generate_dataset()
    cv2.imshow("Test", img)

    if cv2.waitKey(1) & 0xFF == ord('/'):
        break
video_capture.release()
cv2.destroyAllWindows()
