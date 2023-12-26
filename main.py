from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
#from UI import Ui_MainWindow as ui
import resources_rc
import subprocess
import sys


ui, _ = loadUiType("./UI.ui")


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Changes()
        self.Handle_buttons()

    def UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_2.tabBar().setVisible(False)
        self.da_btn_clicked()
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)

    def Handle_buttons(self):
        self.lch_pushButton.clicked.connect(lambda: self.lch_btn_clicked())
        self.file_pushButton.clicked.connect(lambda: self.file_btn_clicked())
        self.da_pushButton.clicked.connect(lambda: self.da_btn_clicked())
        self.btn.clicked.connect(lambda: self.tabWidget_2.setCurrentIndex(0))
        self.btn1.clicked.connect(lambda: self.tabWidget_2.setCurrentIndex(1))
        self.btn2.clicked.connect(lambda: self.tabWidget_2.setCurrentIndex(2))
        self.btn3.clicked.connect(lambda: self.tabWidget_2.setCurrentIndex(3))
        self.btn_enc.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_dec.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        #self.toolButton_109.clicked.connect(
        #    lambda: self.execute_command(str(self.lineEdit_43.text()))
        #)

    def lch_btn_clicked(self):
        self.lch_pushButton.setStyleSheet(
            """QPushButton {
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: #00a884;
                border-bottom-color: transparent;
                border-width: 5px;
                background-color: rgb(45, 45, 45);
                }
            """
        )
        self.file_pushButton.setStyleSheet(
            """QPushButton {
                background-color: #202020;
                
                }
                QPushButton:hover {
                
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: transparent;
                border-bottom-color: transparent;
                border-width: 0px;
                background-color: #2d2d2d;
                }
            """
        )
        self.da_pushButton.setStyleSheet(
            """QPushButton {
                background-color: #202020;
                
                }
                QPushButton:hover {
                
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: transparent;
                border-bottom-color: transparent;
                border-width: 0px;
                background-color: #2d2d2d;
                }
            """
        )
        self.tabWidget.setCurrentIndex(0)

    def file_btn_clicked(self):
        self.lch_pushButton.setStyleSheet(
            """QPushButton {
                background-color: #202020;
                
                }
                QPushButton:hover {
                
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: transparent;
                border-bottom-color: transparent;
                border-width: 0px;
                background-color: #2d2d2d;
                }
            """
        )
        self.file_pushButton.setStyleSheet(
            """QPushButton {
                
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: #00a884;
                border-bottom-color: transparent;
                border-width: 5px;
                background-color: rgb(45, 45, 45);
                }
            """
        )
        self.da_pushButton.setStyleSheet(
            """QPushButton {
                background-color: #202020;
                
                }
                QPushButton:hover {
                
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: transparent;
                border-bottom-color: transparent;
                border-width: 0px;
                background-color: #2d2d2d;
                }
            """
        )
        self.tabWidget.setCurrentIndex(1)

    def da_btn_clicked(self):
        self.lch_pushButton.setStyleSheet(
            """QPushButton {
                background-color: #202020;
                
                }
                QPushButton:hover {
                
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: transparent;
                border-bottom-color: transparent;
                border-width: 0px;
                background-color: #2d2d2d;
                }
            """
        )
        self.file_pushButton.setStyleSheet(
            """QPushButton {
                background-color: #202020;
                
                }
                QPushButton:hover {
                
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: transparent;
                border-bottom-color: transparent;
                border-width: 0px;
                background-color: #2d2d2d;
                }
            """
        )
        self.da_pushButton.setStyleSheet(
            """QPushButton {
                
                border-style: solid;
                border-top-color: transparent;
                border-right-color: transparent;
                border-left-color: #00a884;
                border-bottom-color: transparent;
                border-width: 5px;
                background-color: rgb(45, 45, 45);
                }
            """
        )
        self.tabWidget.setCurrentIndex(2)

    def execute_command(self, command):
        print("command", command)
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
