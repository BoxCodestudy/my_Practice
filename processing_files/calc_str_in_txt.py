def count_lines_in_file(file_path):
    """
    统计指定文本文件中由换行符分隔的字符串（行）的数量。

    参数:
    file_path (str): 要统计行数的文本文件的路径。

    返回:
    int: 文件中的行数。
    """
    # 初始化行数计数器
    line_count = 0

    try:
        # 使用with语句打开文件，确保文件内容读取完毕后正确关闭文件
        with open(file_path, 'r', encoding='utf-8') as file:
            # 逐行读取文件内容
            for line in file:
                # 增加行数计数器
                line_count += 1
        return line_count
    except FileNotFoundError:
        # 如果文件未找到，返回错误信息
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        # 捕获其他可能的异常，并返回错误信息
        print(f"An error occurred: {e}")
        return None


# 使用示例
if __name__ == "__main__":
    # 替换为你的文本文件路径
    file_path = "path/to/your/textfile.txt"
    lines_number = count_lines_in_file(file_path)

    if lines_number is not None:
        print(f"The file '{file_path}' contains {lines_number} lines.")
