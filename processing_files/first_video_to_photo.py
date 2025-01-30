import cv2
import os
from . import clear_folder
def video_to_images(video_path, output_folder, sampling_rate):
    clear_folder.clear_folder_content(output_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break


        if frame_id % sampling_rate == 0:
            image_name = f"frame_{frame_id:04d}.jpg"
            image_path = os.path.join(output_folder, image_name)
            cv2.imwrite(image_path, frame)

        frame_id += 1

    cap.release()
    print("All frames have been saved as photos successfully.")


if __name__ == '__main__':
    video_path = 'my_Practice/raw_materials/test_video.mp4'
    output_folder = 'my_Practice/output_images'
    video_to_images(video_path, output_folder, sampling_rate=1)