from PyQt5.QtGui import QImage, QPixmap
import cv2

class img_controller(object):
    def __init__(self, img_path, ui):
        self.img_path = img_path # image file path
        self.ui = ui # ui object

        self.img = None  # image with OpenCV type(BGR)
        self.qimg = None  # image with QImage type(RGB)
        self.qpixmap = None  # image with QPixmap type
        self.qpixmap_height = None  # get QPixmap's height for resize
        self.slider_value = 50 # slider value 50 = scale ratio 100%

        self.__read_img()
        self.__display_img()

    def set_zoom_in(self):
        # set slider value and move slider
        self.slider_value = max(1, self.slider_value - 1)
        self.__move_slider_whenZoom()
        # minimum value = original image * 0.02
        self.qpixmap_height = int(self.qpixmap.height() * (self.slider_value / 50))
        self.__display_img()

    def set_zoom_out(self):
        # set slider value and move slider
        self.slider_value = min(self.slider_value + 1, 100)
        self.__move_slider_whenZoom()
        # maximum value = original image * 2
        self.qpixmap_height = int(self.qpixmap.height() * (self.slider_value / 50))
        self.__display_img()

    def set_img_path(self, img_path):
        self.img_path = img_path
        self.__read_img()
        self.__display_img()

    def set_slider_value(self, slider_value):
        self.slider_value = slider_value
        self.qpixmap_height = int(self.qpixmap.height() * (slider_value / 50))
        self.__display_img()

    def save_img(self, path):
        self.qpixmap.save(path)

    def __read_img(self):
        # OpenCV type(BGR)
        try:
            self.img = cv2.imread(self.img_path)
        except:
            self.img = cv2.imread('image/sad.jpg')
        height, width, channel = self.img.shape
        print(f"height={height}, width={width}, channel={channel}")
        # QImage type(RGB)
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        # QPixmap type
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        # initialize slider value
        self.slider_value = 50

    def __display_img(self):
        # resize image
        scaled_qpixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        print(f"current img shape = ({scaled_qpixmap.width()}, {scaled_qpixmap.height()})")
        # display image
        self.ui.label.setPixmap(scaled_qpixmap)
        # display text(image shape)
        self.__display_text_imgShape((scaled_qpixmap.width(), scaled_qpixmap.height()))
        # display text(image ratio)
        self.__display_text_imgRatio()

    def __display_text_imgShape(self, scaledImgShape):
        self.ui.label_img_shape_original.setText(f"Original img shape = ({self.qpixmap.width()}, {self.qpixmap.height()})")
        self.ui.label_img_shape_current.setText(f"Current img shape = ({scaledImgShape[0]}, {scaledImgShape[1]})")

    def __display_text_imgRatio(self):
        ratio = int((self.slider_value / 50) * 100)
        self.ui.label_img_ratio.setText(f"Ratio:{ratio}%")

    def __move_slider_whenZoom(self):
        self.ui.slider_zoom.setProperty("value", self.slider_value)