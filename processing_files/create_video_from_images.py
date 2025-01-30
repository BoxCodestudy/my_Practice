import cv2
import os


def generate_video_from_images(image_folder, txt_file_path, output_video_path,old_video_path,source_video_path,fps=24):
    """
    根据TXT文件中列出的照片名字，从指定文件夹中找到这些照片并合成视频。

    参数:
    - image_folder (str): 包含照片的文件夹路径。
    - txt_file_path (str): 包含照片文件名的TXT文件路径。
    - output_video_path (str): 输出视频的文件路径。
    - fps (int): 视频的帧率，默认为24。
    """
    if (os.path.isfile(old_video_path)):
        # print('发现存在旧输出视频，正将其删除\n')
        os.remove(old_video_path)
    # 读取TXT文件，获取照片名字列表
    with open(txt_file_path, 'r') as f:
        image_names = f.read().splitlines()

    # 确定视频的宽度和高度
    my_cap = cv2.VideoCapture(source_video_path)
    my_width = int(my_cap.get(3))
    my_height = int(my_cap.get(4))
    my_cap.release()

    # 创建视频写入对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 视频编解码器
    video = cv2.VideoWriter(output_video_path, fourcc, fps, (my_width, my_height))

    # 遍历照片名字列表，将每张照片添加到视频中
    for image_name in image_names:
        image_path = os.path.join(image_folder, image_name)
        if not os.path.exists(image_path):
            print(f"Warning: Image '{image_path}' does not exist and will be skipped.")
            continue

        img = cv2.imread(image_path)
        video.write(img)

    # 释放视频写入对象
    video.release()
    print(f"Video has been successfully generated at '{output_video_path}'")

# 使用示例
if __name__ == "__main__":
    image_folder = "path/to/your/image/folder"
    txt_file_path = "path/to/your/txt/file.txt"
    output_video_path = "output_video.mp4"

    generate_video_from_images(image_folder, txt_file_path, output_video_path)
