from WindowDetail.GetWindowDetail import GetWindowNameAndType, GetWindowSizeAndPostiion, SetWindowMinimize, SetWindowToTop
from WindowDetail.GetWinsowProportion import WindowProportion
from MouseSimulation.AnalogMouse import GetMouseClickPosition, AnalogMouseLeftClick, AnalogMouseLeftClickAndMove
from ScreenShot.GetPhoto import GetScreenShot, PhotoGrayAverageBrightness, PhotoCompareSSIM
from OCR.PhotoToText import GetRunsImageText, GetRunsHeaderImageText, GetImageText, GetContinuousBattleEndText
from ScreenShot.ImageProcessing import PhotoBinary
import time
import datetime

def AutoRunsSteps(leftUpPosition, path):
    #解除休眠
    AnalogMouseLeftClickAndMove(leftUpPosition[0] + 114, leftUpPosition[1] + 676, leftUpPosition[0] + 114, leftUpPosition[1] + 376)
    #滑動到符文頁面到最上面
    AnalogMouseLeftClickAndMove(leftUpPosition[0] + 1060, leftUpPosition[1] + 345, leftUpPosition[0] + 1060, leftUpPosition[1] + 445)
    #賣掉不符合規則的符文
    AnalogMouseLeftClick(leftUpPosition[0] + 1167, leftUpPosition[1] + 690)
    AnalogMouseLeftClick(leftUpPosition[0] + 1002, leftUpPosition[1] + 684)
    AnalogMouseLeftClick(leftUpPosition[0] + 554, leftUpPosition[1] + 481)
    #賣掉傳說符文
    AnalogMouseLeftClick(leftUpPosition[0] + 549, leftUpPosition[1] + 481)
    #沒有符合的符文
    noSaleRunsImage = GetScreenShot(leftUpPosition[0] + 475, leftUpPosition[1] + 283, leftUpPosition[0] + 860, leftUpPosition[1] + 362)
    noSale = GetImageText(noSaleRunsImage, path)
    if noSale:
        AnalogMouseLeftClick(leftUpPosition[0] + 670, leftUpPosition[1] + 479)
        AnalogMouseLeftClick(leftUpPosition[0] + 1184, leftUpPosition[1] + 688)
    for i in range(0, 3):
        for j in range(0, 4):
            #做圖片比對符合符文才做以下動作
            down = 106 * i
            right = 106 * j
            time.sleep(1)
            runsImage = GetScreenShot(leftUpPosition[0] + 867 + right, leftUpPosition[1] + 314 + down, leftUpPosition[0] + 938 + right, leftUpPosition[1] + 382 + down)
            runsImageCompare = PhotoCompareSSIM(runsImage)
            runsImageSale = PhotoGrayAverageBrightness(runsImage)
            if runsImageCompare and runsImageSale:
                #點擊符文並且截圖至OCR做判斷
                AnalogMouseLeftClick(leftUpPosition[0] + 900 + right, leftUpPosition[1] + 345 + down)
                time.sleep(0.5)
                #獲取符文標頭
                img = GetScreenShot(leftUpPosition[0] + 514, leftUpPosition[1] + 164, leftUpPosition[0] + 769, leftUpPosition[1] + 216)
                img = PhotoBinary(img)
                header = GetRunsHeaderImageText(img, path)
                runsInitiallyDetailImage = GetScreenShot(leftUpPosition[0] + 403, leftUpPosition[1] + 317, leftUpPosition[0] + 772, leftUpPosition[1] + 463)
                initiallyMatches = GetRunsImageText(runsInitiallyDetailImage, path, header, 0)
                if initiallyMatches:
                    #強化
                    AnalogMouseLeftClick(leftUpPosition[0] + 784, leftUpPosition[1] + 576)
                    #+6
                    AnalogMouseLeftClick(leftUpPosition[0] + 424, leftUpPosition[1] + 482)
                    #確定強化
                    AnalogMouseLeftClick(leftUpPosition[0] + 509, leftUpPosition[1] + 614)
                    #做OCR判斷是否符合規則
                    time.sleep(4)
                    runsFinallyDetailImage = GetScreenShot(leftUpPosition[0] + 749, leftUpPosition[1] + 362, leftUpPosition[0] + 1022, leftUpPosition[1] + 497)
                    finallyMatch = GetRunsImageText(runsFinallyDetailImage, path, header, 1)
                    if finallyMatch:
                        #符合確定
                        AnalogMouseLeftClick(leftUpPosition[0] + 820, leftUpPosition[1] + 694)
                        #離開
                        AnalogMouseLeftClick(leftUpPosition[0] + 674, leftUpPosition[1] + 720)
                        #符合規則才有按叉
                        AnalogMouseLeftClick(leftUpPosition[0] + 927, leftUpPosition[1] + 186)
                    else:
                        #不符合出售
                        AnalogMouseLeftClick(leftUpPosition[0] + 591, leftUpPosition[1] + 696)
                        #賣掉傳說符文
                        AnalogMouseLeftClick(leftUpPosition[0] + 550, leftUpPosition[1] + 480)
                        #離開
                        AnalogMouseLeftClick(leftUpPosition[0] + 674, leftUpPosition[1] + 720)
                else:
                    #賣掉單獨符文
                    AnalogMouseLeftClick(leftUpPosition[0] + 562, leftUpPosition[1] + 589)
                    #賣掉傳說符文
                    AnalogMouseLeftClick(leftUpPosition[0] + 544, leftUpPosition[1] + 480)
        if i == 4:
            #滑動到符文頁面到最下面
            AnalogMouseLeftClickAndMove(leftUpPosition[0] + 1060, leftUpPosition[1] + 445, leftUpPosition[0] + 1060, leftUpPosition[1] + 345)    
    #再來一次
    AnalogMouseLeftClick(leftUpPosition[0] + 713, leftUpPosition[1] + 674)
    AnalogMouseLeftClick(leftUpPosition[0] + 1118, leftUpPosition[1] + 589)
    #休眠
    AnalogMouseLeftClick(leftUpPosition[0] + 114, leftUpPosition[1] + 676)

def AutoRunsStepsProportion(leftUpPosition, widthProportion, highProportion, path):
    #解除休眠
    AnalogMouseLeftClickAndMove((leftUpPosition[0] + 114) * widthProportion, (leftUpPosition[1] + 676) * highProportion, (leftUpPosition[0] + 114) * widthProportion, (leftUpPosition[1] + 376) * highProportion)
    #滑動到符文頁面到最上面
    AnalogMouseLeftClickAndMove((leftUpPosition[0] + 1060) * widthProportion, (leftUpPosition[1] + 345) * highProportion, (leftUpPosition[0] + 1060) * widthProportion, (leftUpPosition[1] + 445) * highProportion)
    #賣掉不符合規則的符文
    AnalogMouseLeftClick((leftUpPosition[0] + 1167) * widthProportion, (leftUpPosition[1] + 690) * highProportion)
    AnalogMouseLeftClick((leftUpPosition[0] + 1002) * widthProportion, (leftUpPosition[1] + 684) * highProportion)
    AnalogMouseLeftClick((leftUpPosition[0] + 554) * widthProportion, (leftUpPosition[1] + 481) * highProportion)
    #賣掉傳說符文
    AnalogMouseLeftClick((leftUpPosition[0] + 549) * widthProportion, (leftUpPosition[1] + 481) * highProportion)
    #沒有符合的符文
    noSaleRunsImage = GetScreenShot((leftUpPosition[0] + 475) * widthProportion, (leftUpPosition[1] + 283) * highProportion, (leftUpPosition[0] + 860) * widthProportion, (leftUpPosition[1] + 362) * highProportion)
    noSale = GetImageText(noSaleRunsImage, path)
    if noSale:
        AnalogMouseLeftClick((leftUpPosition[0] + 670) * widthProportion, (leftUpPosition[1] + 479) * highProportion)
        AnalogMouseLeftClick((leftUpPosition[0] + 1184) * widthProportion, (leftUpPosition[1] + 688) * highProportion)
    for i in range(0, 3):
        for j in range(0, 4):
            #做圖片比對符合符文才做以下動作
            down = 106 * i
            right = 106 * j
            time.sleep(1)
            runsImage = GetScreenShot((leftUpPosition[0] + 867 + right) * widthProportion, (leftUpPosition[1] + 314 + down) * highProportion, (leftUpPosition[0] + 938 + right) * widthProportion, (leftUpPosition[1] + 382 + down) * highProportion)
            runsImageCompare = PhotoCompareSSIM(runsImage)
            runsImageSale = PhotoGrayAverageBrightness(runsImage)
            if runsImageCompare and runsImageSale:
                #點擊符文並且截圖至OCR做判斷
                AnalogMouseLeftClick((leftUpPosition[0] + 900 + right) * widthProportion, (leftUpPosition[1] + 345 + down) * highProportion)
                time.sleep(0.5)
                #獲取符文標頭
                img = GetScreenShot((leftUpPosition[0] + 514) * widthProportion, (leftUpPosition[1] + 164) * highProportion, (leftUpPosition[0] + 769) * widthProportion, (leftUpPosition[1] + 216) * highProportion)
                img = PhotoBinary(img)
                header = GetRunsHeaderImageText(img, path)
                runsInitiallyDetailImage = GetScreenShot((leftUpPosition[0] + 403) * widthProportion, (leftUpPosition[1] + 317) * highProportion, (leftUpPosition[0] + 772) * widthProportion, (leftUpPosition[1] + 463) * highProportion)
                initiallyMatches = GetRunsImageText(runsInitiallyDetailImage, path, header, 0)
                if initiallyMatches:
                    #強化
                    AnalogMouseLeftClick((leftUpPosition[0] + 784) * widthProportion, (leftUpPosition[1] + 576) * highProportion)
                    #+6
                    AnalogMouseLeftClick((leftUpPosition[0] + 424) * widthProportion, (leftUpPosition[1] + 482) * highProportion)
                    #確定強化
                    AnalogMouseLeftClick((leftUpPosition[0] + 509) * widthProportion, (leftUpPosition[1] + 614) * highProportion)
                    #做OCR判斷是否符合規則
                    time.sleep(4)
                    runsFinallyDetailImage = GetScreenShot((leftUpPosition[0] + 749) * widthProportion, (leftUpPosition[1] + 362) * highProportion, (leftUpPosition[0] + 1022) * widthProportion, (leftUpPosition[1] + 497) * highProportion)
                    finallyMatch = GetRunsImageText(runsFinallyDetailImage, path, header, 1)
                    if finallyMatch:
                        #符合確定
                        AnalogMouseLeftClick((leftUpPosition[0] + 820) * widthProportion, (leftUpPosition[1] + 694) * highProportion)
                        #離開
                        AnalogMouseLeftClick((leftUpPosition[0] + 674) * widthProportion, (leftUpPosition[1] + 720) * highProportion)
                        #符合規則才有按叉
                        AnalogMouseLeftClick((leftUpPosition[0] + 927) * widthProportion, (leftUpPosition[1] + 186) * highProportion)
                    else:
                        #不符合出售
                        AnalogMouseLeftClick((leftUpPosition[0] + 591) * widthProportion, (leftUpPosition[1] + 696) * highProportion)
                        #賣掉傳說符文
                        AnalogMouseLeftClick((leftUpPosition[0] + 550) * widthProportion, (leftUpPosition[1] + 480) * highProportion)
                        #離開
                        AnalogMouseLeftClick((leftUpPosition[0] + 674) * widthProportion, (leftUpPosition[1] + 720) * highProportion)
                else:
                    #賣掉單獨符文
                    AnalogMouseLeftClick((leftUpPosition[0] + 562) * widthProportion, (leftUpPosition[1] + 589) * highProportion)
                    #賣掉傳說符文
                    AnalogMouseLeftClick((leftUpPosition[0] + 544) * widthProportion, (leftUpPosition[1] + 480) * highProportion)
        if i == 4:
            #滑動到符文頁面到最下面
            AnalogMouseLeftClickAndMove((leftUpPosition[0] + 1060) * widthProportion, (leftUpPosition[1] + 445) * highProportion, (leftUpPosition[0] + 1060) * widthProportion, (leftUpPosition[1] + 345) * highProportion)    
    #再來一次
    AnalogMouseLeftClick((leftUpPosition[0] + 713) * widthProportion, (leftUpPosition[1] + 674) * highProportion)
    AnalogMouseLeftClick((leftUpPosition[0] + 1118) * widthProportion, (leftUpPosition[1] + 589) * highProportion)
    #休眠
    AnalogMouseLeftClick((leftUpPosition[0] + 114) * widthProportion, (leftUpPosition[1] + 676) * highProportion)

if __name__ == '__main__':
    i = 0
    path = r'D:\tesseract\tesseract.exe'
    GetMouseClickPosition()
    hwnd = GetWindowNameAndType() #steam  windowName = 魔灵召唤 windowType = GLFW30 、 google play 模擬器  windowName = 魔靈召喚: 天空之役 windowType = CROSVM_1
    while i < 10:
        start = datetime.datetime.now()
        time.sleep(30)
        SetWindowToTop(hwnd)
        width, high, leftUpPosition = GetWindowSizeAndPostiion(hwnd)
        widthProportion, highProportion = WindowProportion(width, high)
        time.sleep(1)
        img = GetScreenShot((leftUpPosition[0] + 461) * widthProportion, (leftUpPosition[1] + 494) * highProportion, (leftUpPosition[0] + 931) * widthProportion, (leftUpPosition[1] + 573) * highProportion)
        battleEnd = GetContinuousBattleEndText(img, path)
        if battleEnd:
            if widthProportion == 1 and highProportion == 1:
                AutoRunsStepsProportion(leftUpPosition, 1, 1, path)
            else:
                AutoRunsStepsProportion(leftUpPosition, widthProportion, highProportion, path)
            i += 1
            end = datetime.datetime.now()
            print(end - start)
            print(i + 1)
        else:
            SetWindowMinimize(hwnd)
        print(width, high, leftUpPosition)
    #藍符文賣掉 亮度 = 69.6
    #圖標 亮度 = 121.9
    #紫符文 亮度 = 87.1
    #紫符文賣掉 亮度 = 73.1
    #橘符文 亮度 = 117.0
    #橘符文賣掉 亮度 = 76.0
    #神秘召喚書 亮度 = 122.8
    #左右相差106、108
    #上下相差106、101