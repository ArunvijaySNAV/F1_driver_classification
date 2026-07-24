import os
import cv2
import shutil
from cropping_img import if_image_eyes


path_to_data = "./model/dataset/"
path_to_cropped_data = "./model/dataset/cropped/"

cropped_imgs_dirs = []
celebrity_file_names_dict = {}

img_dirs = []

for entry in os.scandir(path_to_data):
    if entry.is_dir():
        img_dirs.append(entry.path)

if os.path.exists(path_to_cropped_data):
    shutil.rmtree(path_to_cropped_data)
os.makedirs(path_to_cropped_data)


for img_dir in img_dirs:
    count = 0
    celebrity_name = img_dir.split('/')[-1]

    celebrity_file_names_dict[celebrity_name] = []

    for entry in os.scandir(img_dir):
        roi_color = if_image_eyes(entry.path)

        if roi_color is not None:
            cropped_folder = path_to_cropped_data + celebrity_name

            if not os.path.exists(cropped_folder):
                os.makedirs(cropped_folder)
                cropped_imgs_dirs.append(cropped_folder)
                print('generating cropped images', cropped_folder)

            cropped_file_name = celebrity_name + str(count) + '.png'
            cropped_file_path = cropped_folder + '/' +cropped_file_name

            cv2.imwrite(cropped_file_path, roi_color)
            celebrity_file_names_dict[celebrity_name].append(cropped_file_path)
            count += 1