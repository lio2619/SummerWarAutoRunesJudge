#獲取視窗大小、位置、名稱、類別
import win32gui
import win32con
import win32com.client

def GetWindowNameAndType():
    """獲得當前窗口名稱與類別"""
    hwnd = win32gui.GetForegroundWindow()
    return hwnd

def GetWindowSizeAndPostiion(hwnd):
    """獲得窗口大小、位置"""
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    high = bottom - top
    leftUpPosition = (left, top)
    return width, high, leftUpPosition

def SetWindowToTop(hwnd):
    """確定窗口是否最小化，如果最小化就將它放大成原尺寸，不管怎樣都會把窗口置頂"""
    if win32gui.IsIconic(hwnd):
        #最小化
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    else:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hwnd)

def SetWindowMinimize(hwnd):
    """最小化視窗"""
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)