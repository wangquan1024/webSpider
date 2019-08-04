import pytesseract
from PIL import Image

# 打开图片
image = Image.open('code.png')
# 将图片转换为文字
# lang参数可以设置为识别的语言
code = pytesseract.image_to_string(image)
print(code)