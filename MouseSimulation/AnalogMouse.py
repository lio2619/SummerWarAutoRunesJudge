#模擬滑鼠操作
import win32api
import win32con
import time

def AnalogMouseLeftClickAndMove(startX, startY, endX, endY):
    """模擬滑鼠按者左鍵並且移動"""
    startX = round(startX)
    startY = round(startY)
    endX = round(endX)
    endY = round(endY)
    time.sleep(1)
    win32api.SetCursorPos((startX, startY))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, startX, startY, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((endX, endY))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, endX, endY, 0, 0)

def AnalogMouseLeftClick(startX, startY):
    """模擬滑鼠按左鍵"""
    startX = round(startX)
    startY = round(startY)
    time.sleep(1)
    win32api.SetCursorPos((startX, startY))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, startX, startY, 0, 0)
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, startX, startY, 0, 0)


def GetMouseClickPosition():
    """透過滑鼠點擊獲得該座標"""
    while True:
        start = win32api.GetKeyState(0x01)
        if start == -127 or start == -128:
            x, y = win32api.GetCursorPos()
            print(f"x = {x}, y = {y}")
            break