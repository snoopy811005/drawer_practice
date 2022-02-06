from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QIntValidator

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
        self.ui.btn_new_image.clicked.connect(self.new_file)
        self.ui.btn_open_image.clicked.connect(self.open_file)
        self.ui.btn_save_image.clicked.connect(self.save_file)
        self.ui.btn_save_as_image.clicked.connect(self.save_file_as)
        self.ui.btn_paint_point.clicked.connect(self.start_paint_point)
        self.ui.btn_paint_curve.clicked.connect(self.start_paint_curve)
        self.ui.btn_paint_line.clicked.connect(self.start_paint_line)
        self.ui.slider_zoom.valueChanged.connect(self.get_scale_slider_value)
        self.ui.edit_resize.returnPressed.connect(self.get_resize_value)

        # Step 3 -> set scrollArea property
        self.ui.scrollArea.setWidgetResizable(True) # activate scroll bar
        self.ui.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop) # align image at scrollArea's left_top

        # Step 4 -> activate mouseMoveEvent(setMouseTracking = True)
        self.ui.label.setMouseTracking(True)
        self.ui.label.mouseMoveEvent = self.img_controller.get_mouse_position

        # Step 5 -> activate mousePressEvent
        self.ui.label.mousePressEvent = self.img_controller.get_mouse_position

        # Step 6 -> set lineEdit property(input integer and range from 1 to 200)
        self.ui.edit_resize.setValidator(QIntValidator(1, 200))

    def new_file(self):
        self.img_path = 'image/empty.jpg'
        # initialize setting
        self.__initialize_setting('new')
        # read and display image
        self.img_controller.set_img_path(self.img_path)

    def open_file(self):
        img_format = ('bmp', 'jpeg', 'jpg', 'png', 'tiff', 'tif', 'pic')
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file", "./") # open current path dialog
        self.img_path = 'image/sad.jpg' if filename.split('.')[-1] not in img_format else filename
        # initialize setting
        self.__initialize_setting('open')
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

    def start_paint_point(self):
        # disable point button and enable curve & line button
        self.ui.btn_paint_point.setProperty("enabled", False)
        self.ui.btn_paint_curve.setProperty("enabled", True)
        self.ui.btn_paint_line.setProperty("enabled", True)
        # activate mouseMoveEvent(setMouseTracking = True)
        self.ui.label.setMouseTracking(True)
        self.ui.label.mouseMoveEvent = self.img_controller.do_nothing
        # activate mousePressEvent
        self.ui.label.mousePressEvent = self.img_controller.paint_point_or_curve

    def start_paint_curve(self):
        # disable curve button and enable point & line button
        self.ui.btn_paint_point.setProperty("enabled", True)
        self.ui.btn_paint_curve.setProperty("enabled", False)
        self.ui.btn_paint_line.setProperty("enabled", True)
        # activate mouseMoveEvent(setMouseTracking = False)
        self.ui.label.setMouseTracking(False)
        self.ui.label.mouseMoveEvent = self.img_controller.paint_point_or_curve
        # activate mousePressEvent
        self.ui.label.mousePressEvent = self.img_controller.paint_point_or_curve

    def start_paint_line(self):
        # disable line button and enable point & curve button
        self.ui.btn_paint_point.setProperty("enabled", True)
        self.ui.btn_paint_curve.setProperty("enabled", True)
        self.ui.btn_paint_line.setProperty("enabled", False)
        # activate mouseMoveEvent(setMouseTracking = True)
        self.ui.label.setMouseTracking(True)
        self.ui.label.mouseMoveEvent = self.img_controller.do_nothing
        # activate mousePressEvent
        self.ui.label.mousePressEvent = self.img_controller.paint_line

    def get_scale_slider_value(self):
        # scale and display image
        self.img_controller.set_slider_value(self.ui.slider_zoom.value())

    def get_resize_value(self):
        # resize and display image
        self.img_controller.set_resize_value(int(self.ui.edit_resize.text()))
        print(f"resize ratio = {int(self.ui.edit_resize.text())}%")

    def __initialize_setting(self, mode):
        # initialize image file path for save
        if mode == 'new':
            self.save_img_path = ''
        elif mode == 'open':
            self.save_img_path = '' if self.img_path == 'image/sad.jpg' else self.img_path
        # initialize slider value
        self.ui.slider_zoom.setProperty("value", 50)
        # initialize spin value
        self.ui.spin_color_red.setProperty("value", 0)
        self.ui.spin_color_green.setProperty("value", 0)
        self.ui.spin_color_blue.setProperty("value", 0)
        self.ui.spin_size.setProperty("value", 5)
        self.ui.edit_resize.setProperty("text", 100)
        # initialize point & curve & line button
        self.ui.btn_paint_point.setProperty("enabled", True)
        self.ui.btn_paint_curve.setProperty("enabled", True)
        self.ui.btn_paint_line.setProperty("enabled", True)
        # initialize mouse event
        self.ui.label.setMouseTracking(True)
        self.ui.label.mouseMoveEvent = self.img_controller.get_mouse_position
        self.ui.label.mousePressEvent = self.img_controller.get_mouse_position