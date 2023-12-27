import cv2
import os
def change_size(images_path):
    
    for filename in os.listdir(images_path):
        file_path=os.path.join(images_path,filename)
        image=cv2.imread(file_path)
        resized_image = cv2.resize(image, (640, 640))
        cv2.imwrite(file_path, resized_image)
images_path="images"

change_size(images_path)


