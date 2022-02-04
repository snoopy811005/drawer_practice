from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
import cv2

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # Step 1 -> read image
        self.img_path = 'dog.jpg' # image file path
        self.img = None # image with OpenCV type(BGR)
        self.qimg = None # image with QImage type(RGB)
        self.qpixmap = None # image with QPixmap type
        self.qpixmap_height = None # get QPixmap's height for resize
        self.__display_img()

        # Step 2 -> set connection(when button clicked)
        self.ui.btn_zoom_in.clicked.connect(self.set_zoom_in)
        self.ui.btn_zoom_out.clicked.connect(self.set_zoom_out)

    def set_zoom_in(self):
        # minimum value = original image * 10%
        self.qpixmap_height = max(int(self.qpixmap.height() * 0.1), self.qpixmap_height - 100)
        self.__resize_display_img()

    def set_zoom_out(self):
        # maximum value = original image * 200%
        self.qpixmap_height = min(self.qpixmap_height + 100, int(self.qpixmap.height() * 2))
        self.__resize_display_img()

    def __display_img(self):
        # OpenCV type(BGR)
        self.img = cv2.imread(self.img_path)
        height, width, channel = self.img.shape
        print(f'height={height}, width={width}, channel={channel}')
        # QImage type(RGB)
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        # QPixmap type
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        # display image
        self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))

    def __resize_display_img(self):
        # resize image
        scaled_qpixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        # display image
        self.ui.label.setPixmap(scaled_qpixmap)