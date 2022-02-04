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
        self.btn_zoom_in.setGeometry(QtCore.QRect(1020, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btn_zoom_in.setFont(font)
        self.btn_zoom_in.setObjectName("btn_zoom_in")
        self.btn_zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_out.setGeometry(QtCore.QRect(1150, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btn_zoom_out.setFont(font)
        self.btn_zoom_out.setObjectName("btn_zoom_out")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 901, 601))
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
        self.label_img_shape = QtWidgets.QLabel(self.centralwidget)
        self.label_img_shape.setGeometry(QtCore.QRect(1030, 70, 201, 20))
        self.label_img_shape.setObjectName("label_img_shape")
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
        self.label_img_shape.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

