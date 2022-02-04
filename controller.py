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
        self.img_path = 'dog.jpg'
        self.display_img()

    def display_img(self):
        self.img = cv2.imread(self.img_path)
        height, width, channel = self.img.shape
        print(height, width, channel)
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))