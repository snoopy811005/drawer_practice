from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import os

from UI import Ui_MainWindow
from img_controller import img_controller

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # Step 1 -> read and display image
        self.img_path = 'image/empty.jpg'  # image file path
        self.save_img_path = '' # image file path for save
        self.img_controller = img_controller(img_path=self.img_path, ui=self.ui)

        # Step 2 -> set connection(when button clicked or slider moved)
        self.ui.btn_zoom_in.clicked.connect(self.img_controller.set_zoom_in)
        self.ui.btn_zoom_out.clicked.connect(self.img_controller.set_zoom_out)
        self.ui.btn_open_image.clicked.connect(self.open_file)
        self.ui.btn_save_image.clicked.connect(self.save_file)
        self.ui.btn_save_as_image.clicked.connect(self.save_file_as)
        self.ui.slider_zoom.valueChanged.connect(self.get_slider_value)

        # Step 3 -> set scrollArea property
        self.ui.scrollArea.setWidgetResizable(True) # activate scroll bar
        self.ui.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop) # align image at scrollArea's left_top

    def open_file(self):
        img_format = ('bmp', 'jpeg', 'jpg', 'png', 'tiff', 'tif', 'pic')
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file", "./") # open current path dialog
        self.img_path = 'image/sad.jpg' if filename.split('.')[-1] not in img_format else filename
        # initialize slider value
        self.ui.slider_zoom.setProperty("value", 50)
        # read and display image
        self.img_controller.set_img_path(self.img_path)

    def save_file(self):
        if self.save_img_path:
            self.img_controller.save_img(self.save_img_path)
        else:
            self.save_file_as()

    def save_file_as(self):
        img_format = "*.jpeg;;*.jpg;;*.png;;*.tiff"
        filename, filetype = QFileDialog.getSaveFileName(self, "Save file", 'new_image', img_format)
        # check file exists or not
        # if os.path.isfile(filename):
        #     format_len = len(filetype.split('.')[1])
        #     filename = filename[:-(format_len + 1)] + '(1).' + filetype.split('.')[1] # rename filename
        self.save_img_path = filename
        self.img_controller.save_img(filename)

    def get_slider_value(self):
        # scale and display image
        self.img_controller.set_slider_value(self.ui.slider_zoom.value())