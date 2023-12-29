from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from UI import Ui_MainWindow as ui
from cryptography.fernet import Fernet
from pathlib import Path
import resources_rc
import subprocess
import sys
import os


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Changes()
        self.Handle_buttons()
        self.Handle_CLH_buttons()

    def UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_2.tabBar().setVisible(False)
        self.da_btn_clicked()
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.Encrypt_Decrypt_File_file_name = "#"
        #self.update_display()

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
        self.toolButton_4.clicked.connect(lambda: self.encrypt_file())
        self.toolButton_5.clicked.connect(lambda: self.decrypt_file())
        self.toolButton_219.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit.text()))
        )

    def Handle_CLH_buttons(self):
        self.toolButton_35.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_6.text()))
        )
        self.toolButton_36.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_6.text()))
        )

    def copyToClipboard(self, text):
        self.clipboard = QApplication.clipboard()
        self.clipboard.setText(text)

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
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            QMessageBox.information(self, "Error executing command", f"Y{e}")

    def update_display(self):
        self.display_disk_usage()
        self.display_disk_space()

    def get_disk_space(self):
        disk_info = os.statvfs("/")
        total_size = disk_info.f_blocks * disk_info.f_frsize
        free_size = disk_info.f_bfree * disk_info.f_frsize
        used_size = total_size - free_size
        return total_size, used_size, free_size

    def display_disk_space(self):
        total, used, free = self.get_disk_space()
        self.label_2.setText(str(self.format_size(total)))
        self.label_7.setText(str(self.format_size(used)))
        self.label_4.setText(str(self.format_size(free)))

    def get_disk_usage(self):
        labels = []
        sizes = []
        for partition in Path("/").glob("*"):
            partition_info = os.statvfs(partition)
            total_size = partition_info.f_blocks * partition_info.f_frsize
            free_size = partition_info.f_bfree * partition_info.f_frsize
            used_size = total_size - free_size

            labels.append(partition.name)
            sizes.append(used_size)

        return labels, sizes

    def display_disk_usage(self):
        labels, sizes = self.get_disk_usage()

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Partition", "Used Space"])
        self.tableWidget.setRowCount(len(labels))

        for i, label in enumerate(labels):
            partition_item = QTableWidgetItem(label)
            size_item = QTableWidgetItem(self.format_size(sizes[i]))
            self.tableWidget.setItem(i, 0, partition_item)
            self.tableWidget.setItem(i, 1, size_item)

    def format_size(self, size):
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
            
    ## ---------- Start Encrypt & Decrypt File ----------##
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.Encrypt_Decrypt_File_file_name = file_path
            self.label_6.setText("file selected")
            self.label_16.setText("file selected")
            event.accept()
        else:
            event.ignore()

    def encrypt_file(self):
        if self.Encrypt_Decrypt_File_file_name == "#":
            QMessageBox.information(self, "Error", "Please select file")
        else:
            file_path = self.Encrypt_Decrypt_File_file_name
            # Generate a random key
            key = Fernet.generate_key()

            # Encrypt the file
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = Fernet(key).encrypt(data)

            # Save the encrypted file
            with open(file_path + ".encrypted", "wb") as f:
                f.write(encrypted_data)

            self.lineEdit.setText(str(key.decode("utf-8")))
            self.label_6.setText("drop file here to encrypt it")
            self.label_16.setText("drop file here to decrypt it")
            self.Encrypt_Decrypt_File_file_name = "#"

    def decrypt_file(self):
        if self.Encrypt_Decrypt_File_file_name == "#":
            QMessageBox.information(self, "Error", "Please select file")
        else:
            file_path = self.Encrypt_Decrypt_File_file_name
            key = self.lineEdit_7.text()
            if key == "":
                QMessageBox.information(self, "Error", "Please enter the key")
            else:
                # Open the encrypted file
                with open(file_path, "rb") as f:
                    encrypted_data = f.read()

                # Decrypt the file
                decrypted_data = Fernet(key).decrypt(encrypted_data)

                # Save the decrypted file
                with open(file_path[:-10], "wb") as f:
                    f.write(decrypted_data)
                self.label_6.setText("drop file here to encrypt it")
                self.label_16.setText("drop file here to decrypt it")
                self.Encrypt_Decrypt_File_file_name = "#"
                self.lineEdit_7.setText("")
                
    ## ---------- End Encrypt & Decrypt File ----------##


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
