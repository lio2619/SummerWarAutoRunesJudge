#圖片轉文字
from OCR.TextJudge import Attack, Defense, Health, Speed, CriticalHit, CriticalHitDamage, Effect
import pytesseract

actions = {
    "攻擊速度": Speed,
    "體力": Health,
    "攻擊力": Attack,
    "防禦力": Defense,
    "暴擊率": CriticalHit,
    "暴擊傷害": CriticalHitDamage,
    "效果命中": Effect,
    "效果抵抗": Effect
}

def GetRunsImageText(img, path, after):
    """將符文圖片轉成文字，依照原本格式"""
    score = 0
    pytesseract.pytesseract.tesseract_cmd = path
    text = pytesseract.image_to_string(img, lang='chi_tra')
    text = [i for i in text.replace(' ', '').split("\n") if i]
    print(text)
    for element in text:
        for key in actions.keys():
            if key in element:
                score += actions[key](element, after)
                break
    print(score)
    if score > 1:
        return False
    return True

def GetImgText(img, path):
    pytesseract.pytesseract.tesseract_cmd = path
    text = pytesseract.image_to_string(img, lang='chi_tra')
    text = [i for i in text.replace(' ', '').split("\n") if i]
    if text and text[0] == "尚未選擇欲出售的道具。":
        return True
    return False