import cv2 
import os 
 
def images_to_video(image_folder, output_video_path, source_video_path, fps):
    if (os.path.isfile('output_video_01.mp4')):
        print('发现存在旧输出视频，正将其删除\n')
        os.remove('output_video_01.mp4')

    my_cap = cv2.VideoCapture(source_video_path) 
    my_width = int(my_cap.get(3))  
    my_height = int(my_cap.get(4))  
    my_cap.release()  
 
    image_files = [img for img in os.listdir(image_folder)  if img.endswith(".jpg")]  
    if not image_files: 
        print("图像文件夹中没有找到有效的图像文件") 
        return 
 
    frame_array = [] 
    size = () 
    for i, img in enumerate(sorted(image_files)): 
        img_path = os.path.join(image_folder,  img) 
        frame = cv2.imread(img_path)  
        frame = cv2.resize(frame,  (0, 0), fx=0.5, fy=0.5) 
        height, width, layers = frame.shape  
        size = (width, height) 
        frame_array.append(frame)  
 
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size) 
 
    for i in range(len(frame_array)): 
        out.write(frame_array[i])  
 
    out.release()  
    print("视频已生成") 
 
if __name__ == '__main__': 
    image_folder = 'my_Practice/useful_images' 
    output_video_path = 'output_video_01.mp4'  
    source_video_path = 'my_Practice/raw_materials/test_video.mp4'  
    images_to_video(image_folder, output_video_path, source_video_path, fps=30) 