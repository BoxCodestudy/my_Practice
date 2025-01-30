from processing_files.first_video_to_photo import video_to_images
from processing_files.calc_similiaty_and_record import calculate_similiaty_and_record
from processing_files.calc_str_in_txt import count_lines_in_file
from processing_files.count_equla_strings import count_equal_strings
from processing_files.create_video_from_images import generate_video_from_images
from processing_files import *
from similarity_algorithm import *
video_path = 'raw_materials/test_video.mp4'
output_folder = 'output_images'
video_to_images(video_path, output_folder, sampling_rate=1)

anchor_photo_folder= 'anchor_images'
output_photo_folder='output_images'
# need_to_clear_folder_directory="output_video_01.mp4"
output_txt_path= "txt_files/useful_images_name.txt"
calculate_similiaty_and_record(anchor_photo_folder,output_photo_folder,output_txt_path)

image_folder = 'output_images'
output_video_path = 'output_video_01.mp4'
txt_file_path= "txt_files/useful_images_name.txt"
old_video_path="output_video_01.mp4"
source_video_path="raw_materials/test_video.mp4"
generate_video_from_images(image_folder,txt_file_path,output_video_path,old_video_path,source_video_path,fps=15)

file1 = "txt_files/useful_images_name.txt"
file2 = "txt_files/vital_photos_name.txt"

Hit_number = count_equal_strings(file1, file2) #Hit_number

Key_Frame_number=count_lines_in_file(file2)
R=(Hit_number/Key_Frame_number)*100 # 命中率计算公式 R = Hit_number/Key_Frame_number
print(f"本次抽帧命中率为:{R}%")