import cv2

def take_pic():
    cam=cv2.VideoCapture(0)
    cv2.namedWindow("Python Webcam app")

    while True:
        ret,frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("test",frame)

        k= cv2.waitKey(1)
        if k%256==27:
            print("Escape hit...Closing the app")
            return
        elif k%256==32:
            img_name='p.png'
            cv2.imwrite(img_name,frame)
            print('picture taken')

    cam.release()

    cam.destroyAllWindows()

def get_sketch():
    img=cv2.imread('p.png')
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    invert=cv2.bitwise_not(grey_img)
    blur=cv2.GaussianBlur(invert,(21,21),0)
    invertedBlur=cv2.bitwise_not(blur)
    sketch=cv2.divide(grey_img,invertedBlur,scale=256.0)

    cv2.imwrite("sketch1.png",sketch)
