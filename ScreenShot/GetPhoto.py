#截圖
from PIL import Image, ImageGrab
from skimage.metrics import structural_similarity as ssim
import os
import math
import numpy as np

def GetScreenShot(startX, startY, endX, endY):
    """先將圖片做對比，再將圖片轉文字"""
    img = ImageGrab.grab(bbox=(startX, startY, endX, endY))
    return img

def PhotoCompareMSE(newImg):
    """用mse算法來比較兩張圖片的相似度，越接近0越相似"""
    originImgs = os.listdir("OriginPhoto")
    for originImg in originImgs:
        h1 = Image.open(f"OriginPhoto/{originImg}").histogram()
        h2 = newImg.histogram()
        different = math.sqrt(sum((a - b) ** 2 for a, b in zip(h1, h2)) / len(h1))
        print(different)
        if different < 3:
            return False
    #是符文才回傳true
    return True

def PhotoCompareSSIM(newImg):
    """用ssim算法來比較兩張圖片的相似度，越接近1.0越相似、接近-1.0越不相似"""
    originImgs = os.listdir("OriginPhoto")
    for originImg in originImgs:
        img = Image.open(f"OriginPhoto/{originImg}")
        different = ssim(np.array(img), np.array(newImg), channel_axis=-1)
        if different > 0.5:
            return False
    #是符文才回傳true
    return True

def PhotoGrayAverageBrightness(newImg):
    """先將圖片轉成灰階，再計算圖片的平均亮度"""
    img = newImg.convert('L')
    pixelVales = list(img.getdata())
    averageBrightness = sum(pixelVales) / len(pixelVales)
    if averageBrightness > 90:
        #是符文且沒有賣出
        return True
    return False