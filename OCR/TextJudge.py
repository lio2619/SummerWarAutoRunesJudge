#判斷是否符合規則
import re

def CheckElement(element, after, limitBefore, limitAfter):
    """檢查元素是否符合規則"""
    if element.find("%") == -1:
        return 1
    number = GetNumberInString(element)
    if after:
        if number <= limitAfter:
            return 1
        else:
            #符合規則
            return -2
    else:
        if number <= limitBefore:
            return 1
    return 0

def Attack(element, after):
    """攻擊力"""
    return CheckElement(element, after, 5, 17)

def Health(element, after):
    """體力"""
    return CheckElement(element, after, 5, 17)


def Defense(element, after):
    """防禦力"""
    return CheckElement(element, after, 6, 20)


def Speed(element, after):
    """攻擊速度"""
    number = GetNumberInString(element)
    if after:
        if number <= 15:
            return 1
        else:
            return -2
    else:
        if number <= 4:
            return 1
    return 0

def CriticalHit(element, after):
    """爆擊率"""
    return CheckElement(element, after, 5, 17)


def CriticalHitDamage(element, after):
    """爆擊傷害"""
    return CheckElement(element, after, 6, 18)

def Effect(element, after):
    """效果命中、抵抗"""
    return CheckElement(element, after, 6, 19)


def GetNumberInString(element):
    """回傳第一組數字"""
    return int(re.findall('[0-9]+', element)[0])