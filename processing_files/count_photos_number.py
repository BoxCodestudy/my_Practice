import os


def count_images_in_directory(directory_path):
    """
    统计指定文件夹下所有照片的数量。

    参数:
    directory_path (str): 要统计的文件夹路径。

    返回:
    int: 文件夹下照片的数量。
    """
    # 定义图片文件的扩展名
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

    # 初始化图片计数器
    image_count = 0

    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # 检查文件扩展名是否为图片文件
            if file.lower().endswith(image_extensions):
                image_count += 1

    return image_count


# 使用示例
if __name__ == "__main__":
    directory_path = "path/to/your/image/directory"
    total_images = count_images_in_directory(directory_path)
    print(f"Total number of images in '{directory_path}': {total_images}")
