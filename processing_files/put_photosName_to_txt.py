import os
### 定义文件夹路径和输出txt文件路径
oppointed_photo_path = "../useful_images"  # 替换为你的照片路径
output_txt_path = "../txt_files/useful_images_name.txt"  # 替换为你的输出txt文件路径

### 遍历文件夹中的所有文件
def photos_to_txt(oppointed_photo_path,output_txt_path):
    file_names = []
    for file_name in os.listdir(oppointed_photo_path):
        if file_name.lower().endswith(('.png',  '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            file_names.append(file_name)
    ### 将文件名写入到指定的txt文档中
    with open(output_txt_path, 'w') as txt_file:
        for file_name in file_names:
            txt_file.write(file_name  + '\n')

    print(f"文件名已成功写入到 {output_txt_path}")
if __name__ == '__main__':
    oppointed_photo_path = '../vital_photos'  # 替换为你的照片路径
    output_txt_path = '../txt_files/vital_photos_name.txt'  # 替换为你的输出txt文件路径
    photos_to_txt(oppointed_photo_path,output_txt_path)