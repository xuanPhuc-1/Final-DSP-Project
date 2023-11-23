# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MenuWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FinalFFTWindow import Ui_MainWindow as Ui_MainWindow_FFT_Final
from FinalVADWindow import Ui_MainWindow as Ui_MainWindow_VAD_Final
from FinalLPFWindow import Ui_MainWindow as Ui_MainWindow_LPF_Final
from FinalWAVWindow import Ui_MainWindow as Ui_MainWindow_WAV_Final


class Ui_MainWindow(object):

    def on_click_fft(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_FFT_Final()
        self.ui.setupUi(self.window)
        self.window.show()

    def on_click_vad(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_VAD_Final()
        self.ui.setupUi(self.window)
        self.window.show()

    def on_click_lpf(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_LPF_Final()
        self.ui.setupUi(self.window)
        self.window.show()

    def on_click_wav(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_WAV_Final()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                                 "background-color:    rgb(218, 232, 252)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnFFT = QtWidgets.QPushButton(self.centralwidget)
        self.btnFFT.setGeometry(QtCore.QRect(60, 110, 310, 181))
        self.btnFFT.setStyleSheet("border-radius:20px;\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "border: 2px solid black;")
        self.btnFFT.setText("")
        self.btnFFT.setObjectName("btnFFT")
        self.btnFFT.clicked.connect(self.on_click_fft)
        self.btnLPF = QtWidgets.QPushButton(self.centralwidget)
        self.btnLPF.setGeometry(QtCore.QRect(420, 110, 310, 181))
        self.btnLPF.setStyleSheet("border-radius:20px;\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "border: 2px solid black;")
        self.btnLPF.clicked.connect(self.on_click_lpf)
        self.btnLPF.setText("")
        self.btnLPF.setObjectName("btnLPF")
        self.btnWVL = QtWidgets.QPushButton(self.centralwidget)
        self.btnWVL.setGeometry(QtCore.QRect(420, 310, 310, 181))
        self.btnWVL.setStyleSheet("border-radius:20px;\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "border: 2px solid black;")
        self.btnWVL.setText("")
        self.btnWVL.setObjectName("btnWVL")
        self.btnWVL.clicked.connect(self.on_click_wav)
        self.btnVAD = QtWidgets.QPushButton(self.centralwidget)
        self.btnVAD.setGeometry(QtCore.QRect(60, 310, 310, 181))
        self.btnVAD.setStyleSheet("border-radius:20px;\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "border: 2px solid black;")
        self.btnVAD.setText("")
        self.btnVAD.setObjectName("btnVAD")
        self.btnVAD.clicked.connect(self.on_click_vad)
        self.lbFFT = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT.setGeometry(QtCore.QRect(80, 150, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT.setFont(font)
        self.lbFFT.setStyleSheet("")
        self.lbFFT.setObjectName("lbFFT")
        self.lbFFT_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT_2.setGeometry(QtCore.QRect(490, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT_2.setFont(font)
        self.lbFFT_2.setStyleSheet("")
        self.lbFFT_2.setObjectName("lbFFT_2")
        self.lbFFT_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT_3.setGeometry(QtCore.QRect(80, 340, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT_3.setFont(font)
        self.lbFFT_3.setStyleSheet("")
        self.lbFFT_3.setObjectName("lbFFT_3")
        self.lbFFT_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT_4.setGeometry(QtCore.QRect(540, 340, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT_4.setFont(font)
        self.lbFFT_4.setStyleSheet("")
        self.lbFFT_4.setObjectName("lbFFT_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 190, 271, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 190, 271, 61))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 390, 271, 61))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 390, 271, 61))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 20, 561, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.lbFFT.setText(_translate(
            "MainWindow", "Fast Fourier Transform (FFT)"))
        self.lbFFT_2.setText(_translate("MainWindow", "Low Pass Filter (LPF)"))
        self.lbFFT_3.setText(_translate(
            "MainWindow", "Voice Activity Detector (VAD)"))
        self.lbFFT_4.setText(_translate("MainWindow", "Wavelet"))
        self.label.setText(_translate(
            "MainWindow", "A method for efficiently computing the discrete Fourier transform."))
        self.label_2.setText(_translate(
            "MainWindow", "A filter that allows signals with a frequency lower than a certain cutoff frequency to pass through, while attenuating frequencies higher than the cutoff."))
        self.label_3.setText(_translate(
            "MainWindow", "A system that identifies the presence or absence of human speech in an audio signal. It is commonly used in speech processing applications to distinguish between speech and non-speech segments."))
        self.label_4.setText(_translate(
            "MainWindow", "A mathematical tool used in signal processing and image compression. Wavelets are particularly effective in representing signals with sharp changes, such as audio signals and images."))
        self.label_5.setText(_translate(
            "MainWindow", "Denoising Data Methods Simulation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())