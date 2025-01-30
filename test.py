from my_Practice.similarity_algorithm.four_idea import *
import cv2
from tqdm import tqdm
import os
def calculate_similiaty_and_record(anchor_photo_folder,output_photo_folder,output_txt_path):
    anchor_files = [img for img in os.listdir(anchor_photo_folder) if img.endswith(".jpg") or img.endswith(".png")]
    output_files = [img for img in os.listdir(output_photo_folder) if img.endswith(".jpg") or img.endswith(".png")]
    file_names = []
    anchor_files = sorted(anchor_files)
    output_files = sorted(output_files)
    total_iterations = len(anchor_files) * len(output_files)
    with tqdm(total=total_iterations, desc="Processing") as pbar:
        for i, img in enumerate(output_files):
            output_img_path = os.path.join(output_photo_folder, img)
            for j, img2 in enumerate(anchor_files):
                anchor_img2_path = os.path.join(anchor_photo_folder, img2)
                image1 = cv2.imread(output_img_path)
                image2 = cv2.imread(anchor_img2_path)
                hist_s = float(hist_similarity(image1, image2))
                if (hist_s <0.1):
                    destination_name=img
                pbar.update(1)
            file_names.append(destination_name)
    with open(output_txt_path, 'w') as txt_file:
        for file_name in file_names:
            txt_file.write(file_name + '\n')
if __name__ == '__main__':
    anchor_photo_folder = 'anchor_images'
    output_photo_folder = 'output_images'
    need_to_clear_folder_directory="output_video_01.mp4"
    output_txt_path="txt_files/useful_images_name.txt"