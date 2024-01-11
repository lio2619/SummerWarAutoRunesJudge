#圖片轉文字
from OCR.HeaderActionsDict import actions, blessingsActions, fierceAttackActions, bladeEdgeActions, provocationActions, repaidActions, concentrateActions
from OCR.HeaderActionsDict import guardActions, patienceActions, rampageActions, despairActions, bloodsuckActions, willpowerActions, retributionActions
from OCR.HeaderActionsDict import protectionActions, counterattackActions, destructionActions
import pytesseract

runsHeaderActions = {
    "祝福": blessingsActions,
    "猛攻": fierceAttackActions,
    "刀刃": bladeEdgeActions,
    "激怒": provocationActions,
    "迅速": repaidActions,
    "集中": concentrateActions,
    "守護": guardActions,
    "忍耐": patienceActions,
    "暴走": rampageActions,
    "絕望": despairActions,
    "吸血": bloodsuckActions,
    "意志": willpowerActions,
    "應報": retributionActions,
    "保護": protectionActions,
    "反擊": counterattackActions,
    "破壞": destructionActions
}

def CheckElementInDictionary(element, header, after, headerActions):
    """確定符文標頭是否在字典裡"""
    text = element.split('+')[0]
    if header:
        if text in headerActions:
            return headerActions[text](element, after)
    else:
        if text in headerActions:
            return headerActions[text](element, after)
    return 1

def GetRunsImageText(img, path, header, after):
    """將符文圖片轉成文字，依照原本格式"""
    score = 0
    pytesseract.pytesseract.tesseract_cmd = path
    lines = pytesseract.image_to_string(img, lang='chi_tra')
    lines = [i for i in lines.replace(' ', '').split("\n") if i]
    print(lines)
    targetAction = runsHeaderActions.get(header, actions)
    for element in lines:
        score += CheckElementInDictionary(element, header, after, targetAction)
    print(f"score = {score}")
    if score > 1:
        return False
    return True

def GetRunsHeaderImageText(img, path):
    """讀取符文標頭"""
    pytesseract.pytesseract.tesseract_cmd = path
    text = pytesseract.image_to_string(img, lang='chi_tra')
    text = [i for i in text.replace(' ', '').split("\n") if i]
    try:
        header = text[0].split("符文")[0][-2:]
        print(header)
    except:
        print(f"符文標頭 = {text}")
        print("符文標頭無法讀取")
        return ""
    return header

def GetImageText(img, path):
    """防止賣出東西時沒有東西導致出錯"""
    pytesseract.pytesseract.tesseract_cmd = path
    text = pytesseract.image_to_string(img, lang='chi_tra')
    text = [i for i in text.replace(' ', '').split("\n") if i]
    if text and text[0] == "尚未選擇欲出售的道具。":
        return True
    return False

def GetContinuousBattleEndText(img, path):
    """獲得連續戰鬥結束文字"""
    pytesseract.pytesseract.tesseract_cmd = path
    text = pytesseract.image_to_string(img, lang='chi_tra')
    text = [i for i in text.replace(' ', '').split("\n") if i]
    #print(text)
    if text and text[0] == "連續戰鬥已結束。":
        return True
    return False