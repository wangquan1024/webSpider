import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')

if not os.path.exists(path):
    print('文件夹不存在')
else:
    print('文件夹存在')
