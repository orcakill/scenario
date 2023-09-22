import os

from pypinyin import pinyin, Style

from src.utils import utils_path


def get_subdirectories(folder_path):
    subdirectories1 = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subdirectories1.append(item_path)
    return subdirectories1


if __name__ == '__main__':
    # 指定文件夹路径
    folder_path1 = utils_path.get_project_path() + r'\src\resources\static\onmyoji\式神录\御魂整理'

    # 获取所有文件夹
    subdirectories = get_subdirectories(folder_path1)

    # 打印所有文件夹路径（去除指定路径部分）
    path = utils_path.get_project_path() + r'\src\resources\static\onmyoji\式神录'
    for subdir in subdirectories:
        subdir = subdir.replace(path, "式神录")
        parts = subdir.split("\\")
        result = parts[-1]

        # 使用 pinyin() 函数将中文转换为拼音
        pinyin_text = pinyin(result, style=Style.FIRST_LETTER)

        # 将拼音列表转换为字符串并转换为大写
        pinyin_text = ''.join([item[0].upper() for item in pinyin_text])

        print("arrange_" + pinyin_text + "=r" + "\"" + subdir + "\"")
