def WindowProportion(windowWidth, windowHigh):
    """計算視窗縮放比例"""
    windowOriginWidth, windowOriginHigh = 1339, 783
    widthProportion = windowWidth / windowOriginWidth
    highProportion = windowHigh / windowOriginHigh
    return widthProportion, highProportion