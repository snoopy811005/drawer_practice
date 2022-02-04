# drawer_practice

## *.py 功能介紹
- UI.py : 設計使用者介面的部分
- controller.py : 控制程式邏輯的部分
- start.py : 程式進入點

## Part_1
- 功能 : 使用 OpenCV 讀取圖檔，轉換成 QImage，透過 QPixmap 將圖檔顯示在 QLabel。
- 問題 : 圖檔解析度過大，造成只能顯示部分圖檔影像。

## Part_2
- 功能 : 建立可以縮放圖檔大小的按鈕。"zoom in" 按鈕縮小圖檔，高度最小值為原圖高度的 0.1 倍。
"zoom out" 按鈕放大圖檔，高度最大值為原圖高度的 2 倍。
- 問題 : 圖檔大小過大，仍然只能顯示部分圖檔影像。