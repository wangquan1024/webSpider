import pytesseract,requests,time
from PIL import Image
from urllib import request

# 识别效果不佳，要通过图像处理将图片处理为白底黑字的图片可以提高识别率
def get_checkcode():
    url = "http://my.cnki.net/elibregister/CheckCode.aspx?id=1564996343307"
    while True:
        request.urlretrieve(url,'checkcode.png')
        image = Image.open('checkcode.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(3)

def main():
    get_checkcode()

if __name__ == "__main__":
    main()

