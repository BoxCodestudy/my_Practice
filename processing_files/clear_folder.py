import os
def clear_folder_content(target_folder_path):
    for filename in os.listdir(target_folder_path):
        file_path = os.path.join(target_folder_path, filename)
        os.remove(file_path)