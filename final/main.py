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
        self.update_display()

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
        #........
        #File Mangement Commands
        #........
        #command ls
        self.toolButton_35.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_6.text()))
        )
        self.toolButton_36.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_6.text()))
        )
        #command cd
        self.toolButton_113.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_45.text()))
        )
        self.toolButton_114.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_45.text()))
        )
        #command pwd
        self.toolButton_111.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_44.text()))
        )
        self.toolButton_112.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_44.text()))
        )
        #command mkdir
        self.toolButton_109.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_43.text()))
        )
        self.toolButton_110.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_43.text()))
        )
        #command rmdir
        self.toolButton_107.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_42.text()))
        )
        self.toolButton_108.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_42.text()))
        )
        #command touch
        self.toolButton_105.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_41.text()))
        )
        self.toolButton_106.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_41.text()))
        )
        #command cp
        self.toolButton_103.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_40.text()))
        )
        self.toolButton_104.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_40.text()))
        )
        #command mv
        self.toolButton_97.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_37.text()))
        )
        self.toolButton_98.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_37.text()))
        )
        #command rm
        self.toolButton_95.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_36.text()))
        )
        self.toolButton_96.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_36.text()))
        )
        #command cat
        self.toolButton_93.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_35.text()))
        )
        self.toolButton_94.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_35.text()))
        )
        #command more
        self.toolButton_91.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_34.text()))
        )
        self.toolButton_92.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_34.text()))
        )
        #command less
        self.toolButton_89.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_33.text()))
        )
        self.toolButton_90.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_33.text()))
        )
        #command grep
        self.toolButton_87.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_32.text()))
        )
        self.toolButton_88.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_32.text()))
        )
        #command chmod
        self.toolButton_85.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_31.text()))
        )
        self.toolButton_86.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_31.text()))
        )
        #command chown
        self.toolButton_83.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_30.text()))
        )
        self.toolButton_84.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_30.text()))
        )
        #command stat
        self.toolButton_81.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_29.text()))
        )
        self.toolButton_82.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_29.text()))
        )
        #command diff
        self.toolButton_77.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_27.text()))
        )
        self.toolButton_78.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_27.text()))
        )
        #command tar -cf
        self.toolButton_79.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_28.text()))
        )
        self.toolButton_80.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_28.text()))
        )
        #command tar -xf
        self.toolButton_117.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_47.text()))
        )
        self.toolButton_118.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_47.text()))
        )
        #command zip
        self.toolButton_123.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_50.text()))
        )
        self.toolButton_124.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_50.text()))
        )
        #command unzip
        self.toolButton_115.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_46.text()))
        )
        self.toolButton_116.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_46.text()))
        )
        #command rar
        self.toolButton_119.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_48.text()))
        )
        self.toolButton_120.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_48.text()))
        )
        #command unrar
        self.toolButton_121.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_49.text()))
        )
        self.toolButton_122.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_49.text()))
        )
        #........
        #Networking Commands
        #........
       #command ifconfig
        self.toolButton_39.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_8.text()))
        )
        self.toolButton_40.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_8.text()))
        )
        #command ip
        self.toolButton_147.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_62.text()))
        )
        self.toolButton_148.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_62.text()))
        )
        #command ping
        self.toolButton_155.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_66.text()))
        )
        self.toolButton_156.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_66.text()))
        )
        #command traceroute
        self.toolButton_127.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_52.text()))
        )
        self.toolButton_128.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_52.text()))
        )
        #command netstat
        self.toolButton_125.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_51.text()))
        )
        self.toolButton_126.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_51.text()))
        )
        #command ss
        self.toolButton_129.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_53.text()))
        )
        self.toolButton_130.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_53.text()))
        )
        #command route
        self.toolButton_143.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_60.text()))
        )
        self.toolButton_144.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_60.text()))
        )
        #command host
        self.toolButton_149.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_63.text()))
        )
        self.toolButton_150.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_63.text()))
        )
        #command dig
        self.toolButton_163.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_70.text()))
        )
        self.toolButton_164.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_70.text()))
        )
        #command iwconfig
        self.toolButton_157.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_67.text()))
        )
        self.toolButton_158.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_67.text()))
        )
        #command iw
        self.toolButton_167.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_72.text()))
        )
        self.toolButton_168.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_72.text()))
        )
        #command arp
        self.toolButton_153.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_65.text()))
        )
        self.toolButton_154.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_65.text()))
        )
        #command tcpdump
        self.toolButton_151.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_64.text()))
        )
        self.toolButton_152.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_64.text()))
        )
        #command nc
        self.toolButton_161.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_69.text()))
        )
        self.toolButton_162.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_69.text()))
        )
        #command nmap
        self.toolButton_159.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_68.text()))
        )
        self.toolButton_160.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_68.text()))
        )
        #command iptables
        self.toolButton_137.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_57.text()))
        )
        self.toolButton_138.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_57.text()))
        )
        #command ip6tables
        self.toolButton_131.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_54.text()))
        )
        self.toolButton_132.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_54.text()))
        )
        #command sshd
        self.toolButton_146.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_61.text()))
        )
        self.toolButton_145.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_61.text()))
        )
        #command wget
        self.toolButton_165.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_71.text()))
        )
        self.toolButton_166.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_71.text()))
        )
        #command curl
        self.toolButton_133.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_55.text()))
        )
        self.toolButton_134.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_55.text()))
        )
        #........
        #Process Mangement Commands
        #........
       #command uptime
        self.toolButton_41.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_9.text()))
        )
        self.toolButton_42.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_9.text()))
        )
        #command top
        self.toolButton_169.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_73.text()))
        )
        self.toolButton_170.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_73.text()))
        )
        #command ps
        self.toolButton_171.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_74.text()))
        )
        self.toolButton_172.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_74.text()))
        )
        #command htop
        self.toolButton_199.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_88.text()))
        )
        self.toolButton_200.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_88.text()))
        )
        #command kill
        self.toolButton_135.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_56.text()))
        )
        self.toolButton_136.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_56.text()))
        )
        #command killall
        self.toolButton_139.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_58.text()))
        )
        self.toolButton_140.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_58.text()))
        )
        #command systemctl
        self.toolButton_175.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_76.text()))
        )
        self.toolButton_176.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_76.text()))
        )
        #command systemctl
        self.toolButton_99.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_38.text()))
        )
        self.toolButton_101.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_38.text()))
        )
        #command systemctl
        self.toolButton_100.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_39.text()))
        )
        self.toolButton_102.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_39.text()))
        )
        #command journalctl
        self.toolButton_179.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_78.text()))
        )
        self.toolButton_180.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_78.text()))
        )
        #command df
        self.toolButton_197.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_87.text()))
        )
        self.toolButton_198.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_87.text()))
        )
        #command du
        self.toolButton_193.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_85.text()))
        )
        self.toolButton_194.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_85.text()))
        )
        #command free
        self.toolButton_189.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_83.text()))
        )
        self.toolButton_190.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_83.text()))
        )
        #command ps
        self.toolButton_195.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_86.text()))
        )
        self.toolButton_196.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_86.text()))
        )
        #command pkill
        self.toolButton_173.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_75.text()))
        )
        self.toolButton_174.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_75.text()))
        )
        #command reboot
        self.toolButton_182.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_79.text()))
        )
        self.toolButton_181.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_79.text()))
        )
        #command shutdown
        self.toolButton_187.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_82.text()))
        )
        self.toolButton_188.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_82.text()))
        )

        #........
        #User Mangement Commands
        #........
       #command useradd
        self.toolButton_43.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_10.text()))
        )
        self.toolButton_44.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_10.text()))
        )
        #command passwd
        self.toolButton_177.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_77.text()))
        )
        self.toolButton_178.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_77.text()))
        )
        #command userdel
        self.toolButton_183.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_80.text()))
        )
        self.toolButton_184.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_80.text()))
        )
        #command groupadd
        self.toolButton_227.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_102.text()))
        )
        self.toolButton_228.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_102.text()))
        )
        #command groupdel
        self.toolButton_141.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_59.text()))
        )
        self.toolButton_142.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_59.text()))
        )
        #command groups
        self.toolButton_191.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_84.text()))
        )
        self.toolButton_192.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_84.text()))
        )
        #command id
        self.toolButton_201.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_89.text()))
        )
        self.toolButton_202.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_89.text()))
        )
        #command who
        self.toolButton_207.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_92.text()))
        )
        self.toolButton_208.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_92.text()))
        )
        #command w
        self.toolButton_225.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_101.text()))
        )
        self.toolButton_226.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_101.text()))
        )
        #command finger
        self.toolButton_221.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_99.text()))
        )
        self.toolButton_222.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_99.text()))
        )
        #command chsh
        self.toolButton_217.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_97.text()))
        )
        self.toolButton_218.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_97.text()))
        )
        #command su
        self.toolButton_223.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_100.text()))
        )
        self.toolButton_224.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_100.text()))
        )
        #command sudo
        self.toolButton_185.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_81.text()))
        )
        self.toolButton_186.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_81.text()))
        )
        #command visudo
        self.toolButton_210.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_93.text()))
        )
        self.toolButton_209.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_93.text()))
        )
        #command chage
        self.toolButton_215.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_96.text()))
        )
        self.toolButton_216.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_96.text()))
        )
        #command last
        self.toolButton_213.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_95.text()))
        )
        self.toolButton_214.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_95.text()))
        )
        #command logname
        self.toolButton_203.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_90.text()))
        )
        self.toolButton_204.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_90.text()))
        )
        #command whoami
        self.toolButton_206.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_91.text()))
        )
        self.toolButton_205.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_91.text()))
        )
        #command su
        self.toolButton_211.clicked.connect(
            lambda: self.execute_command(str(self.lineEdit_94.text()))
        )
        self.toolButton_212.clicked.connect(
            lambda: self.copyToClipboard(str(self.lineEdit_94.text()))
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
