import os
import requests

def download_images(image_urls, save_folder):
    """
    从给定的URL列表下载所有的图片并保存到指定的文件夹中。
    
    :param image_urls: 包含图片URL的列表
    :param save_folder: 保存下载图片的本地文件夹路径
    """
    # 创建保存图片的文件夹，如果它还不存在的话
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    total_images = len(image_urls)
    print(f"Found {total_images} images to download.")

    for i, img_url in enumerate(image_urls):
        # 获取图片名称
        img_name = os.path.basename(img_url)

        # 下载图片
        try:
            img_data = requests.get(img_url).content
            with open(os.path.join(save_folder, img_name), 'wb') as f:
                f.write(img_data)
            print(f"{i+1}/{total_images}: Downloaded {img_name}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

# 使用示例
# image_urls = [
#     'https://example.com/image1.jpg',
#     'https://example.com/image2.jpg',
#     'https://example.com/image3.jpg'
# ]
save_folder = './downloaded_images'  # 图片保存的文件夹

image_urls = []


# 使用示例
url = 'http://agora.ex.nii.ac.jp/'  # 替换为你想爬取的网站URL
save_folder = '.'  # 图片保存的文件夹

for i in range(21,29):
    for j in range(0,24):
        image_urls.append(url+"/digital-typhoon/wnp/by-name/202305/4/512x512/HMW92307{:02d}{:02d}.202305.jpg".format(i,j))
download_images(image_urls, save_folder)