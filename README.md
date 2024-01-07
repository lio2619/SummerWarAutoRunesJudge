## 使用程式和相關執行檔
### python

1. python version = 3.10.10
2. 使用套件安裝請參照以下指令
```powershell
python -m pip install -r requirements.txt
```

### 圖片比對
* 此程式是透過ssim來檢查圖片相似度

### OCR執行檔與訓練資料
1. 執行檔的[下載網站](https://github.com/UB-Mannheim/tesseract/wiki)
2. 訓練資料的[下載網站](https://github.com/tesseract-ocr/tessdata_best/blob/main/chi_tra.traineddata)
3. 將執行檔下載的路徑記起來，並且修改main.py裡面path的路徑成剛剛紀錄的

* 也可參考[這邊](https://github.com/lio2619/ProgramNotes/blob/main/python/%E4%BD%BF%E7%94%A8pytesseract%E5%A5%97%E4%BB%B6.md)的步驟

## 執行
```powershell
python main.py
```

## 執行影片

https://github.com/lio2619/SummerWarAutoRunesJudge/assets/30797096/4fb182f4-ae4d-45ed-a701-917991734cd4

