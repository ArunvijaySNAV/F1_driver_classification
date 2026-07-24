import cv2
from matplotlib import pyplot as plt


def if_image_eyes(image_path):
    if image_path.split('.')[1] == 'jpg':

        original_img = cv2.imread(image_path)

        # convertion of the original image into the back and white image
        bw_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

        # image cascading
        face_cascade = cv2.CascadeClassifier(
            '/Users/snarunvijay/Documents/Machine_Learning/ImageClassification/model/opencv/haarcascades/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(
            '/Users/snarunvijay/Documents/Machine_Learning/ImageClassification/model/opencv/haarcascades/haarcascade_eye.xml')

        # used cascade and detecting face
        face_images = face_cascade.detectMultiScale(bw_img)
        for (x, y, w, h) in face_images:
            rec_pic = cv2.rectangle(original_img, (x, y), (x + h, y + w), (255, 0, 0), 2)

            gray_roi = bw_img[y:y + h, x:x + w]
            face_roi = rec_pic[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(gray_roi)

            if len(eyes) == 2:
                for (ex, ey, ew, eh) in eyes:
                    pass
                    # cv2.rectangle(face_roi, (ex, ey), (ex + eh, ey + ew), (0, 255, 0), 2)

                plt.figure()
                plt.imshow(face_roi)
                plt.show()
            else:
                return None