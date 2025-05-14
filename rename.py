import os
from glob import glob

def rename_images(directory):
    # 获取目录中所有符合条件的图片文件
    files = glob(os.path.join(directory, 'HMW92307*.202305.jpg'))
    
    # 按文件名排序
    files.sort()
    
    # 重命名图片
    for index, file in enumerate(files):
        new_name = os.path.join(directory, f'image_{index:03d}.jpg')
        os.rename(file, new_name)
        print(f'Renamed {file} to {new_name}')

# 指定图片所在的目录
directory = 'C:\\Users\\tifis\\Desktop\\ff\\doksuri'
rename_images(directory)