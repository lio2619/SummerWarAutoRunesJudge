#影像處理：二值化、降躁
from PIL import ImageFilter

def PhotoBinary(img):
    """將圖片二值化"""
    img = img.convert('L')
    img = img.point(lambda x: 0 if x < 127 else 1, '1')
    return img

def PhotoFilter(img):
    """將圖片降噪"""
    img = img.filter(ImageFilter.MedianFilter(size=3))
    return img