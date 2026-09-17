import cv2

camera = cv2.VideoCapture(0)

while True:
    ok, frame = camera.read()
    if not ok:
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 255 == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
