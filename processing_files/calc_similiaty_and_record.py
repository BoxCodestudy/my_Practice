from processing_files import clear_folder
from processing_files.count_photos_number import count_images_in_directory
from similarity_algorithm.four_idea import *
from similarity_algorithm.Hash import *
from numba import jit
import cv2
from tqdm import tqdm
import os
def calculate_similiaty_and_record(anchor_photo_folder,output_photo_folder,output_txt_path):
    # cnt=1
    # anchor_photos_number=count_images_in_directory(anchor_photo_folder)
    # output_photos_number=count_images_in_directory(output_photo_folder)
    anchor_files = [img for img in os.listdir(anchor_photo_folder) if img.endswith(".jpg") or img.endswith(".png")]
    output_files = [img for img in os.listdir(output_photo_folder) if img.endswith(".jpg") or img.endswith(".png")]

    # clear_folder.clear_folder_content(need_to_clear_folder_directory)
    file_names = []

    anchor_files = sorted(anchor_files)
    output_files = sorted(output_files)
    total_iterations = len(anchor_files) * len(output_files)

    with tqdm(total=total_iterations, desc="Processing") as pbar:
        for i, img in enumerate(output_files):
            output_img_path = os.path.join(output_photo_folder, img)
            for j, img2 in enumerate(anchor_files):
                # 这里是你循环中的代码
                anchor_img2_path = os.path.join(anchor_photo_folder, img2)
                image1 = cv2.imread(output_img_path)
                image2 = cv2.imread(anchor_img2_path)
                hash1 = pHash(image1)
                hash2 = pHash(image2)
                dist = Hamming_distance(hash1, hash2)
                similarity = 1 - dist * 1.0 / 64

                # 目的为了查看照片相似度的情况
                # print(f"输出图像第{i + 1}张{img}与锚图第{j + 1}张{img2}\nhist_similarity:{hist_similarity(image1, image2)}"
                #       # f"\nPSNR:{PSNR(image1, image2)}"
                #       f"\n灰度图SSIM:{SSIM(image1, image2)[0]}"
                #       f"\nRGB图_ssim:{ssim(image1, image2)}"
                #       # f"\nMSE:{MSE(image1, image2)}"
                #       f"\n哈希相似度:{similarity}")

                hist_s = float(hist_similarity(image1, image2))
                gray_SSIM_s = float(SSIM(image1, image2)[0])
                RGB_SSIM_s = float(ssim(image1, image2))
                hash_s = similarity

                if (hist_s <0.1 or gray_SSIM_s < 0.1 or RGB_SSIM_s <0.1 or hash_s < 0.1):
                    # destination_name = os.path.join(output_photo_folder, img)
                    destination_name=img
                pbar.update(1)
            file_names.append(destination_name)



    with open(output_txt_path, 'w') as txt_file:
        for file_name in file_names:
            txt_file.write(file_name + '\n')
    print("Useful frames have been written to txt_files/useful_images_name.txt")
if __name__ == '__main__':
    anchor_photo_folder = 'anchor_images'
    output_photo_folder = 'output_images'
    need_to_clear_folder_directory="output_video_01.mp4"
    output_txt_path="txt_files/useful_images_name.txt"