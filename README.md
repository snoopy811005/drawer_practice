# drawer_practice

## *.py 功能介紹
- UI.py : 設計使用者介面的部分
- controller.py : 控制主程式邏輯的部分
- img_controller.py : 控制影像邏輯的部分
- start.py : 程式進入點

## Part_1
- 功能 : 使用 OpenCV 讀取圖檔，轉換成 QImage，透過 QPixmap 將圖檔顯示在 QLabel。
- 問題 : 圖檔解析度過大，造成只能顯示部分圖檔影像。

## Part_2
- 功能 : 建立可以縮放圖檔大小的按鈕。"zoom in" 按鈕縮小圖檔，高度最小值為原圖高度的 0.02 倍。
"zoom out" 按鈕放大圖檔，高度最大值為原圖高度的 2 倍。
- 問題 : 圖檔大小過大，仍然只能顯示部分圖檔影像。

## Part_3
- 功能 : 建立捲軸功能，使超過可視範圍的圖檔可以透過滾動捲軸觀看，克服圖檔過大造成只能顯示部分圖檔影像的問題。

## Part_4
- 功能 : 增加 "open file" 按鈕，讓使用者可以選擇圖檔。支援圖檔格式有 
('bmp', 'jpeg', 'jpg', 'png', 'tiff', 'tif', 'pic')。

## Part_5
- 功能 : 建立可以縮放圖檔大小的 slider。點擊 "zoom in" 按鈕或 "zoom out" 按鈕，slider 會相對應的移動。

## Part_6
- 功能 : 增加 "save file" 按鈕和 "save as ..." 按鈕，讓使用者可以儲存圖檔。
支援圖檔格式有 ('jpeg', 'jpg', 'png', 'tiff')。

## Part_7
- 功能 : 追蹤滑鼠座標。

## Part_8
- 功能 : 增加 "point" 按鈕和 "curve" 按鈕，讓使用者可以畫點或畫曲線。
- 問題 : 目前只能畫出固定的顏色及大小。

## Part_9
- 功能 : 增加 "line" 按鈕，讓使用者可以畫直線。
- 問題 : 目前仍然只能畫出固定的顏色及大小。

## Reference
1. https://www.wongwonggoods.com/python/pyqt5-1/
2. https://stackoverflow.com/questions/64214892/python-pyqt5-add-file-name-to-getsavefilename
3. https://stackoverflow.com/questions/41688668/how-to-return-mouse-coordinates-in-realtime