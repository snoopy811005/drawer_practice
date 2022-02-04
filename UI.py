# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_in.setGeometry(QtCore.QRect(940, 70, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btn_zoom_in.setFont(font)
        self.btn_zoom_in.setObjectName("btn_zoom_in")
        self.btn_zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_out.setGeometry(QtCore.QRect(1050, 70, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btn_zoom_out.setFont(font)
        self.btn_zoom_out.setObjectName("btn_zoom_out")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 901, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 897, 597))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(0, 0, 897, 597))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.label)
        self.verticalLayout.addWidget(self.scrollArea)
        self.label_img_shape_original = QtWidgets.QLabel(self.centralwidget)
        self.label_img_shape_original.setGeometry(QtCore.QRect(940, 150, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_img_shape_original.setFont(font)
        self.label_img_shape_original.setObjectName("label_img_shape_original")
        self.slider_zoom = QtWidgets.QSlider(self.centralwidget)
        self.slider_zoom.setGeometry(QtCore.QRect(940, 120, 201, 22))
        self.slider_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.slider_zoom.setObjectName("slider_zoom")
        self.label_ratio = QtWidgets.QLabel(self.centralwidget)
        self.label_ratio.setGeometry(QtCore.QRect(1160, 110, 111, 41))
        self.label_ratio.setObjectName("label_ratio")
        self.label_img_shape_current = QtWidgets.QLabel(self.centralwidget)
        self.label_img_shape_current.setGeometry(QtCore.QRect(940, 180, 301, 31))
        self.label_img_shape_current.setObjectName("label_img_shape_current")
        self.btn_open_image = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_image.setGeometry(QtCore.QRect(940, 30, 93, 28))
        self.btn_open_image.setObjectName("btn_open_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_zoom_in.setText(_translate("MainWindow", "zoom in"))
        self.btn_zoom_out.setText(_translate("MainWindow", "zoom out"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_img_shape_original.setText(_translate("MainWindow", "Original img shape = (1024, 768)"))
        self.label_ratio.setText(_translate("MainWindow", "Ratio:100%"))
        self.label_img_shape_current.setText(_translate("MainWindow", "Current img shape = (1024, 768)"))
        self.btn_open_image.setText(_translate("MainWindow", "open file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

