def count_equal_strings(file1, file2):
    # 读取文件内容
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # 去除行末的换行符
    lines1 = [line.strip() for line in lines1]
    lines2 = [line.strip() for line in lines2]

    # 找出相同的字符串
    common_strings = set(lines1) & set(lines2)

    # 返回相同字符串的数量
    return len(common_strings)
