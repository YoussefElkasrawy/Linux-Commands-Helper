from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(1200, 800))
        palette = QPalette()
        brush = QBrush(QColor(0, 168, 132, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(39, 39, 39, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 168, 132, 128))
        brush2.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(0, 168, 132, 128))
        brush3.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 168, 132, 128))
        brush4.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
        # endif
        MainWindow.setPalette(palette)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(":/images/icons/cil-map.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: rgb(39, 39, 39);\n" "color: #00a884;\n" "\n" ""
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('font: 63 11pt "Yu Gothic UI Semibold";')
        self.gridLayout_20 = QGridLayout(self.centralwidget)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setMaximumSize(QSize(100, 16777215))
        self.frame.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "\n"
            "}\n"
            "QPushButton {\n"
            "                background-color: #202020;\n"
            "                border-style: solid;\n"
            "                border-top-color: transparent;\n"
            "                border-right-color: transparent;\n"
            "                border-left-color: transparent;\n"
            "                border-bottom-color: transparent;\n"
            "                border-width: 0px;\n"
            " }\n"
            " QPushButton:hover {\n"
            "                border-style: solid;\n"
            "                border-top-color: transparent;\n"
            "                border-right-color: transparent;\n"
            "                border-left-color: transparent;\n"
            "                border-bottom-color: transparent;\n"
            "                border-width: 0px;\n"
            "                background-color: #2d2d2d;\n"
            "}\n"
            "/*\n"
            "QPushButton\n"
            "{\n"
            "background-color: #202020;\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-c"
            "olor: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            "}*/"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.file_pushButton = QPushButton(self.frame)
        self.file_pushButton.setObjectName("file_pushButton")
        self.file_pushButton.setMinimumSize(QSize(100, 266))
        self.file_pushButton.setMaximumSize(QSize(100, 16777215))
        icon1 = QIcon()
        icon1.addFile(":/images/icons/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.file_pushButton.setIcon(icon1)

        self.gridLayout_2.addWidget(self.file_pushButton, 2, 0, 1, 1)

        self.lch_pushButton = QPushButton(self.frame)
        self.lch_pushButton.setObjectName("lch_pushButton")
        self.lch_pushButton.setMinimumSize(QSize(100, 266))
        self.lch_pushButton.setMaximumSize(QSize(100, 16777215))
        self.lch_pushButton.setStyleSheet("")
        icon2 = QIcon()
        icon2.addFile(
            ":/images/icons/cil-chevron-double-right.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.lch_pushButton.setIcon(icon2)

        self.gridLayout_2.addWidget(self.lch_pushButton, 1, 0, 1, 1)

        self.da_pushButton = QPushButton(self.frame)
        self.da_pushButton.setObjectName("da_pushButton")
        self.da_pushButton.setMinimumSize(QSize(100, 266))
        self.da_pushButton.setMaximumSize(QSize(100, 16777215))
        icon3 = QIcon()
        icon3.addFile(
            ":/images/icons/cil-chart-pie.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.da_pushButton.setIcon(icon3)

        self.gridLayout_2.addWidget(self.da_pushButton, 0, 0, 1, 1)

        self.gridLayout_20.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet(
            "QTabWidget\n"
            "{\n"
            "	border-width: 0px;\n"
            "}\n"
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style"
            ": solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            " "
            "  border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar"
            "::sub-page:vertical\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            ""
            "\n"
            "QScrollBar::sub-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "QTableWidget {\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QTableWidget QHeaderView::section {\n"
            "    background-color: #00a884;\n"
            "    color: white;\n"
            "    padding: 5px;\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QTableWidget::item {\n"
            "    border: 1px solid #222222;\n"
            "    padding: 5px;\n"
            '    font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTableWidget::item:selected {\n"
            "    background-color: #404040;\n"
            "  "
            "  color: white;\n"
            "}\n"
            ""
        )
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setStyleSheet(
            "QTabWidget\n"
            "{\n"
            "	border-style: solid;\n"
            "	border-top-color: transparent;\n"
            "	border-right-color: transparent;\n"
            "	border-left-color: transparent;\n"
            "	border-bottom-color: transparent;\n"
            "	border-width: 0px;\n"
            "}"
        )
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QGridLayout(self.tab_4)
        self.gridLayout_7.setSpacing(10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.tab_4)
        self.frame_22.setObjectName("frame_22")
        self.frame_22.setMinimumSize(QSize(0, 60))
        self.frame_22.setMaximumSize(QSize(16777215, 60))
        self.frame_22.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_22)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_30.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.label_11 = QLabel(self.frame_22)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')

        self.gridLayout_30.addWidget(self.label_11, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_30.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.gridLayout_7.addWidget(self.frame_22, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.tab_4)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet(
            "	border-style: solid;\n"
            "	border-top-color: transparent;\n"
            "	border-right-color: transparent;\n"
            "	border-left-color: transparent;\n"
            "	border-bottom-color: transparent;\n"
            "	border-width: 0px;"
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 958, 4440))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.setContentsMargins(20, 20, 20, 20)
        self.frame_97 = QFrame(self.scrollAreaWidgetContents)
        self.frame_97.setObjectName("frame_97")
        self.frame_97.setMinimumSize(QSize(0, 200))
        self.frame_97.setMaximumSize(QSize(16777215, 200))
        self.frame_97.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.gridLayout_106 = QGridLayout(self.frame_97)
        self.gridLayout_106.setObjectName("gridLayout_106")
        self.gridLayout_106.setContentsMargins(20, 20, 20, 20)
        self.label_99 = QLabel(self.frame_97)
        self.label_99.setObjectName("label_99")
        self.label_99.setMinimumSize(QSize(70, 30))
        self.label_99.setMaximumSize(QSize(70, 30))
        self.label_99.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_99.setTextFormat(Qt.AutoText)
        self.label_99.setScaledContents(True)
        self.label_99.setAlignment(Qt.AlignCenter)
        self.label_99.setWordWrap(False)
        self.label_99.setOpenExternalLinks(False)

        self.gridLayout_106.addWidget(self.label_99, 0, 0, 1, 1)

        self.label_100 = QLabel(self.frame_97)
        self.label_100.setObjectName("label_100")

        self.gridLayout_106.addWidget(self.label_100, 0, 1, 1, 1)

        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName("frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.gridLayout_107 = QGridLayout(self.frame_98)
        self.gridLayout_107.setObjectName("gridLayout_107")
        self.gridLayout_107.setHorizontalSpacing(5)
        self.gridLayout_107.setContentsMargins(0, 0, 0, 0)
        self.toolButton_107 = QToolButton(self.frame_98)
        self.toolButton_107.setObjectName("toolButton_107")
        self.toolButton_107.setMinimumSize(QSize(50, 50))
        self.toolButton_107.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(
            ":/images/icons/cil-caret-right.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.toolButton_107.setIcon(icon4)

        self.gridLayout_107.addWidget(self.toolButton_107, 0, 1, 1, 1)

        self.lineEdit_42 = QLineEdit(self.frame_98)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_42.setMinimumSize(QSize(0, 50))

        self.gridLayout_107.addWidget(self.lineEdit_42, 0, 0, 1, 1)

        self.toolButton_108 = QToolButton(self.frame_98)
        self.toolButton_108.setObjectName("toolButton_108")
        self.toolButton_108.setMinimumSize(QSize(50, 50))
        self.toolButton_108.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(":/images/icons/cil-clone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_108.setIcon(icon5)

        self.gridLayout_107.addWidget(self.toolButton_108, 0, 2, 1, 1)

        self.gridLayout_106.addWidget(self.frame_98, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_97, 4, 0, 1, 1)

        self.frame_99 = QFrame(self.scrollAreaWidgetContents)
        self.frame_99.setObjectName("frame_99")
        self.frame_99.setMinimumSize(QSize(0, 200))
        self.frame_99.setMaximumSize(QSize(16777215, 200))
        self.frame_99.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.gridLayout_108 = QGridLayout(self.frame_99)
        self.gridLayout_108.setObjectName("gridLayout_108")
        self.gridLayout_108.setContentsMargins(20, 20, 20, 20)
        self.label_101 = QLabel(self.frame_99)
        self.label_101.setObjectName("label_101")
        self.label_101.setMinimumSize(QSize(70, 30))
        self.label_101.setMaximumSize(QSize(70, 30))
        self.label_101.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_101.setTextFormat(Qt.AutoText)
        self.label_101.setScaledContents(True)
        self.label_101.setAlignment(Qt.AlignCenter)
        self.label_101.setWordWrap(False)
        self.label_101.setOpenExternalLinks(False)

        self.gridLayout_108.addWidget(self.label_101, 0, 0, 1, 1)

        self.label_102 = QLabel(self.frame_99)
        self.label_102.setObjectName("label_102")

        self.gridLayout_108.addWidget(self.label_102, 0, 1, 1, 1)

        self.frame_100 = QFrame(self.frame_99)
        self.frame_100.setObjectName("frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.gridLayout_109 = QGridLayout(self.frame_100)
        self.gridLayout_109.setObjectName("gridLayout_109")
        self.gridLayout_109.setHorizontalSpacing(5)
        self.gridLayout_109.setContentsMargins(0, 0, 0, 0)
        self.toolButton_109 = QToolButton(self.frame_100)
        self.toolButton_109.setObjectName("toolButton_109")
        self.toolButton_109.setMinimumSize(QSize(50, 50))
        self.toolButton_109.setMaximumSize(QSize(50, 50))
        self.toolButton_109.setIcon(icon4)

        self.gridLayout_109.addWidget(self.toolButton_109, 0, 1, 1, 1)

        self.lineEdit_43 = QLineEdit(self.frame_100)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_43.setMinimumSize(QSize(0, 50))

        self.gridLayout_109.addWidget(self.lineEdit_43, 0, 0, 1, 1)

        self.toolButton_110 = QToolButton(self.frame_100)
        self.toolButton_110.setObjectName("toolButton_110")
        self.toolButton_110.setMinimumSize(QSize(50, 50))
        self.toolButton_110.setMaximumSize(QSize(50, 50))
        self.toolButton_110.setIcon(icon5)

        self.gridLayout_109.addWidget(self.toolButton_110, 0, 2, 1, 1)

        self.gridLayout_108.addWidget(self.frame_100, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_99, 3, 0, 1, 1)

        self.frame_95 = QFrame(self.scrollAreaWidgetContents)
        self.frame_95.setObjectName("frame_95")
        self.frame_95.setMinimumSize(QSize(0, 200))
        self.frame_95.setMaximumSize(QSize(16777215, 200))
        self.frame_95.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.gridLayout_104 = QGridLayout(self.frame_95)
        self.gridLayout_104.setObjectName("gridLayout_104")
        self.gridLayout_104.setContentsMargins(20, 20, 20, 20)
        self.label_97 = QLabel(self.frame_95)
        self.label_97.setObjectName("label_97")
        self.label_97.setMinimumSize(QSize(70, 30))
        self.label_97.setMaximumSize(QSize(70, 30))
        self.label_97.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_97.setTextFormat(Qt.AutoText)
        self.label_97.setScaledContents(True)
        self.label_97.setAlignment(Qt.AlignCenter)
        self.label_97.setWordWrap(False)
        self.label_97.setOpenExternalLinks(False)

        self.gridLayout_104.addWidget(self.label_97, 0, 0, 1, 1)

        self.label_98 = QLabel(self.frame_95)
        self.label_98.setObjectName("label_98")

        self.gridLayout_104.addWidget(self.label_98, 0, 1, 1, 1)

        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName("frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.gridLayout_105 = QGridLayout(self.frame_96)
        self.gridLayout_105.setObjectName("gridLayout_105")
        self.gridLayout_105.setHorizontalSpacing(5)
        self.gridLayout_105.setContentsMargins(0, 0, 0, 0)
        self.toolButton_105 = QToolButton(self.frame_96)
        self.toolButton_105.setObjectName("toolButton_105")
        self.toolButton_105.setMinimumSize(QSize(50, 50))
        self.toolButton_105.setMaximumSize(QSize(50, 50))
        self.toolButton_105.setIcon(icon4)

        self.gridLayout_105.addWidget(self.toolButton_105, 0, 1, 1, 1)

        self.lineEdit_41 = QLineEdit(self.frame_96)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_41.setMinimumSize(QSize(0, 50))

        self.gridLayout_105.addWidget(self.lineEdit_41, 0, 0, 1, 1)

        self.toolButton_106 = QToolButton(self.frame_96)
        self.toolButton_106.setObjectName("toolButton_106")
        self.toolButton_106.setMinimumSize(QSize(50, 50))
        self.toolButton_106.setMaximumSize(QSize(50, 50))
        self.toolButton_106.setIcon(icon5)

        self.gridLayout_105.addWidget(self.toolButton_106, 0, 2, 1, 1)

        self.gridLayout_104.addWidget(self.frame_96, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_95, 5, 0, 1, 1)

        self.frame_69 = QFrame(self.scrollAreaWidgetContents)
        self.frame_69.setObjectName("frame_69")
        self.frame_69.setMinimumSize(QSize(0, 200))
        self.frame_69.setMaximumSize(QSize(16777215, 200))
        self.frame_69.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.gridLayout_76 = QGridLayout(self.frame_69)
        self.gridLayout_76.setObjectName("gridLayout_76")
        self.gridLayout_76.setContentsMargins(20, 20, 20, 20)
        self.label_69 = QLabel(self.frame_69)
        self.label_69.setObjectName("label_69")
        self.label_69.setMinimumSize(QSize(50, 30))
        self.label_69.setMaximumSize(QSize(50, 30))
        self.label_69.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_69.setTextFormat(Qt.AutoText)
        self.label_69.setScaledContents(True)
        self.label_69.setAlignment(Qt.AlignCenter)
        self.label_69.setWordWrap(False)
        self.label_69.setOpenExternalLinks(False)

        self.gridLayout_76.addWidget(self.label_69, 0, 0, 1, 1)

        self.label_70 = QLabel(self.frame_69)
        self.label_70.setObjectName("label_70")

        self.gridLayout_76.addWidget(self.label_70, 0, 1, 1, 1)

        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName("frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.gridLayout_77 = QGridLayout(self.frame_70)
        self.gridLayout_77.setObjectName("gridLayout_77")
        self.gridLayout_77.setHorizontalSpacing(5)
        self.gridLayout_77.setContentsMargins(0, 0, 0, 0)
        self.toolButton_77 = QToolButton(self.frame_70)
        self.toolButton_77.setObjectName("toolButton_77")
        self.toolButton_77.setMinimumSize(QSize(50, 50))
        self.toolButton_77.setMaximumSize(QSize(50, 50))
        self.toolButton_77.setIcon(icon4)

        self.gridLayout_77.addWidget(self.toolButton_77, 0, 1, 1, 1)

        self.lineEdit_27 = QLineEdit(self.frame_70)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(0, 50))

        self.gridLayout_77.addWidget(self.lineEdit_27, 0, 0, 1, 1)

        self.toolButton_78 = QToolButton(self.frame_70)
        self.toolButton_78.setObjectName("toolButton_78")
        self.toolButton_78.setMinimumSize(QSize(50, 50))
        self.toolButton_78.setMaximumSize(QSize(50, 50))
        self.toolButton_78.setIcon(icon5)

        self.gridLayout_77.addWidget(self.toolButton_78, 0, 2, 1, 1)

        self.gridLayout_76.addWidget(self.frame_70, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_69, 16, 0, 1, 1)

        self.frame_113 = QFrame(self.scrollAreaWidgetContents)
        self.frame_113.setObjectName("frame_113")
        self.frame_113.setMinimumSize(QSize(0, 200))
        self.frame_113.setMaximumSize(QSize(16777215, 200))
        self.frame_113.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.gridLayout_122 = QGridLayout(self.frame_113)
        self.gridLayout_122.setObjectName("gridLayout_122")
        self.gridLayout_122.setContentsMargins(20, 20, 20, 20)
        self.label_115 = QLabel(self.frame_113)
        self.label_115.setObjectName("label_115")
        self.label_115.setMinimumSize(QSize(100, 30))
        self.label_115.setMaximumSize(QSize(100, 30))
        self.label_115.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_115.setTextFormat(Qt.AutoText)
        self.label_115.setScaledContents(True)
        self.label_115.setAlignment(Qt.AlignCenter)
        self.label_115.setWordWrap(False)
        self.label_115.setOpenExternalLinks(False)

        self.gridLayout_122.addWidget(self.label_115, 0, 0, 1, 1)

        self.label_116 = QLabel(self.frame_113)
        self.label_116.setObjectName("label_116")

        self.gridLayout_122.addWidget(self.label_116, 0, 1, 1, 1)

        self.frame_114 = QFrame(self.frame_113)
        self.frame_114.setObjectName("frame_114")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.gridLayout_123 = QGridLayout(self.frame_114)
        self.gridLayout_123.setObjectName("gridLayout_123")
        self.gridLayout_123.setHorizontalSpacing(5)
        self.gridLayout_123.setContentsMargins(0, 0, 0, 0)
        self.toolButton_123 = QToolButton(self.frame_114)
        self.toolButton_123.setObjectName("toolButton_123")
        self.toolButton_123.setMinimumSize(QSize(50, 50))
        self.toolButton_123.setMaximumSize(QSize(50, 50))
        self.toolButton_123.setIcon(icon4)

        self.gridLayout_123.addWidget(self.toolButton_123, 0, 1, 1, 1)

        self.toolButton_124 = QToolButton(self.frame_114)
        self.toolButton_124.setObjectName("toolButton_124")
        self.toolButton_124.setMinimumSize(QSize(50, 50))
        self.toolButton_124.setMaximumSize(QSize(50, 50))
        self.toolButton_124.setIcon(icon5)

        self.gridLayout_123.addWidget(self.toolButton_124, 0, 2, 1, 1)

        self.lineEdit_50 = QLineEdit(self.frame_114)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.lineEdit_50.setMinimumSize(QSize(0, 50))

        self.gridLayout_123.addWidget(self.lineEdit_50, 0, 0, 1, 1)

        self.lineEdit_46 = QLineEdit(self.frame_114)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_46.setMinimumSize(QSize(0, 50))

        self.gridLayout_123.addWidget(self.lineEdit_46, 1, 0, 1, 1)

        self.toolButton_115 = QToolButton(self.frame_114)
        self.toolButton_115.setObjectName("toolButton_115")
        self.toolButton_115.setMinimumSize(QSize(50, 50))
        self.toolButton_115.setMaximumSize(QSize(50, 50))
        self.toolButton_115.setIcon(icon4)

        self.gridLayout_123.addWidget(self.toolButton_115, 1, 1, 1, 1)

        self.toolButton_116 = QToolButton(self.frame_114)
        self.toolButton_116.setObjectName("toolButton_116")
        self.toolButton_116.setMinimumSize(QSize(50, 50))
        self.toolButton_116.setMaximumSize(QSize(50, 50))
        self.toolButton_116.setIcon(icon5)

        self.gridLayout_123.addWidget(self.toolButton_116, 1, 2, 1, 1)

        self.gridLayout_122.addWidget(self.frame_114, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_113, 19, 0, 1, 1)

        self.frame_73 = QFrame(self.scrollAreaWidgetContents)
        self.frame_73.setObjectName("frame_73")
        self.frame_73.setMinimumSize(QSize(0, 200))
        self.frame_73.setMaximumSize(QSize(16777215, 200))
        self.frame_73.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.gridLayout_80 = QGridLayout(self.frame_73)
        self.gridLayout_80.setObjectName("gridLayout_80")
        self.gridLayout_80.setContentsMargins(20, 20, 20, 20)
        self.label_73 = QLabel(self.frame_73)
        self.label_73.setObjectName("label_73")
        self.label_73.setMinimumSize(QSize(60, 30))
        self.label_73.setMaximumSize(QSize(60, 30))
        self.label_73.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_73.setTextFormat(Qt.AutoText)
        self.label_73.setScaledContents(True)
        self.label_73.setAlignment(Qt.AlignCenter)
        self.label_73.setWordWrap(False)
        self.label_73.setOpenExternalLinks(False)

        self.gridLayout_80.addWidget(self.label_73, 0, 0, 1, 1)

        self.label_74 = QLabel(self.frame_73)
        self.label_74.setObjectName("label_74")

        self.gridLayout_80.addWidget(self.label_74, 0, 1, 1, 1)

        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName("frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.gridLayout_81 = QGridLayout(self.frame_74)
        self.gridLayout_81.setObjectName("gridLayout_81")
        self.gridLayout_81.setHorizontalSpacing(5)
        self.gridLayout_81.setContentsMargins(0, 0, 0, 0)
        self.toolButton_81 = QToolButton(self.frame_74)
        self.toolButton_81.setObjectName("toolButton_81")
        self.toolButton_81.setMinimumSize(QSize(50, 50))
        self.toolButton_81.setMaximumSize(QSize(50, 50))
        self.toolButton_81.setIcon(icon4)

        self.gridLayout_81.addWidget(self.toolButton_81, 0, 1, 1, 1)

        self.lineEdit_29 = QLineEdit(self.frame_74)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_29.setMinimumSize(QSize(0, 50))

        self.gridLayout_81.addWidget(self.lineEdit_29, 0, 0, 1, 1)

        self.toolButton_82 = QToolButton(self.frame_74)
        self.toolButton_82.setObjectName("toolButton_82")
        self.toolButton_82.setMinimumSize(QSize(50, 50))
        self.toolButton_82.setMaximumSize(QSize(50, 50))
        self.toolButton_82.setIcon(icon5)

        self.gridLayout_81.addWidget(self.toolButton_82, 0, 2, 1, 1)

        self.gridLayout_80.addWidget(self.frame_74, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_73, 15, 0, 1, 1)

        self.frame_109 = QFrame(self.scrollAreaWidgetContents)
        self.frame_109.setObjectName("frame_109")
        self.frame_109.setMinimumSize(QSize(0, 200))
        self.frame_109.setMaximumSize(QSize(16777215, 200))
        self.frame_109.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.gridLayout_118 = QGridLayout(self.frame_109)
        self.gridLayout_118.setObjectName("gridLayout_118")
        self.gridLayout_118.setContentsMargins(20, 20, 20, 20)
        self.label_111 = QLabel(self.frame_109)
        self.label_111.setObjectName("label_111")
        self.label_111.setMinimumSize(QSize(100, 30))
        self.label_111.setMaximumSize(QSize(100, 30))
        self.label_111.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_111.setTextFormat(Qt.AutoText)
        self.label_111.setScaledContents(True)
        self.label_111.setAlignment(Qt.AlignCenter)
        self.label_111.setWordWrap(False)
        self.label_111.setOpenExternalLinks(False)

        self.gridLayout_118.addWidget(self.label_111, 0, 0, 1, 1)

        self.label_112 = QLabel(self.frame_109)
        self.label_112.setObjectName("label_112")

        self.gridLayout_118.addWidget(self.label_112, 0, 1, 1, 1)

        self.frame_110 = QFrame(self.frame_109)
        self.frame_110.setObjectName("frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.gridLayout_119 = QGridLayout(self.frame_110)
        self.gridLayout_119.setObjectName("gridLayout_119")
        self.gridLayout_119.setHorizontalSpacing(5)
        self.gridLayout_119.setContentsMargins(0, 0, 0, 0)
        self.toolButton_120 = QToolButton(self.frame_110)
        self.toolButton_120.setObjectName("toolButton_120")
        self.toolButton_120.setMinimumSize(QSize(50, 50))
        self.toolButton_120.setMaximumSize(QSize(50, 50))
        self.toolButton_120.setIcon(icon5)

        self.gridLayout_119.addWidget(self.toolButton_120, 0, 2, 1, 1)

        self.lineEdit_48 = QLineEdit(self.frame_110)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.lineEdit_48.setMinimumSize(QSize(0, 50))

        self.gridLayout_119.addWidget(self.lineEdit_48, 0, 0, 1, 1)

        self.toolButton_119 = QToolButton(self.frame_110)
        self.toolButton_119.setObjectName("toolButton_119")
        self.toolButton_119.setMinimumSize(QSize(50, 50))
        self.toolButton_119.setMaximumSize(QSize(50, 50))
        self.toolButton_119.setIcon(icon4)

        self.gridLayout_119.addWidget(self.toolButton_119, 0, 1, 1, 1)

        self.lineEdit_49 = QLineEdit(self.frame_110)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_49.setMinimumSize(QSize(0, 50))

        self.gridLayout_119.addWidget(self.lineEdit_49, 1, 0, 1, 1)

        self.toolButton_121 = QToolButton(self.frame_110)
        self.toolButton_121.setObjectName("toolButton_121")
        self.toolButton_121.setMinimumSize(QSize(50, 50))
        self.toolButton_121.setMaximumSize(QSize(50, 50))
        self.toolButton_121.setIcon(icon4)

        self.gridLayout_119.addWidget(self.toolButton_121, 1, 1, 1, 1)

        self.toolButton_122 = QToolButton(self.frame_110)
        self.toolButton_122.setObjectName("toolButton_122")
        self.toolButton_122.setMinimumSize(QSize(50, 50))
        self.toolButton_122.setMaximumSize(QSize(50, 50))
        self.toolButton_122.setIcon(icon5)

        self.gridLayout_119.addWidget(self.toolButton_122, 1, 2, 1, 1)

        self.gridLayout_118.addWidget(self.frame_110, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_109, 20, 0, 1, 1)

        self.frame_91 = QFrame(self.scrollAreaWidgetContents)
        self.frame_91.setObjectName("frame_91")
        self.frame_91.setMinimumSize(QSize(0, 200))
        self.frame_91.setMaximumSize(QSize(16777215, 200))
        self.frame_91.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.gridLayout_102 = QGridLayout(self.frame_91)
        self.gridLayout_102.setObjectName("gridLayout_102")
        self.gridLayout_102.setContentsMargins(20, 20, 20, 20)
        self.label_95 = QLabel(self.frame_91)
        self.label_95.setObjectName("label_95")
        self.label_95.setMinimumSize(QSize(30, 30))
        self.label_95.setMaximumSize(QSize(30, 30))
        self.label_95.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_95.setTextFormat(Qt.AutoText)
        self.label_95.setScaledContents(True)
        self.label_95.setAlignment(Qt.AlignCenter)
        self.label_95.setWordWrap(False)
        self.label_95.setOpenExternalLinks(False)

        self.gridLayout_102.addWidget(self.label_95, 0, 0, 1, 1)

        self.label_96 = QLabel(self.frame_91)
        self.label_96.setObjectName("label_96")

        self.gridLayout_102.addWidget(self.label_96, 0, 1, 1, 1)

        self.frame_94 = QFrame(self.frame_91)
        self.frame_94.setObjectName("frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.gridLayout_103 = QGridLayout(self.frame_94)
        self.gridLayout_103.setObjectName("gridLayout_103")
        self.gridLayout_103.setHorizontalSpacing(5)
        self.gridLayout_103.setContentsMargins(0, 0, 0, 0)
        self.toolButton_103 = QToolButton(self.frame_94)
        self.toolButton_103.setObjectName("toolButton_103")
        self.toolButton_103.setMinimumSize(QSize(50, 50))
        self.toolButton_103.setMaximumSize(QSize(50, 50))
        self.toolButton_103.setIcon(icon4)

        self.gridLayout_103.addWidget(self.toolButton_103, 0, 1, 1, 1)

        self.lineEdit_40 = QLineEdit(self.frame_94)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_40.setMinimumSize(QSize(0, 50))

        self.gridLayout_103.addWidget(self.lineEdit_40, 0, 0, 1, 1)

        self.toolButton_104 = QToolButton(self.frame_94)
        self.toolButton_104.setObjectName("toolButton_104")
        self.toolButton_104.setMinimumSize(QSize(50, 50))
        self.toolButton_104.setMaximumSize(QSize(50, 50))
        self.toolButton_104.setIcon(icon5)

        self.gridLayout_103.addWidget(self.toolButton_104, 0, 2, 1, 1)

        self.gridLayout_102.addWidget(self.frame_94, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_91, 6, 0, 1, 1)

        self.frame_71 = QFrame(self.scrollAreaWidgetContents)
        self.frame_71.setObjectName("frame_71")
        self.frame_71.setMinimumSize(QSize(0, 200))
        self.frame_71.setMaximumSize(QSize(16777215, 200))
        self.frame_71.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.gridLayout_78 = QGridLayout(self.frame_71)
        self.gridLayout_78.setObjectName("gridLayout_78")
        self.gridLayout_78.setContentsMargins(20, 20, 20, 20)
        self.label_71 = QLabel(self.frame_71)
        self.label_71.setObjectName("label_71")
        self.label_71.setMinimumSize(QSize(80, 30))
        self.label_71.setMaximumSize(QSize(80, 30))
        self.label_71.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_71.setTextFormat(Qt.AutoText)
        self.label_71.setScaledContents(True)
        self.label_71.setAlignment(Qt.AlignCenter)
        self.label_71.setWordWrap(False)
        self.label_71.setOpenExternalLinks(False)

        self.gridLayout_78.addWidget(self.label_71, 0, 0, 1, 1)

        self.label_72 = QLabel(self.frame_71)
        self.label_72.setObjectName("label_72")

        self.gridLayout_78.addWidget(self.label_72, 0, 1, 1, 1)

        self.frame_72 = QFrame(self.frame_71)
        self.frame_72.setObjectName("frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.gridLayout_79 = QGridLayout(self.frame_72)
        self.gridLayout_79.setObjectName("gridLayout_79")
        self.gridLayout_79.setHorizontalSpacing(5)
        self.gridLayout_79.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_28 = QLineEdit(self.frame_72)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_28.setMinimumSize(QSize(0, 50))

        self.gridLayout_79.addWidget(self.lineEdit_28, 0, 0, 1, 1)

        self.toolButton_80 = QToolButton(self.frame_72)
        self.toolButton_80.setObjectName("toolButton_80")
        self.toolButton_80.setMinimumSize(QSize(50, 50))
        self.toolButton_80.setMaximumSize(QSize(50, 50))
        self.toolButton_80.setIcon(icon5)

        self.gridLayout_79.addWidget(self.toolButton_80, 0, 2, 1, 1)

        self.toolButton_79 = QToolButton(self.frame_72)
        self.toolButton_79.setObjectName("toolButton_79")
        self.toolButton_79.setMinimumSize(QSize(50, 50))
        self.toolButton_79.setMaximumSize(QSize(50, 50))
        self.toolButton_79.setIcon(icon4)

        self.gridLayout_79.addWidget(self.toolButton_79, 0, 1, 1, 1)

        self.gridLayout_78.addWidget(self.frame_72, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_71, 17, 0, 1, 1)

        self.frame_103 = QFrame(self.scrollAreaWidgetContents)
        self.frame_103.setObjectName("frame_103")
        self.frame_103.setMinimumSize(QSize(0, 200))
        self.frame_103.setMaximumSize(QSize(16777215, 200))
        self.frame_103.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.gridLayout_112 = QGridLayout(self.frame_103)
        self.gridLayout_112.setObjectName("gridLayout_112")
        self.gridLayout_112.setContentsMargins(20, 20, 20, 20)
        self.label_105 = QLabel(self.frame_103)
        self.label_105.setObjectName("label_105")
        self.label_105.setMinimumSize(QSize(30, 30))
        self.label_105.setMaximumSize(QSize(30, 30))
        self.label_105.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_105.setTextFormat(Qt.AutoText)
        self.label_105.setScaledContents(True)
        self.label_105.setAlignment(Qt.AlignCenter)
        self.label_105.setWordWrap(False)
        self.label_105.setOpenExternalLinks(False)

        self.gridLayout_112.addWidget(self.label_105, 0, 0, 1, 1)

        self.label_106 = QLabel(self.frame_103)
        self.label_106.setObjectName("label_106")

        self.gridLayout_112.addWidget(self.label_106, 0, 1, 1, 1)

        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName("frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.gridLayout_113 = QGridLayout(self.frame_104)
        self.gridLayout_113.setObjectName("gridLayout_113")
        self.gridLayout_113.setHorizontalSpacing(5)
        self.gridLayout_113.setContentsMargins(0, 0, 0, 0)
        self.toolButton_113 = QToolButton(self.frame_104)
        self.toolButton_113.setObjectName("toolButton_113")
        self.toolButton_113.setMinimumSize(QSize(50, 50))
        self.toolButton_113.setMaximumSize(QSize(50, 50))
        self.toolButton_113.setIcon(icon4)

        self.gridLayout_113.addWidget(self.toolButton_113, 0, 1, 1, 1)

        self.lineEdit_45 = QLineEdit(self.frame_104)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_45.setMinimumSize(QSize(0, 50))

        self.gridLayout_113.addWidget(self.lineEdit_45, 0, 0, 1, 1)

        self.toolButton_114 = QToolButton(self.frame_104)
        self.toolButton_114.setObjectName("toolButton_114")
        self.toolButton_114.setMinimumSize(QSize(50, 50))
        self.toolButton_114.setMaximumSize(QSize(50, 50))
        self.toolButton_114.setIcon(icon5)

        self.gridLayout_113.addWidget(self.toolButton_114, 0, 2, 1, 1)

        self.gridLayout_112.addWidget(self.frame_104, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_103, 1, 0, 1, 1)

        self.frame_89 = QFrame(self.scrollAreaWidgetContents)
        self.frame_89.setObjectName("frame_89")
        self.frame_89.setMinimumSize(QSize(0, 200))
        self.frame_89.setMaximumSize(QSize(16777215, 200))
        self.frame_89.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.gridLayout_96 = QGridLayout(self.frame_89)
        self.gridLayout_96.setObjectName("gridLayout_96")
        self.gridLayout_96.setContentsMargins(20, 20, 20, 20)
        self.label_89 = QLabel(self.frame_89)
        self.label_89.setObjectName("label_89")
        self.label_89.setMinimumSize(QSize(30, 30))
        self.label_89.setMaximumSize(QSize(30, 30))
        self.label_89.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_89.setTextFormat(Qt.AutoText)
        self.label_89.setScaledContents(True)
        self.label_89.setAlignment(Qt.AlignCenter)
        self.label_89.setWordWrap(False)
        self.label_89.setOpenExternalLinks(False)

        self.gridLayout_96.addWidget(self.label_89, 0, 0, 1, 1)

        self.label_90 = QLabel(self.frame_89)
        self.label_90.setObjectName("label_90")

        self.gridLayout_96.addWidget(self.label_90, 0, 1, 1, 1)

        self.frame_90 = QFrame(self.frame_89)
        self.frame_90.setObjectName("frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.gridLayout_97 = QGridLayout(self.frame_90)
        self.gridLayout_97.setObjectName("gridLayout_97")
        self.gridLayout_97.setHorizontalSpacing(5)
        self.gridLayout_97.setContentsMargins(0, 0, 0, 0)
        self.toolButton_97 = QToolButton(self.frame_90)
        self.toolButton_97.setObjectName("toolButton_97")
        self.toolButton_97.setMinimumSize(QSize(50, 50))
        self.toolButton_97.setMaximumSize(QSize(50, 50))
        self.toolButton_97.setIcon(icon4)

        self.gridLayout_97.addWidget(self.toolButton_97, 0, 1, 1, 1)

        self.lineEdit_37 = QLineEdit(self.frame_90)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_37.setMinimumSize(QSize(0, 50))

        self.gridLayout_97.addWidget(self.lineEdit_37, 0, 0, 1, 1)

        self.toolButton_98 = QToolButton(self.frame_90)
        self.toolButton_98.setObjectName("toolButton_98")
        self.toolButton_98.setMinimumSize(QSize(50, 50))
        self.toolButton_98.setMaximumSize(QSize(50, 50))
        self.toolButton_98.setIcon(icon5)

        self.gridLayout_97.addWidget(self.toolButton_98, 0, 2, 1, 1)

        self.gridLayout_96.addWidget(self.frame_90, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_89, 7, 0, 1, 1)

        self.frame_79 = QFrame(self.scrollAreaWidgetContents)
        self.frame_79.setObjectName("frame_79")
        self.frame_79.setMinimumSize(QSize(0, 200))
        self.frame_79.setMaximumSize(QSize(16777215, 200))
        self.frame_79.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.gridLayout_86 = QGridLayout(self.frame_79)
        self.gridLayout_86.setObjectName("gridLayout_86")
        self.gridLayout_86.setContentsMargins(20, 20, 20, 20)
        self.label_79 = QLabel(self.frame_79)
        self.label_79.setObjectName("label_79")
        self.label_79.setMinimumSize(QSize(70, 30))
        self.label_79.setMaximumSize(QSize(70, 30))
        self.label_79.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_79.setTextFormat(Qt.AutoText)
        self.label_79.setScaledContents(True)
        self.label_79.setAlignment(Qt.AlignCenter)
        self.label_79.setWordWrap(False)
        self.label_79.setOpenExternalLinks(False)

        self.gridLayout_86.addWidget(self.label_79, 0, 0, 1, 1)

        self.label_80 = QLabel(self.frame_79)
        self.label_80.setObjectName("label_80")

        self.gridLayout_86.addWidget(self.label_80, 0, 1, 1, 1)

        self.frame_80 = QFrame(self.frame_79)
        self.frame_80.setObjectName("frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.gridLayout_87 = QGridLayout(self.frame_80)
        self.gridLayout_87.setObjectName("gridLayout_87")
        self.gridLayout_87.setHorizontalSpacing(5)
        self.gridLayout_87.setContentsMargins(0, 0, 0, 0)
        self.toolButton_87 = QToolButton(self.frame_80)
        self.toolButton_87.setObjectName("toolButton_87")
        self.toolButton_87.setMinimumSize(QSize(50, 50))
        self.toolButton_87.setMaximumSize(QSize(50, 50))
        self.toolButton_87.setIcon(icon4)

        self.gridLayout_87.addWidget(self.toolButton_87, 0, 1, 1, 1)

        self.lineEdit_32 = QLineEdit(self.frame_80)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_32.setMinimumSize(QSize(0, 50))

        self.gridLayout_87.addWidget(self.lineEdit_32, 0, 0, 1, 1)

        self.toolButton_88 = QToolButton(self.frame_80)
        self.toolButton_88.setObjectName("toolButton_88")
        self.toolButton_88.setMinimumSize(QSize(50, 50))
        self.toolButton_88.setMaximumSize(QSize(50, 50))
        self.toolButton_88.setIcon(icon5)

        self.gridLayout_87.addWidget(self.toolButton_88, 0, 2, 1, 1)

        self.gridLayout_86.addWidget(self.frame_80, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_79, 12, 0, 1, 1)

        self.frame_30 = QFrame(self.scrollAreaWidgetContents)
        self.frame_30.setObjectName("frame_30")
        self.frame_30.setMinimumSize(QSize(0, 200))
        self.frame_30.setMaximumSize(QSize(16777215, 200))
        self.frame_30.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_30)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.gridLayout_34.setContentsMargins(20, 20, 20, 20)
        self.label_28 = QLabel(self.frame_30)
        self.label_28.setObjectName("label_28")

        self.gridLayout_34.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_27 = QLabel(self.frame_30)
        self.label_27.setObjectName("label_27")
        self.label_27.setMinimumSize(QSize(30, 30))
        self.label_27.setMaximumSize(QSize(30, 30))
        self.label_27.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_27.setTextFormat(Qt.AutoText)
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setWordWrap(False)
        self.label_27.setOpenExternalLinks(False)

        self.gridLayout_34.addWidget(self.label_27, 0, 0, 1, 1)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName("frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_31)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.gridLayout_35.setHorizontalSpacing(5)
        self.gridLayout_35.setVerticalSpacing(0)
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.frame_31)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 50))

        self.gridLayout_35.addWidget(self.lineEdit_6, 0, 0, 1, 1)

        self.toolButton_36 = QToolButton(self.frame_31)
        self.toolButton_36.setObjectName("toolButton_36")
        self.toolButton_36.setMinimumSize(QSize(50, 50))
        self.toolButton_36.setMaximumSize(QSize(50, 50))
        self.toolButton_36.setIcon(icon5)

        self.gridLayout_35.addWidget(self.toolButton_36, 0, 2, 1, 1)

        self.toolButton_35 = QToolButton(self.frame_31)
        self.toolButton_35.setObjectName("toolButton_35")
        self.toolButton_35.setMinimumSize(QSize(50, 50))
        self.toolButton_35.setMaximumSize(QSize(50, 50))
        self.toolButton_35.setIcon(icon4)

        self.gridLayout_35.addWidget(self.toolButton_35, 0, 1, 1, 1)

        self.gridLayout_34.addWidget(self.frame_31, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_30, 0, 0, 1, 1)

        self.frame_81 = QFrame(self.scrollAreaWidgetContents)
        self.frame_81.setObjectName("frame_81")
        self.frame_81.setMinimumSize(QSize(0, 200))
        self.frame_81.setMaximumSize(QSize(16777215, 200))
        self.frame_81.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.gridLayout_88 = QGridLayout(self.frame_81)
        self.gridLayout_88.setObjectName("gridLayout_88")
        self.gridLayout_88.setContentsMargins(20, 20, 20, 20)
        self.label_81 = QLabel(self.frame_81)
        self.label_81.setObjectName("label_81")
        self.label_81.setMinimumSize(QSize(50, 30))
        self.label_81.setMaximumSize(QSize(50, 30))
        self.label_81.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_81.setTextFormat(Qt.AutoText)
        self.label_81.setScaledContents(True)
        self.label_81.setAlignment(Qt.AlignCenter)
        self.label_81.setWordWrap(False)
        self.label_81.setOpenExternalLinks(False)

        self.gridLayout_88.addWidget(self.label_81, 0, 0, 1, 1)

        self.label_82 = QLabel(self.frame_81)
        self.label_82.setObjectName("label_82")

        self.gridLayout_88.addWidget(self.label_82, 0, 1, 1, 1)

        self.frame_82 = QFrame(self.frame_81)
        self.frame_82.setObjectName("frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.gridLayout_89 = QGridLayout(self.frame_82)
        self.gridLayout_89.setObjectName("gridLayout_89")
        self.gridLayout_89.setHorizontalSpacing(5)
        self.gridLayout_89.setContentsMargins(0, 0, 0, 0)
        self.toolButton_89 = QToolButton(self.frame_82)
        self.toolButton_89.setObjectName("toolButton_89")
        self.toolButton_89.setMinimumSize(QSize(50, 50))
        self.toolButton_89.setMaximumSize(QSize(50, 50))
        self.toolButton_89.setIcon(icon4)

        self.gridLayout_89.addWidget(self.toolButton_89, 0, 1, 1, 1)

        self.lineEdit_33 = QLineEdit(self.frame_82)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_33.setMinimumSize(QSize(0, 50))

        self.gridLayout_89.addWidget(self.lineEdit_33, 0, 0, 1, 1)

        self.toolButton_90 = QToolButton(self.frame_82)
        self.toolButton_90.setObjectName("toolButton_90")
        self.toolButton_90.setMinimumSize(QSize(50, 50))
        self.toolButton_90.setMaximumSize(QSize(50, 50))
        self.toolButton_90.setIcon(icon5)

        self.gridLayout_89.addWidget(self.toolButton_90, 0, 2, 1, 1)

        self.gridLayout_88.addWidget(self.frame_82, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_81, 11, 0, 1, 1)

        self.frame_101 = QFrame(self.scrollAreaWidgetContents)
        self.frame_101.setObjectName("frame_101")
        self.frame_101.setMinimumSize(QSize(0, 200))
        self.frame_101.setMaximumSize(QSize(16777215, 200))
        self.frame_101.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.gridLayout_110 = QGridLayout(self.frame_101)
        self.gridLayout_110.setObjectName("gridLayout_110")
        self.gridLayout_110.setContentsMargins(20, 20, 20, 20)
        self.label_103 = QLabel(self.frame_101)
        self.label_103.setObjectName("label_103")
        self.label_103.setMinimumSize(QSize(50, 30))
        self.label_103.setMaximumSize(QSize(50, 30))
        self.label_103.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_103.setTextFormat(Qt.AutoText)
        self.label_103.setScaledContents(True)
        self.label_103.setAlignment(Qt.AlignCenter)
        self.label_103.setWordWrap(False)
        self.label_103.setOpenExternalLinks(False)

        self.gridLayout_110.addWidget(self.label_103, 0, 0, 1, 1)

        self.label_104 = QLabel(self.frame_101)
        self.label_104.setObjectName("label_104")

        self.gridLayout_110.addWidget(self.label_104, 0, 1, 1, 1)

        self.frame_102 = QFrame(self.frame_101)
        self.frame_102.setObjectName("frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.gridLayout_111 = QGridLayout(self.frame_102)
        self.gridLayout_111.setObjectName("gridLayout_111")
        self.gridLayout_111.setHorizontalSpacing(5)
        self.gridLayout_111.setContentsMargins(0, 0, 0, 0)
        self.toolButton_111 = QToolButton(self.frame_102)
        self.toolButton_111.setObjectName("toolButton_111")
        self.toolButton_111.setMinimumSize(QSize(50, 50))
        self.toolButton_111.setMaximumSize(QSize(50, 50))
        self.toolButton_111.setIcon(icon4)

        self.gridLayout_111.addWidget(self.toolButton_111, 0, 1, 1, 1)

        self.lineEdit_44 = QLineEdit(self.frame_102)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_44.setMinimumSize(QSize(0, 50))

        self.gridLayout_111.addWidget(self.lineEdit_44, 0, 0, 1, 1)

        self.toolButton_112 = QToolButton(self.frame_102)
        self.toolButton_112.setObjectName("toolButton_112")
        self.toolButton_112.setMinimumSize(QSize(50, 50))
        self.toolButton_112.setMaximumSize(QSize(50, 50))
        self.toolButton_112.setIcon(icon5)

        self.gridLayout_111.addWidget(self.toolButton_112, 0, 2, 1, 1)

        self.gridLayout_110.addWidget(self.frame_102, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_101, 2, 0, 1, 1)

        self.frame_85 = QFrame(self.scrollAreaWidgetContents)
        self.frame_85.setObjectName("frame_85")
        self.frame_85.setMinimumSize(QSize(0, 200))
        self.frame_85.setMaximumSize(QSize(16777215, 200))
        self.frame_85.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.gridLayout_92 = QGridLayout(self.frame_85)
        self.gridLayout_92.setObjectName("gridLayout_92")
        self.gridLayout_92.setContentsMargins(20, 20, 20, 20)
        self.label_85 = QLabel(self.frame_85)
        self.label_85.setObjectName("label_85")
        self.label_85.setMinimumSize(QSize(50, 30))
        self.label_85.setMaximumSize(QSize(50, 30))
        self.label_85.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_85.setTextFormat(Qt.AutoText)
        self.label_85.setScaledContents(True)
        self.label_85.setAlignment(Qt.AlignCenter)
        self.label_85.setWordWrap(False)
        self.label_85.setOpenExternalLinks(False)

        self.gridLayout_92.addWidget(self.label_85, 0, 0, 1, 1)

        self.label_86 = QLabel(self.frame_85)
        self.label_86.setObjectName("label_86")

        self.gridLayout_92.addWidget(self.label_86, 0, 1, 1, 1)

        self.frame_86 = QFrame(self.frame_85)
        self.frame_86.setObjectName("frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.gridLayout_93 = QGridLayout(self.frame_86)
        self.gridLayout_93.setObjectName("gridLayout_93")
        self.gridLayout_93.setHorizontalSpacing(5)
        self.gridLayout_93.setContentsMargins(0, 0, 0, 0)
        self.toolButton_93 = QToolButton(self.frame_86)
        self.toolButton_93.setObjectName("toolButton_93")
        self.toolButton_93.setMinimumSize(QSize(50, 50))
        self.toolButton_93.setMaximumSize(QSize(50, 50))
        self.toolButton_93.setIcon(icon4)

        self.gridLayout_93.addWidget(self.toolButton_93, 0, 1, 1, 1)

        self.lineEdit_35 = QLineEdit(self.frame_86)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_35.setMinimumSize(QSize(0, 50))

        self.gridLayout_93.addWidget(self.lineEdit_35, 0, 0, 1, 1)

        self.toolButton_94 = QToolButton(self.frame_86)
        self.toolButton_94.setObjectName("toolButton_94")
        self.toolButton_94.setMinimumSize(QSize(50, 50))
        self.toolButton_94.setMaximumSize(QSize(50, 50))
        self.toolButton_94.setIcon(icon5)

        self.gridLayout_93.addWidget(self.toolButton_94, 0, 2, 1, 1)

        self.gridLayout_92.addWidget(self.frame_86, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_85, 9, 0, 1, 1)

        self.frame_75 = QFrame(self.scrollAreaWidgetContents)
        self.frame_75.setObjectName("frame_75")
        self.frame_75.setMinimumSize(QSize(0, 200))
        self.frame_75.setMaximumSize(QSize(16777215, 200))
        self.frame_75.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.gridLayout_82 = QGridLayout(self.frame_75)
        self.gridLayout_82.setObjectName("gridLayout_82")
        self.gridLayout_82.setContentsMargins(20, 20, 20, 20)
        self.label_75 = QLabel(self.frame_75)
        self.label_75.setObjectName("label_75")
        self.label_75.setMinimumSize(QSize(80, 30))
        self.label_75.setMaximumSize(QSize(80, 30))
        self.label_75.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_75.setTextFormat(Qt.AutoText)
        self.label_75.setScaledContents(True)
        self.label_75.setAlignment(Qt.AlignCenter)
        self.label_75.setWordWrap(False)
        self.label_75.setOpenExternalLinks(False)

        self.gridLayout_82.addWidget(self.label_75, 0, 0, 1, 1)

        self.label_76 = QLabel(self.frame_75)
        self.label_76.setObjectName("label_76")

        self.gridLayout_82.addWidget(self.label_76, 0, 1, 1, 1)

        self.frame_76 = QFrame(self.frame_75)
        self.frame_76.setObjectName("frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.gridLayout_83 = QGridLayout(self.frame_76)
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.gridLayout_83.setHorizontalSpacing(5)
        self.gridLayout_83.setContentsMargins(0, 0, 0, 0)
        self.toolButton_83 = QToolButton(self.frame_76)
        self.toolButton_83.setObjectName("toolButton_83")
        self.toolButton_83.setMinimumSize(QSize(50, 50))
        self.toolButton_83.setMaximumSize(QSize(50, 50))
        self.toolButton_83.setIcon(icon4)

        self.gridLayout_83.addWidget(self.toolButton_83, 0, 1, 1, 1)

        self.lineEdit_30 = QLineEdit(self.frame_76)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_30.setMinimumSize(QSize(0, 50))

        self.gridLayout_83.addWidget(self.lineEdit_30, 0, 0, 1, 1)

        self.toolButton_84 = QToolButton(self.frame_76)
        self.toolButton_84.setObjectName("toolButton_84")
        self.toolButton_84.setMinimumSize(QSize(50, 50))
        self.toolButton_84.setMaximumSize(QSize(50, 50))
        self.toolButton_84.setIcon(icon5)

        self.gridLayout_83.addWidget(self.toolButton_84, 0, 2, 1, 1)

        self.gridLayout_82.addWidget(self.frame_76, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_75, 14, 0, 1, 1)

        self.frame_77 = QFrame(self.scrollAreaWidgetContents)
        self.frame_77.setObjectName("frame_77")
        self.frame_77.setMinimumSize(QSize(0, 200))
        self.frame_77.setMaximumSize(QSize(16777215, 200))
        self.frame_77.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.gridLayout_84 = QGridLayout(self.frame_77)
        self.gridLayout_84.setObjectName("gridLayout_84")
        self.gridLayout_84.setContentsMargins(20, 20, 20, 20)
        self.label_77 = QLabel(self.frame_77)
        self.label_77.setObjectName("label_77")
        self.label_77.setMinimumSize(QSize(80, 30))
        self.label_77.setMaximumSize(QSize(80, 30))
        self.label_77.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_77.setTextFormat(Qt.AutoText)
        self.label_77.setScaledContents(True)
        self.label_77.setAlignment(Qt.AlignCenter)
        self.label_77.setWordWrap(False)
        self.label_77.setOpenExternalLinks(False)

        self.gridLayout_84.addWidget(self.label_77, 0, 0, 1, 1)

        self.label_78 = QLabel(self.frame_77)
        self.label_78.setObjectName("label_78")

        self.gridLayout_84.addWidget(self.label_78, 0, 1, 1, 1)

        self.frame_78 = QFrame(self.frame_77)
        self.frame_78.setObjectName("frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.gridLayout_85 = QGridLayout(self.frame_78)
        self.gridLayout_85.setObjectName("gridLayout_85")
        self.gridLayout_85.setHorizontalSpacing(5)
        self.gridLayout_85.setContentsMargins(0, 0, 0, 0)
        self.toolButton_85 = QToolButton(self.frame_78)
        self.toolButton_85.setObjectName("toolButton_85")
        self.toolButton_85.setMinimumSize(QSize(50, 50))
        self.toolButton_85.setMaximumSize(QSize(50, 50))
        self.toolButton_85.setIcon(icon4)

        self.gridLayout_85.addWidget(self.toolButton_85, 0, 1, 1, 1)

        self.lineEdit_31 = QLineEdit(self.frame_78)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_31.setMinimumSize(QSize(0, 50))

        self.gridLayout_85.addWidget(self.lineEdit_31, 0, 0, 1, 1)

        self.toolButton_86 = QToolButton(self.frame_78)
        self.toolButton_86.setObjectName("toolButton_86")
        self.toolButton_86.setMinimumSize(QSize(50, 50))
        self.toolButton_86.setMaximumSize(QSize(50, 50))
        self.toolButton_86.setIcon(icon5)

        self.gridLayout_85.addWidget(self.toolButton_86, 0, 2, 1, 1)

        self.gridLayout_84.addWidget(self.frame_78, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_77, 13, 0, 1, 1)

        self.frame_87 = QFrame(self.scrollAreaWidgetContents)
        self.frame_87.setObjectName("frame_87")
        self.frame_87.setMinimumSize(QSize(0, 200))
        self.frame_87.setMaximumSize(QSize(16777215, 200))
        self.frame_87.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.gridLayout_94 = QGridLayout(self.frame_87)
        self.gridLayout_94.setObjectName("gridLayout_94")
        self.gridLayout_94.setContentsMargins(20, 20, 20, 20)
        self.label_87 = QLabel(self.frame_87)
        self.label_87.setObjectName("label_87")
        self.label_87.setMinimumSize(QSize(30, 30))
        self.label_87.setMaximumSize(QSize(30, 30))
        self.label_87.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_87.setTextFormat(Qt.AutoText)
        self.label_87.setScaledContents(True)
        self.label_87.setAlignment(Qt.AlignCenter)
        self.label_87.setWordWrap(False)
        self.label_87.setOpenExternalLinks(False)

        self.gridLayout_94.addWidget(self.label_87, 0, 0, 1, 1)

        self.label_88 = QLabel(self.frame_87)
        self.label_88.setObjectName("label_88")

        self.gridLayout_94.addWidget(self.label_88, 0, 1, 1, 1)

        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName("frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.gridLayout_95 = QGridLayout(self.frame_88)
        self.gridLayout_95.setObjectName("gridLayout_95")
        self.gridLayout_95.setHorizontalSpacing(5)
        self.gridLayout_95.setContentsMargins(0, 0, 0, 0)
        self.toolButton_95 = QToolButton(self.frame_88)
        self.toolButton_95.setObjectName("toolButton_95")
        self.toolButton_95.setMinimumSize(QSize(50, 50))
        self.toolButton_95.setMaximumSize(QSize(50, 50))
        self.toolButton_95.setIcon(icon4)

        self.gridLayout_95.addWidget(self.toolButton_95, 0, 1, 1, 1)

        self.lineEdit_36 = QLineEdit(self.frame_88)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_36.setMinimumSize(QSize(0, 50))

        self.gridLayout_95.addWidget(self.lineEdit_36, 0, 0, 1, 1)

        self.toolButton_96 = QToolButton(self.frame_88)
        self.toolButton_96.setObjectName("toolButton_96")
        self.toolButton_96.setMinimumSize(QSize(50, 50))
        self.toolButton_96.setMaximumSize(QSize(50, 50))
        self.toolButton_96.setIcon(icon5)

        self.gridLayout_95.addWidget(self.toolButton_96, 0, 2, 1, 1)

        self.gridLayout_94.addWidget(self.frame_88, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_87, 8, 0, 1, 1)

        self.frame_105 = QFrame(self.scrollAreaWidgetContents)
        self.frame_105.setObjectName("frame_105")
        self.frame_105.setMinimumSize(QSize(0, 200))
        self.frame_105.setMaximumSize(QSize(16777215, 200))
        self.frame_105.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.gridLayout_114 = QGridLayout(self.frame_105)
        self.gridLayout_114.setObjectName("gridLayout_114")
        self.gridLayout_114.setContentsMargins(20, 20, 20, 20)
        self.label_107 = QLabel(self.frame_105)
        self.label_107.setObjectName("label_107")
        self.label_107.setMinimumSize(QSize(80, 30))
        self.label_107.setMaximumSize(QSize(80, 30))
        self.label_107.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_107.setTextFormat(Qt.AutoText)
        self.label_107.setScaledContents(True)
        self.label_107.setAlignment(Qt.AlignCenter)
        self.label_107.setWordWrap(False)
        self.label_107.setOpenExternalLinks(False)

        self.gridLayout_114.addWidget(self.label_107, 0, 0, 1, 1)

        self.label_108 = QLabel(self.frame_105)
        self.label_108.setObjectName("label_108")

        self.gridLayout_114.addWidget(self.label_108, 0, 1, 1, 1)

        self.frame_106 = QFrame(self.frame_105)
        self.frame_106.setObjectName("frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.gridLayout_115 = QGridLayout(self.frame_106)
        self.gridLayout_115.setObjectName("gridLayout_115")
        self.gridLayout_115.setHorizontalSpacing(5)
        self.gridLayout_115.setContentsMargins(0, 0, 0, 0)
        self.toolButton_117 = QToolButton(self.frame_106)
        self.toolButton_117.setObjectName("toolButton_117")
        self.toolButton_117.setMinimumSize(QSize(50, 50))
        self.toolButton_117.setMaximumSize(QSize(50, 50))
        self.toolButton_117.setIcon(icon4)

        self.gridLayout_115.addWidget(self.toolButton_117, 0, 1, 1, 1)

        self.lineEdit_47 = QLineEdit(self.frame_106)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_47.setMinimumSize(QSize(0, 50))

        self.gridLayout_115.addWidget(self.lineEdit_47, 0, 0, 1, 1)

        self.toolButton_118 = QToolButton(self.frame_106)
        self.toolButton_118.setObjectName("toolButton_118")
        self.toolButton_118.setMinimumSize(QSize(50, 50))
        self.toolButton_118.setMaximumSize(QSize(50, 50))
        self.toolButton_118.setIcon(icon5)

        self.gridLayout_115.addWidget(self.toolButton_118, 0, 2, 1, 1)

        self.gridLayout_114.addWidget(self.frame_106, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_105, 18, 0, 1, 1)

        self.frame_83 = QFrame(self.scrollAreaWidgetContents)
        self.frame_83.setObjectName("frame_83")
        self.frame_83.setMinimumSize(QSize(0, 200))
        self.frame_83.setMaximumSize(QSize(16777215, 200))
        self.frame_83.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.gridLayout_90 = QGridLayout(self.frame_83)
        self.gridLayout_90.setObjectName("gridLayout_90")
        self.gridLayout_90.setContentsMargins(20, 20, 20, 20)
        self.label_83 = QLabel(self.frame_83)
        self.label_83.setObjectName("label_83")
        self.label_83.setMinimumSize(QSize(60, 30))
        self.label_83.setMaximumSize(QSize(60, 30))
        self.label_83.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_83.setTextFormat(Qt.AutoText)
        self.label_83.setScaledContents(True)
        self.label_83.setAlignment(Qt.AlignCenter)
        self.label_83.setWordWrap(False)
        self.label_83.setOpenExternalLinks(False)

        self.gridLayout_90.addWidget(self.label_83, 0, 0, 1, 1)

        self.label_84 = QLabel(self.frame_83)
        self.label_84.setObjectName("label_84")

        self.gridLayout_90.addWidget(self.label_84, 0, 1, 1, 1)

        self.frame_84 = QFrame(self.frame_83)
        self.frame_84.setObjectName("frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.gridLayout_91 = QGridLayout(self.frame_84)
        self.gridLayout_91.setObjectName("gridLayout_91")
        self.gridLayout_91.setHorizontalSpacing(5)
        self.gridLayout_91.setContentsMargins(0, 0, 0, 0)
        self.toolButton_91 = QToolButton(self.frame_84)
        self.toolButton_91.setObjectName("toolButton_91")
        self.toolButton_91.setMinimumSize(QSize(50, 50))
        self.toolButton_91.setMaximumSize(QSize(50, 50))
        self.toolButton_91.setIcon(icon4)

        self.gridLayout_91.addWidget(self.toolButton_91, 0, 1, 1, 1)

        self.lineEdit_34 = QLineEdit(self.frame_84)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_34.setMinimumSize(QSize(0, 50))

        self.gridLayout_91.addWidget(self.lineEdit_34, 0, 0, 1, 1)

        self.toolButton_92 = QToolButton(self.frame_84)
        self.toolButton_92.setObjectName("toolButton_92")
        self.toolButton_92.setMinimumSize(QSize(50, 50))
        self.toolButton_92.setMaximumSize(QSize(50, 50))
        self.toolButton_92.setIcon(icon5)

        self.gridLayout_91.addWidget(self.toolButton_92, 0, 2, 1, 1)

        self.gridLayout_90.addWidget(self.frame_84, 1, 0, 1, 2)

        self.gridLayout_6.addWidget(self.frame_83, 10, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_7.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_9 = QGridLayout(self.tab_6)
        self.gridLayout_9.setSpacing(10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.tab_6)
        self.frame_23.setObjectName("frame_23")
        self.frame_23.setMinimumSize(QSize(0, 60))
        self.frame_23.setMaximumSize(QSize(16777215, 60))
        self.frame_23.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_23)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.label_12 = QLabel(self.frame_23)
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')

        self.gridLayout_31.addWidget(self.label_12, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_31.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_31.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.gridLayout_9.addWidget(self.frame_23, 0, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.tab_6)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setStyleSheet(
            "	border-style: solid;\n"
            "	border-top-color: transparent;\n"
            "	border-right-color: transparent;\n"
            "	border-left-color: transparent;\n"
            "	border-bottom-color: transparent;\n"
            "	border-width: 0px;"
        )
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 958, 4230))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_8.setContentsMargins(20, 20, 20, 20)
        self.frame_129 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_129.setObjectName("frame_129")
        self.frame_129.setMinimumSize(QSize(0, 200))
        self.frame_129.setMaximumSize(QSize(16777215, 200))
        self.frame_129.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.gridLayout_138 = QGridLayout(self.frame_129)
        self.gridLayout_138.setObjectName("gridLayout_138")
        self.gridLayout_138.setContentsMargins(20, 20, 20, 20)
        self.label_131 = QLabel(self.frame_129)
        self.label_131.setObjectName("label_131")
        self.label_131.setMinimumSize(QSize(30, 30))
        self.label_131.setMaximumSize(QSize(30, 30))
        self.label_131.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_131.setTextFormat(Qt.AutoText)
        self.label_131.setScaledContents(True)
        self.label_131.setAlignment(Qt.AlignCenter)
        self.label_131.setWordWrap(False)
        self.label_131.setOpenExternalLinks(False)

        self.gridLayout_138.addWidget(self.label_131, 0, 0, 1, 1)

        self.label_132 = QLabel(self.frame_129)
        self.label_132.setObjectName("label_132")

        self.gridLayout_138.addWidget(self.label_132, 0, 1, 1, 1)

        self.frame_130 = QFrame(self.frame_129)
        self.frame_130.setObjectName("frame_130")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.gridLayout_139 = QGridLayout(self.frame_130)
        self.gridLayout_139.setObjectName("gridLayout_139")
        self.gridLayout_139.setHorizontalSpacing(5)
        self.gridLayout_139.setContentsMargins(0, 0, 0, 0)
        self.toolButton_147 = QToolButton(self.frame_130)
        self.toolButton_147.setObjectName("toolButton_147")
        self.toolButton_147.setMinimumSize(QSize(50, 50))
        self.toolButton_147.setMaximumSize(QSize(50, 50))
        self.toolButton_147.setIcon(icon4)

        self.gridLayout_139.addWidget(self.toolButton_147, 0, 1, 1, 1)

        self.lineEdit_62 = QLineEdit(self.frame_130)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.lineEdit_62.setMinimumSize(QSize(0, 50))

        self.gridLayout_139.addWidget(self.lineEdit_62, 0, 0, 1, 1)

        self.toolButton_148 = QToolButton(self.frame_130)
        self.toolButton_148.setObjectName("toolButton_148")
        self.toolButton_148.setMinimumSize(QSize(50, 50))
        self.toolButton_148.setMaximumSize(QSize(50, 50))
        self.toolButton_148.setIcon(icon5)

        self.gridLayout_139.addWidget(self.toolButton_148, 0, 2, 1, 1)

        self.gridLayout_138.addWidget(self.frame_130, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_129, 1, 0, 1, 1)

        self.frame_137 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_137.setObjectName("frame_137")
        self.frame_137.setMinimumSize(QSize(0, 200))
        self.frame_137.setMaximumSize(QSize(16777215, 200))
        self.frame_137.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.gridLayout_146 = QGridLayout(self.frame_137)
        self.gridLayout_146.setObjectName("gridLayout_146")
        self.gridLayout_146.setContentsMargins(20, 20, 20, 20)
        self.label_139 = QLabel(self.frame_137)
        self.label_139.setObjectName("label_139")
        self.label_139.setMinimumSize(QSize(50, 30))
        self.label_139.setMaximumSize(QSize(50, 30))
        self.label_139.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_139.setTextFormat(Qt.AutoText)
        self.label_139.setScaledContents(True)
        self.label_139.setAlignment(Qt.AlignCenter)
        self.label_139.setWordWrap(False)
        self.label_139.setOpenExternalLinks(False)

        self.gridLayout_146.addWidget(self.label_139, 0, 0, 1, 1)

        self.label_140 = QLabel(self.frame_137)
        self.label_140.setObjectName("label_140")

        self.gridLayout_146.addWidget(self.label_140, 0, 1, 1, 1)

        self.frame_138 = QFrame(self.frame_137)
        self.frame_138.setObjectName("frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.gridLayout_147 = QGridLayout(self.frame_138)
        self.gridLayout_147.setObjectName("gridLayout_147")
        self.gridLayout_147.setHorizontalSpacing(5)
        self.gridLayout_147.setContentsMargins(0, 0, 0, 0)
        self.toolButton_155 = QToolButton(self.frame_138)
        self.toolButton_155.setObjectName("toolButton_155")
        self.toolButton_155.setMinimumSize(QSize(50, 50))
        self.toolButton_155.setMaximumSize(QSize(50, 50))
        self.toolButton_155.setIcon(icon4)

        self.gridLayout_147.addWidget(self.toolButton_155, 0, 1, 1, 1)

        self.lineEdit_66 = QLineEdit(self.frame_138)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.lineEdit_66.setMinimumSize(QSize(0, 50))

        self.gridLayout_147.addWidget(self.lineEdit_66, 0, 0, 1, 1)

        self.toolButton_156 = QToolButton(self.frame_138)
        self.toolButton_156.setObjectName("toolButton_156")
        self.toolButton_156.setMinimumSize(QSize(50, 50))
        self.toolButton_156.setMaximumSize(QSize(50, 50))
        self.toolButton_156.setIcon(icon5)

        self.gridLayout_147.addWidget(self.toolButton_156, 0, 2, 1, 1)

        self.gridLayout_146.addWidget(self.frame_138, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_137, 2, 0, 1, 1)

        self.frame_133 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_133.setObjectName("frame_133")
        self.frame_133.setMinimumSize(QSize(0, 200))
        self.frame_133.setMaximumSize(QSize(16777215, 200))
        self.frame_133.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.gridLayout_142 = QGridLayout(self.frame_133)
        self.gridLayout_142.setObjectName("gridLayout_142")
        self.gridLayout_142.setContentsMargins(20, 20, 20, 20)
        self.label_135 = QLabel(self.frame_133)
        self.label_135.setObjectName("label_135")
        self.label_135.setMinimumSize(QSize(110, 30))
        self.label_135.setMaximumSize(QSize(110, 30))
        self.label_135.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_135.setTextFormat(Qt.AutoText)
        self.label_135.setScaledContents(True)
        self.label_135.setAlignment(Qt.AlignCenter)
        self.label_135.setWordWrap(False)
        self.label_135.setOpenExternalLinks(False)

        self.gridLayout_142.addWidget(self.label_135, 0, 0, 1, 1)

        self.label_136 = QLabel(self.frame_133)
        self.label_136.setObjectName("label_136")

        self.gridLayout_142.addWidget(self.label_136, 0, 1, 1, 1)

        self.frame_134 = QFrame(self.frame_133)
        self.frame_134.setObjectName("frame_134")
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.gridLayout_143 = QGridLayout(self.frame_134)
        self.gridLayout_143.setObjectName("gridLayout_143")
        self.gridLayout_143.setHorizontalSpacing(5)
        self.gridLayout_143.setContentsMargins(0, 0, 0, 0)
        self.toolButton_151 = QToolButton(self.frame_134)
        self.toolButton_151.setObjectName("toolButton_151")
        self.toolButton_151.setMinimumSize(QSize(50, 50))
        self.toolButton_151.setMaximumSize(QSize(50, 50))
        self.toolButton_151.setIcon(icon4)

        self.gridLayout_143.addWidget(self.toolButton_151, 0, 1, 1, 1)

        self.lineEdit_64 = QLineEdit(self.frame_134)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.lineEdit_64.setMinimumSize(QSize(0, 50))

        self.gridLayout_143.addWidget(self.lineEdit_64, 0, 0, 1, 1)

        self.toolButton_152 = QToolButton(self.frame_134)
        self.toolButton_152.setObjectName("toolButton_152")
        self.toolButton_152.setMinimumSize(QSize(50, 50))
        self.toolButton_152.setMaximumSize(QSize(50, 50))
        self.toolButton_152.setIcon(icon5)

        self.gridLayout_143.addWidget(self.toolButton_152, 0, 2, 1, 1)

        self.gridLayout_142.addWidget(self.frame_134, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_133, 12, 0, 1, 1)

        self.frame_107 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_107.setObjectName("frame_107")
        self.frame_107.setMinimumSize(QSize(0, 200))
        self.frame_107.setMaximumSize(QSize(16777215, 200))
        self.frame_107.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.gridLayout_116 = QGridLayout(self.frame_107)
        self.gridLayout_116.setObjectName("gridLayout_116")
        self.gridLayout_116.setContentsMargins(20, 20, 20, 20)
        self.label_109 = QLabel(self.frame_107)
        self.label_109.setObjectName("label_109")
        self.label_109.setMinimumSize(QSize(80, 30))
        self.label_109.setMaximumSize(QSize(80, 30))
        self.label_109.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_109.setTextFormat(Qt.AutoText)
        self.label_109.setScaledContents(True)
        self.label_109.setAlignment(Qt.AlignCenter)
        self.label_109.setWordWrap(False)
        self.label_109.setOpenExternalLinks(False)

        self.gridLayout_116.addWidget(self.label_109, 0, 0, 1, 1)

        self.label_110 = QLabel(self.frame_107)
        self.label_110.setObjectName("label_110")

        self.gridLayout_116.addWidget(self.label_110, 0, 1, 1, 1)

        self.frame_108 = QFrame(self.frame_107)
        self.frame_108.setObjectName("frame_108")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.gridLayout_117 = QGridLayout(self.frame_108)
        self.gridLayout_117.setObjectName("gridLayout_117")
        self.gridLayout_117.setHorizontalSpacing(5)
        self.gridLayout_117.setContentsMargins(0, 0, 0, 0)
        self.toolButton_125 = QToolButton(self.frame_108)
        self.toolButton_125.setObjectName("toolButton_125")
        self.toolButton_125.setMinimumSize(QSize(50, 50))
        self.toolButton_125.setMaximumSize(QSize(50, 50))
        self.toolButton_125.setIcon(icon4)

        self.gridLayout_117.addWidget(self.toolButton_125, 0, 1, 1, 1)

        self.lineEdit_51 = QLineEdit(self.frame_108)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.lineEdit_51.setMinimumSize(QSize(0, 50))

        self.gridLayout_117.addWidget(self.lineEdit_51, 0, 0, 1, 1)

        self.toolButton_126 = QToolButton(self.frame_108)
        self.toolButton_126.setObjectName("toolButton_126")
        self.toolButton_126.setMinimumSize(QSize(50, 50))
        self.toolButton_126.setMaximumSize(QSize(50, 50))
        self.toolButton_126.setIcon(icon5)

        self.gridLayout_117.addWidget(self.toolButton_126, 0, 2, 1, 1)

        self.gridLayout_116.addWidget(self.frame_108, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_107, 4, 0, 1, 1)

        self.frame_32 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_32.setObjectName("frame_32")
        self.frame_32.setMinimumSize(QSize(0, 200))
        self.frame_32.setMaximumSize(QSize(16777215, 200))
        self.frame_32.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_32)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.gridLayout_38.setContentsMargins(20, 20, 20, 20)
        self.label_31 = QLabel(self.frame_32)
        self.label_31.setObjectName("label_31")

        self.gridLayout_38.addWidget(self.label_31, 0, 1, 1, 1)

        self.label_32 = QLabel(self.frame_32)
        self.label_32.setObjectName("label_32")
        self.label_32.setMinimumSize(QSize(90, 30))
        self.label_32.setMaximumSize(QSize(90, 30))
        self.label_32.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_32.setTextFormat(Qt.AutoText)
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setWordWrap(False)
        self.label_32.setOpenExternalLinks(False)

        self.gridLayout_38.addWidget(self.label_32, 0, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName("frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_34)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.gridLayout_39.setHorizontalSpacing(5)
        self.gridLayout_39.setVerticalSpacing(0)
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.toolButton_39 = QToolButton(self.frame_34)
        self.toolButton_39.setObjectName("toolButton_39")
        self.toolButton_39.setMinimumSize(QSize(50, 50))
        self.toolButton_39.setMaximumSize(QSize(50, 50))
        self.toolButton_39.setIcon(icon4)

        self.gridLayout_39.addWidget(self.toolButton_39, 0, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_34)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 50))

        self.gridLayout_39.addWidget(self.lineEdit_8, 0, 0, 1, 1)

        self.toolButton_40 = QToolButton(self.frame_34)
        self.toolButton_40.setObjectName("toolButton_40")
        self.toolButton_40.setMinimumSize(QSize(50, 50))
        self.toolButton_40.setMaximumSize(QSize(50, 50))
        self.toolButton_40.setIcon(icon5)

        self.gridLayout_39.addWidget(self.toolButton_40, 0, 2, 1, 1)

        self.gridLayout_38.addWidget(self.frame_34, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_32, 0, 0, 1, 1)

        self.frame_115 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_115.setObjectName("frame_115")
        self.frame_115.setMinimumSize(QSize(0, 200))
        self.frame_115.setMaximumSize(QSize(16777215, 200))
        self.frame_115.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.gridLayout_124 = QGridLayout(self.frame_115)
        self.gridLayout_124.setObjectName("gridLayout_124")
        self.gridLayout_124.setContentsMargins(20, 20, 20, 20)
        self.label_117 = QLabel(self.frame_115)
        self.label_117.setObjectName("label_117")
        self.label_117.setMinimumSize(QSize(30, 30))
        self.label_117.setMaximumSize(QSize(30, 30))
        self.label_117.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_117.setTextFormat(Qt.AutoText)
        self.label_117.setScaledContents(True)
        self.label_117.setAlignment(Qt.AlignCenter)
        self.label_117.setWordWrap(False)
        self.label_117.setOpenExternalLinks(False)

        self.gridLayout_124.addWidget(self.label_117, 0, 0, 1, 1)

        self.label_118 = QLabel(self.frame_115)
        self.label_118.setObjectName("label_118")

        self.gridLayout_124.addWidget(self.label_118, 0, 1, 1, 1)

        self.frame_116 = QFrame(self.frame_115)
        self.frame_116.setObjectName("frame_116")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.gridLayout_125 = QGridLayout(self.frame_116)
        self.gridLayout_125.setObjectName("gridLayout_125")
        self.gridLayout_125.setHorizontalSpacing(5)
        self.gridLayout_125.setContentsMargins(0, 0, 0, 0)
        self.toolButton_129 = QToolButton(self.frame_116)
        self.toolButton_129.setObjectName("toolButton_129")
        self.toolButton_129.setMinimumSize(QSize(50, 50))
        self.toolButton_129.setMaximumSize(QSize(50, 50))
        self.toolButton_129.setIcon(icon4)

        self.gridLayout_125.addWidget(self.toolButton_129, 0, 1, 1, 1)

        self.lineEdit_53 = QLineEdit(self.frame_116)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_53.setMinimumSize(QSize(0, 50))

        self.gridLayout_125.addWidget(self.lineEdit_53, 0, 0, 1, 1)

        self.toolButton_130 = QToolButton(self.frame_116)
        self.toolButton_130.setObjectName("toolButton_130")
        self.toolButton_130.setMinimumSize(QSize(50, 50))
        self.toolButton_130.setMaximumSize(QSize(50, 50))
        self.toolButton_130.setIcon(icon5)

        self.gridLayout_125.addWidget(self.toolButton_130, 0, 2, 1, 1)

        self.gridLayout_124.addWidget(self.frame_116, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_115, 5, 0, 1, 1)

        self.frame_125 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_125.setObjectName("frame_125")
        self.frame_125.setMinimumSize(QSize(0, 200))
        self.frame_125.setMaximumSize(QSize(16777215, 200))
        self.frame_125.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.gridLayout_134 = QGridLayout(self.frame_125)
        self.gridLayout_134.setObjectName("gridLayout_134")
        self.gridLayout_134.setContentsMargins(20, 20, 20, 20)
        self.label_127 = QLabel(self.frame_125)
        self.label_127.setObjectName("label_127")
        self.label_127.setMinimumSize(QSize(70, 30))
        self.label_127.setMaximumSize(QSize(70, 30))
        self.label_127.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_127.setTextFormat(Qt.AutoText)
        self.label_127.setScaledContents(True)
        self.label_127.setAlignment(Qt.AlignCenter)
        self.label_127.setWordWrap(False)
        self.label_127.setOpenExternalLinks(False)

        self.gridLayout_134.addWidget(self.label_127, 0, 0, 1, 1)

        self.label_128 = QLabel(self.frame_125)
        self.label_128.setObjectName("label_128")

        self.gridLayout_134.addWidget(self.label_128, 0, 1, 1, 1)

        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName("frame_126")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.gridLayout_135 = QGridLayout(self.frame_126)
        self.gridLayout_135.setObjectName("gridLayout_135")
        self.gridLayout_135.setHorizontalSpacing(5)
        self.gridLayout_135.setContentsMargins(0, 0, 0, 0)
        self.toolButton_143 = QToolButton(self.frame_126)
        self.toolButton_143.setObjectName("toolButton_143")
        self.toolButton_143.setMinimumSize(QSize(50, 50))
        self.toolButton_143.setMaximumSize(QSize(50, 50))
        self.toolButton_143.setIcon(icon4)

        self.gridLayout_135.addWidget(self.toolButton_143, 0, 1, 1, 1)

        self.lineEdit_60 = QLineEdit(self.frame_126)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.lineEdit_60.setMinimumSize(QSize(0, 50))

        self.gridLayout_135.addWidget(self.lineEdit_60, 0, 0, 1, 1)

        self.toolButton_144 = QToolButton(self.frame_126)
        self.toolButton_144.setObjectName("toolButton_144")
        self.toolButton_144.setMinimumSize(QSize(50, 50))
        self.toolButton_144.setMaximumSize(QSize(50, 50))
        self.toolButton_144.setIcon(icon5)

        self.gridLayout_135.addWidget(self.toolButton_144, 0, 2, 1, 1)

        self.gridLayout_134.addWidget(self.frame_126, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_125, 6, 0, 1, 1)

        self.frame_117 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_117.setObjectName("frame_117")
        self.frame_117.setMinimumSize(QSize(0, 200))
        self.frame_117.setMaximumSize(QSize(16777215, 200))
        self.frame_117.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.gridLayout_126 = QGridLayout(self.frame_117)
        self.gridLayout_126.setObjectName("gridLayout_126")
        self.gridLayout_126.setContentsMargins(20, 20, 20, 20)
        self.label_119 = QLabel(self.frame_117)
        self.label_119.setObjectName("label_119")
        self.label_119.setMinimumSize(QSize(110, 30))
        self.label_119.setMaximumSize(QSize(110, 30))
        self.label_119.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_119.setTextFormat(Qt.AutoText)
        self.label_119.setScaledContents(True)
        self.label_119.setAlignment(Qt.AlignCenter)
        self.label_119.setWordWrap(False)
        self.label_119.setOpenExternalLinks(False)

        self.gridLayout_126.addWidget(self.label_119, 0, 0, 1, 1)

        self.label_120 = QLabel(self.frame_117)
        self.label_120.setObjectName("label_120")

        self.gridLayout_126.addWidget(self.label_120, 0, 1, 1, 1)

        self.frame_118 = QFrame(self.frame_117)
        self.frame_118.setObjectName("frame_118")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.gridLayout_127 = QGridLayout(self.frame_118)
        self.gridLayout_127.setObjectName("gridLayout_127")
        self.gridLayout_127.setHorizontalSpacing(5)
        self.gridLayout_127.setContentsMargins(0, 0, 0, 0)
        self.toolButton_131 = QToolButton(self.frame_118)
        self.toolButton_131.setObjectName("toolButton_131")
        self.toolButton_131.setMinimumSize(QSize(50, 50))
        self.toolButton_131.setMaximumSize(QSize(50, 50))
        self.toolButton_131.setIcon(icon4)

        self.gridLayout_127.addWidget(self.toolButton_131, 0, 1, 1, 1)

        self.lineEdit_54 = QLineEdit(self.frame_118)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.lineEdit_54.setMinimumSize(QSize(0, 50))

        self.gridLayout_127.addWidget(self.lineEdit_54, 0, 0, 1, 1)

        self.toolButton_132 = QToolButton(self.frame_118)
        self.toolButton_132.setObjectName("toolButton_132")
        self.toolButton_132.setMinimumSize(QSize(50, 50))
        self.toolButton_132.setMaximumSize(QSize(50, 50))
        self.toolButton_132.setIcon(icon5)

        self.gridLayout_127.addWidget(self.toolButton_132, 0, 2, 1, 1)

        self.gridLayout_126.addWidget(self.frame_118, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_117, 16, 0, 1, 1)

        self.frame_127 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_127.setObjectName("frame_127")
        self.frame_127.setMinimumSize(QSize(0, 200))
        self.frame_127.setMaximumSize(QSize(16777215, 200))
        self.frame_127.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.gridLayout_136 = QGridLayout(self.frame_127)
        self.gridLayout_136.setObjectName("gridLayout_136")
        self.gridLayout_136.setContentsMargins(20, 20, 20, 20)
        self.label_129 = QLabel(self.frame_127)
        self.label_129.setObjectName("label_129")
        self.label_129.setMinimumSize(QSize(80, 30))
        self.label_129.setMaximumSize(QSize(80, 30))
        self.label_129.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_129.setTextFormat(Qt.AutoText)
        self.label_129.setScaledContents(True)
        self.label_129.setAlignment(Qt.AlignCenter)
        self.label_129.setWordWrap(False)
        self.label_129.setOpenExternalLinks(False)

        self.gridLayout_136.addWidget(self.label_129, 0, 0, 1, 1)

        self.label_130 = QLabel(self.frame_127)
        self.label_130.setObjectName("label_130")

        self.gridLayout_136.addWidget(self.label_130, 0, 1, 1, 1)

        self.frame_128 = QFrame(self.frame_127)
        self.frame_128.setObjectName("frame_128")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.gridLayout_137 = QGridLayout(self.frame_128)
        self.gridLayout_137.setObjectName("gridLayout_137")
        self.gridLayout_137.setHorizontalSpacing(5)
        self.gridLayout_137.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_61 = QLineEdit(self.frame_128)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.lineEdit_61.setMinimumSize(QSize(0, 50))

        self.gridLayout_137.addWidget(self.lineEdit_61, 0, 0, 1, 1)

        self.toolButton_145 = QToolButton(self.frame_128)
        self.toolButton_145.setObjectName("toolButton_145")
        self.toolButton_145.setMinimumSize(QSize(50, 50))
        self.toolButton_145.setMaximumSize(QSize(50, 50))
        self.toolButton_145.setIcon(icon5)

        self.gridLayout_137.addWidget(self.toolButton_145, 0, 2, 1, 1)

        self.toolButton_146 = QToolButton(self.frame_128)
        self.toolButton_146.setObjectName("toolButton_146")
        self.toolButton_146.setMinimumSize(QSize(50, 50))
        self.toolButton_146.setMaximumSize(QSize(50, 50))
        self.toolButton_146.setIcon(icon4)

        self.gridLayout_137.addWidget(self.toolButton_146, 0, 1, 1, 1)

        self.gridLayout_136.addWidget(self.frame_128, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_127, 17, 0, 1, 1)

        self.frame_131 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_131.setObjectName("frame_131")
        self.frame_131.setMinimumSize(QSize(0, 200))
        self.frame_131.setMaximumSize(QSize(16777215, 200))
        self.frame_131.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.gridLayout_140 = QGridLayout(self.frame_131)
        self.gridLayout_140.setObjectName("gridLayout_140")
        self.gridLayout_140.setContentsMargins(20, 20, 20, 20)
        self.label_133 = QLabel(self.frame_131)
        self.label_133.setObjectName("label_133")
        self.label_133.setMinimumSize(QSize(50, 30))
        self.label_133.setMaximumSize(QSize(50, 30))
        self.label_133.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_133.setTextFormat(Qt.AutoText)
        self.label_133.setScaledContents(True)
        self.label_133.setAlignment(Qt.AlignCenter)
        self.label_133.setWordWrap(False)
        self.label_133.setOpenExternalLinks(False)

        self.gridLayout_140.addWidget(self.label_133, 0, 0, 1, 1)

        self.label_134 = QLabel(self.frame_131)
        self.label_134.setObjectName("label_134")

        self.gridLayout_140.addWidget(self.label_134, 0, 1, 1, 1)

        self.frame_132 = QFrame(self.frame_131)
        self.frame_132.setObjectName("frame_132")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.gridLayout_141 = QGridLayout(self.frame_132)
        self.gridLayout_141.setObjectName("gridLayout_141")
        self.gridLayout_141.setHorizontalSpacing(5)
        self.gridLayout_141.setContentsMargins(0, 0, 0, 0)
        self.toolButton_149 = QToolButton(self.frame_132)
        self.toolButton_149.setObjectName("toolButton_149")
        self.toolButton_149.setMinimumSize(QSize(50, 50))
        self.toolButton_149.setMaximumSize(QSize(50, 50))
        self.toolButton_149.setIcon(icon4)

        self.gridLayout_141.addWidget(self.toolButton_149, 0, 1, 1, 1)

        self.lineEdit_63 = QLineEdit(self.frame_132)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.lineEdit_63.setMinimumSize(QSize(0, 50))

        self.gridLayout_141.addWidget(self.lineEdit_63, 0, 0, 1, 1)

        self.toolButton_150 = QToolButton(self.frame_132)
        self.toolButton_150.setObjectName("toolButton_150")
        self.toolButton_150.setMinimumSize(QSize(50, 50))
        self.toolButton_150.setMaximumSize(QSize(50, 50))
        self.toolButton_150.setIcon(icon5)

        self.gridLayout_141.addWidget(self.toolButton_150, 0, 2, 1, 1)

        self.gridLayout_140.addWidget(self.frame_132, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_131, 7, 0, 1, 1)

        self.frame_143 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_143.setObjectName("frame_143")
        self.frame_143.setMinimumSize(QSize(0, 200))
        self.frame_143.setMaximumSize(QSize(16777215, 200))
        self.frame_143.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.gridLayout_152 = QGridLayout(self.frame_143)
        self.gridLayout_152.setObjectName("gridLayout_152")
        self.gridLayout_152.setContentsMargins(20, 20, 20, 20)
        self.label_145 = QLabel(self.frame_143)
        self.label_145.setObjectName("label_145")
        self.label_145.setMinimumSize(QSize(30, 30))
        self.label_145.setMaximumSize(QSize(30, 30))
        self.label_145.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_145.setTextFormat(Qt.AutoText)
        self.label_145.setScaledContents(True)
        self.label_145.setAlignment(Qt.AlignCenter)
        self.label_145.setWordWrap(False)
        self.label_145.setOpenExternalLinks(False)

        self.gridLayout_152.addWidget(self.label_145, 0, 0, 1, 1)

        self.label_146 = QLabel(self.frame_143)
        self.label_146.setObjectName("label_146")

        self.gridLayout_152.addWidget(self.label_146, 0, 1, 1, 1)

        self.frame_144 = QFrame(self.frame_143)
        self.frame_144.setObjectName("frame_144")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.gridLayout_153 = QGridLayout(self.frame_144)
        self.gridLayout_153.setObjectName("gridLayout_153")
        self.gridLayout_153.setHorizontalSpacing(5)
        self.gridLayout_153.setContentsMargins(0, 0, 0, 0)
        self.toolButton_162 = QToolButton(self.frame_144)
        self.toolButton_162.setObjectName("toolButton_162")
        self.toolButton_162.setMinimumSize(QSize(50, 50))
        self.toolButton_162.setMaximumSize(QSize(50, 50))
        self.toolButton_162.setIcon(icon5)

        self.gridLayout_153.addWidget(self.toolButton_162, 0, 2, 1, 1)

        self.toolButton_161 = QToolButton(self.frame_144)
        self.toolButton_161.setObjectName("toolButton_161")
        self.toolButton_161.setMinimumSize(QSize(50, 50))
        self.toolButton_161.setMaximumSize(QSize(50, 50))
        self.toolButton_161.setIcon(icon4)

        self.gridLayout_153.addWidget(self.toolButton_161, 0, 1, 1, 1)

        self.lineEdit_69 = QLineEdit(self.frame_144)
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.lineEdit_69.setMinimumSize(QSize(0, 50))

        self.gridLayout_153.addWidget(self.lineEdit_69, 0, 0, 1, 1)

        self.gridLayout_152.addWidget(self.frame_144, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_143, 13, 0, 1, 1)

        self.frame_147 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_147.setObjectName("frame_147")
        self.frame_147.setMinimumSize(QSize(0, 200))
        self.frame_147.setMaximumSize(QSize(16777215, 200))
        self.frame_147.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.gridLayout_156 = QGridLayout(self.frame_147)
        self.gridLayout_156.setObjectName("gridLayout_156")
        self.gridLayout_156.setContentsMargins(20, 20, 20, 20)
        self.label_149 = QLabel(self.frame_147)
        self.label_149.setObjectName("label_149")
        self.label_149.setMinimumSize(QSize(80, 30))
        self.label_149.setMaximumSize(QSize(80, 30))
        self.label_149.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_149.setTextFormat(Qt.AutoText)
        self.label_149.setScaledContents(True)
        self.label_149.setAlignment(Qt.AlignCenter)
        self.label_149.setWordWrap(False)
        self.label_149.setOpenExternalLinks(False)

        self.gridLayout_156.addWidget(self.label_149, 0, 0, 1, 1)

        self.label_150 = QLabel(self.frame_147)
        self.label_150.setObjectName("label_150")

        self.gridLayout_156.addWidget(self.label_150, 0, 1, 1, 1)

        self.frame_148 = QFrame(self.frame_147)
        self.frame_148.setObjectName("frame_148")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.gridLayout_157 = QGridLayout(self.frame_148)
        self.gridLayout_157.setObjectName("gridLayout_157")
        self.gridLayout_157.setHorizontalSpacing(5)
        self.gridLayout_157.setContentsMargins(0, 0, 0, 0)
        self.toolButton_165 = QToolButton(self.frame_148)
        self.toolButton_165.setObjectName("toolButton_165")
        self.toolButton_165.setMinimumSize(QSize(50, 50))
        self.toolButton_165.setMaximumSize(QSize(50, 50))
        self.toolButton_165.setIcon(icon4)

        self.gridLayout_157.addWidget(self.toolButton_165, 0, 1, 1, 1)

        self.lineEdit_71 = QLineEdit(self.frame_148)
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.lineEdit_71.setMinimumSize(QSize(0, 50))

        self.gridLayout_157.addWidget(self.lineEdit_71, 0, 0, 1, 1)

        self.toolButton_166 = QToolButton(self.frame_148)
        self.toolButton_166.setObjectName("toolButton_166")
        self.toolButton_166.setMinimumSize(QSize(50, 50))
        self.toolButton_166.setMaximumSize(QSize(50, 50))
        self.toolButton_166.setIcon(icon5)

        self.gridLayout_157.addWidget(self.toolButton_166, 0, 2, 1, 1)

        self.gridLayout_156.addWidget(self.frame_148, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_147, 18, 0, 1, 1)

        self.frame_121 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_121.setObjectName("frame_121")
        self.frame_121.setMinimumSize(QSize(0, 200))
        self.frame_121.setMaximumSize(QSize(16777215, 200))
        self.frame_121.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.gridLayout_130 = QGridLayout(self.frame_121)
        self.gridLayout_130.setObjectName("gridLayout_130")
        self.gridLayout_130.setContentsMargins(20, 20, 20, 20)
        self.label_123 = QLabel(self.frame_121)
        self.label_123.setObjectName("label_123")
        self.label_123.setMinimumSize(QSize(110, 30))
        self.label_123.setMaximumSize(QSize(110, 30))
        self.label_123.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_123.setTextFormat(Qt.AutoText)
        self.label_123.setScaledContents(True)
        self.label_123.setAlignment(Qt.AlignCenter)
        self.label_123.setWordWrap(False)
        self.label_123.setOpenExternalLinks(False)

        self.gridLayout_130.addWidget(self.label_123, 0, 0, 1, 1)

        self.label_124 = QLabel(self.frame_121)
        self.label_124.setObjectName("label_124")

        self.gridLayout_130.addWidget(self.label_124, 0, 1, 1, 1)

        self.frame_122 = QFrame(self.frame_121)
        self.frame_122.setObjectName("frame_122")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.gridLayout_131 = QGridLayout(self.frame_122)
        self.gridLayout_131.setObjectName("gridLayout_131")
        self.gridLayout_131.setHorizontalSpacing(5)
        self.gridLayout_131.setContentsMargins(0, 0, 0, 0)
        self.toolButton_137 = QToolButton(self.frame_122)
        self.toolButton_137.setObjectName("toolButton_137")
        self.toolButton_137.setMinimumSize(QSize(50, 50))
        self.toolButton_137.setMaximumSize(QSize(50, 50))
        self.toolButton_137.setIcon(icon4)

        self.gridLayout_131.addWidget(self.toolButton_137, 0, 1, 1, 1)

        self.lineEdit_57 = QLineEdit(self.frame_122)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.lineEdit_57.setMinimumSize(QSize(0, 50))

        self.gridLayout_131.addWidget(self.lineEdit_57, 0, 0, 1, 1)

        self.toolButton_138 = QToolButton(self.frame_122)
        self.toolButton_138.setObjectName("toolButton_138")
        self.toolButton_138.setMinimumSize(QSize(50, 50))
        self.toolButton_138.setMaximumSize(QSize(50, 50))
        self.toolButton_138.setIcon(icon5)

        self.gridLayout_131.addWidget(self.toolButton_138, 0, 2, 1, 1)

        self.gridLayout_130.addWidget(self.frame_122, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_121, 15, 0, 1, 1)

        self.frame_141 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_141.setObjectName("frame_141")
        self.frame_141.setMinimumSize(QSize(0, 200))
        self.frame_141.setMaximumSize(QSize(16777215, 200))
        self.frame_141.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.gridLayout_150 = QGridLayout(self.frame_141)
        self.gridLayout_150.setObjectName("gridLayout_150")
        self.gridLayout_150.setContentsMargins(20, 20, 20, 20)
        self.label_143 = QLabel(self.frame_141)
        self.label_143.setObjectName("label_143")
        self.label_143.setMinimumSize(QSize(80, 30))
        self.label_143.setMaximumSize(QSize(80, 30))
        self.label_143.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_143.setTextFormat(Qt.AutoText)
        self.label_143.setScaledContents(True)
        self.label_143.setAlignment(Qt.AlignCenter)
        self.label_143.setWordWrap(False)
        self.label_143.setOpenExternalLinks(False)

        self.gridLayout_150.addWidget(self.label_143, 0, 0, 1, 1)

        self.label_144 = QLabel(self.frame_141)
        self.label_144.setObjectName("label_144")

        self.gridLayout_150.addWidget(self.label_144, 0, 1, 1, 1)

        self.frame_142 = QFrame(self.frame_141)
        self.frame_142.setObjectName("frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.gridLayout_151 = QGridLayout(self.frame_142)
        self.gridLayout_151.setObjectName("gridLayout_151")
        self.gridLayout_151.setHorizontalSpacing(5)
        self.gridLayout_151.setContentsMargins(0, 0, 0, 0)
        self.toolButton_159 = QToolButton(self.frame_142)
        self.toolButton_159.setObjectName("toolButton_159")
        self.toolButton_159.setMinimumSize(QSize(50, 50))
        self.toolButton_159.setMaximumSize(QSize(50, 50))
        self.toolButton_159.setIcon(icon4)

        self.gridLayout_151.addWidget(self.toolButton_159, 0, 1, 1, 1)

        self.lineEdit_68 = QLineEdit(self.frame_142)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.lineEdit_68.setMinimumSize(QSize(0, 50))

        self.gridLayout_151.addWidget(self.lineEdit_68, 0, 0, 1, 1)

        self.toolButton_160 = QToolButton(self.frame_142)
        self.toolButton_160.setObjectName("toolButton_160")
        self.toolButton_160.setMinimumSize(QSize(50, 50))
        self.toolButton_160.setMaximumSize(QSize(50, 50))
        self.toolButton_160.setIcon(icon5)

        self.gridLayout_151.addWidget(self.toolButton_160, 0, 2, 1, 1)

        self.gridLayout_150.addWidget(self.frame_142, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_141, 14, 0, 1, 1)

        self.frame_149 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_149.setObjectName("frame_149")
        self.frame_149.setMinimumSize(QSize(0, 200))
        self.frame_149.setMaximumSize(QSize(16777215, 200))
        self.frame_149.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.gridLayout_158 = QGridLayout(self.frame_149)
        self.gridLayout_158.setObjectName("gridLayout_158")
        self.gridLayout_158.setContentsMargins(20, 20, 20, 20)
        self.label_151 = QLabel(self.frame_149)
        self.label_151.setObjectName("label_151")
        self.label_151.setMinimumSize(QSize(30, 30))
        self.label_151.setMaximumSize(QSize(30, 30))
        self.label_151.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_151.setTextFormat(Qt.AutoText)
        self.label_151.setScaledContents(True)
        self.label_151.setAlignment(Qt.AlignCenter)
        self.label_151.setWordWrap(False)
        self.label_151.setOpenExternalLinks(False)

        self.gridLayout_158.addWidget(self.label_151, 0, 0, 1, 1)

        self.label_152 = QLabel(self.frame_149)
        self.label_152.setObjectName("label_152")

        self.gridLayout_158.addWidget(self.label_152, 0, 1, 1, 1)

        self.frame_150 = QFrame(self.frame_149)
        self.frame_150.setObjectName("frame_150")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.gridLayout_159 = QGridLayout(self.frame_150)
        self.gridLayout_159.setObjectName("gridLayout_159")
        self.gridLayout_159.setHorizontalSpacing(5)
        self.gridLayout_159.setContentsMargins(0, 0, 0, 0)
        self.toolButton_167 = QToolButton(self.frame_150)
        self.toolButton_167.setObjectName("toolButton_167")
        self.toolButton_167.setMinimumSize(QSize(50, 50))
        self.toolButton_167.setMaximumSize(QSize(50, 50))
        self.toolButton_167.setIcon(icon4)

        self.gridLayout_159.addWidget(self.toolButton_167, 0, 1, 1, 1)

        self.lineEdit_72 = QLineEdit(self.frame_150)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.lineEdit_72.setMinimumSize(QSize(0, 50))

        self.gridLayout_159.addWidget(self.lineEdit_72, 0, 0, 1, 1)

        self.toolButton_168 = QToolButton(self.frame_150)
        self.toolButton_168.setObjectName("toolButton_168")
        self.toolButton_168.setMinimumSize(QSize(50, 50))
        self.toolButton_168.setMaximumSize(QSize(50, 50))
        self.toolButton_168.setIcon(icon5)

        self.gridLayout_159.addWidget(self.toolButton_168, 0, 2, 1, 1)

        self.gridLayout_158.addWidget(self.frame_150, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_149, 10, 0, 1, 1)

        self.frame_119 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_119.setObjectName("frame_119")
        self.frame_119.setMinimumSize(QSize(0, 200))
        self.frame_119.setMaximumSize(QSize(16777215, 200))
        self.frame_119.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.gridLayout_128 = QGridLayout(self.frame_119)
        self.gridLayout_128.setObjectName("gridLayout_128")
        self.gridLayout_128.setContentsMargins(20, 20, 20, 20)
        self.label_121 = QLabel(self.frame_119)
        self.label_121.setObjectName("label_121")
        self.label_121.setMinimumSize(QSize(80, 30))
        self.label_121.setMaximumSize(QSize(80, 30))
        self.label_121.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_121.setTextFormat(Qt.AutoText)
        self.label_121.setScaledContents(True)
        self.label_121.setAlignment(Qt.AlignCenter)
        self.label_121.setWordWrap(False)
        self.label_121.setOpenExternalLinks(False)

        self.gridLayout_128.addWidget(self.label_121, 0, 0, 1, 1)

        self.label_122 = QLabel(self.frame_119)
        self.label_122.setObjectName("label_122")

        self.gridLayout_128.addWidget(self.label_122, 0, 1, 1, 1)

        self.frame_120 = QFrame(self.frame_119)
        self.frame_120.setObjectName("frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.gridLayout_129 = QGridLayout(self.frame_120)
        self.gridLayout_129.setObjectName("gridLayout_129")
        self.gridLayout_129.setHorizontalSpacing(5)
        self.gridLayout_129.setContentsMargins(0, 0, 0, 0)
        self.toolButton_134 = QToolButton(self.frame_120)
        self.toolButton_134.setObjectName("toolButton_134")
        self.toolButton_134.setMinimumSize(QSize(50, 50))
        self.toolButton_134.setMaximumSize(QSize(50, 50))
        self.toolButton_134.setIcon(icon5)

        self.gridLayout_129.addWidget(self.toolButton_134, 0, 2, 1, 1)

        self.toolButton_133 = QToolButton(self.frame_120)
        self.toolButton_133.setObjectName("toolButton_133")
        self.toolButton_133.setMinimumSize(QSize(50, 50))
        self.toolButton_133.setMaximumSize(QSize(50, 50))
        self.toolButton_133.setIcon(icon4)

        self.gridLayout_129.addWidget(self.toolButton_133, 0, 1, 1, 1)

        self.lineEdit_55 = QLineEdit(self.frame_120)
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.lineEdit_55.setMinimumSize(QSize(0, 50))

        self.gridLayout_129.addWidget(self.lineEdit_55, 0, 0, 1, 1)

        self.gridLayout_128.addWidget(self.frame_120, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_119, 19, 0, 1, 1)

        self.frame_139 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_139.setObjectName("frame_139")
        self.frame_139.setMinimumSize(QSize(0, 200))
        self.frame_139.setMaximumSize(QSize(16777215, 200))
        self.frame_139.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.gridLayout_148 = QGridLayout(self.frame_139)
        self.gridLayout_148.setObjectName("gridLayout_148")
        self.gridLayout_148.setContentsMargins(20, 20, 20, 20)
        self.label_141 = QLabel(self.frame_139)
        self.label_141.setObjectName("label_141")
        self.label_141.setMinimumSize(QSize(100, 30))
        self.label_141.setMaximumSize(QSize(100, 30))
        self.label_141.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_141.setTextFormat(Qt.AutoText)
        self.label_141.setScaledContents(True)
        self.label_141.setAlignment(Qt.AlignCenter)
        self.label_141.setWordWrap(False)
        self.label_141.setOpenExternalLinks(False)

        self.gridLayout_148.addWidget(self.label_141, 0, 0, 1, 1)

        self.label_142 = QLabel(self.frame_139)
        self.label_142.setObjectName("label_142")

        self.gridLayout_148.addWidget(self.label_142, 0, 1, 1, 1)

        self.frame_140 = QFrame(self.frame_139)
        self.frame_140.setObjectName("frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.gridLayout_149 = QGridLayout(self.frame_140)
        self.gridLayout_149.setObjectName("gridLayout_149")
        self.gridLayout_149.setHorizontalSpacing(5)
        self.gridLayout_149.setContentsMargins(0, 0, 0, 0)
        self.toolButton_157 = QToolButton(self.frame_140)
        self.toolButton_157.setObjectName("toolButton_157")
        self.toolButton_157.setMinimumSize(QSize(50, 50))
        self.toolButton_157.setMaximumSize(QSize(50, 50))
        self.toolButton_157.setIcon(icon4)

        self.gridLayout_149.addWidget(self.toolButton_157, 0, 1, 1, 1)

        self.lineEdit_67 = QLineEdit(self.frame_140)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.lineEdit_67.setMinimumSize(QSize(0, 50))

        self.gridLayout_149.addWidget(self.lineEdit_67, 0, 0, 1, 1)

        self.toolButton_158 = QToolButton(self.frame_140)
        self.toolButton_158.setObjectName("toolButton_158")
        self.toolButton_158.setMinimumSize(QSize(50, 50))
        self.toolButton_158.setMaximumSize(QSize(50, 50))
        self.toolButton_158.setIcon(icon5)

        self.gridLayout_149.addWidget(self.toolButton_158, 0, 2, 1, 1)

        self.gridLayout_148.addWidget(self.frame_140, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_139, 9, 0, 1, 1)

        self.frame_135 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_135.setObjectName("frame_135")
        self.frame_135.setMinimumSize(QSize(0, 200))
        self.frame_135.setMaximumSize(QSize(16777215, 200))
        self.frame_135.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.gridLayout_144 = QGridLayout(self.frame_135)
        self.gridLayout_144.setObjectName("gridLayout_144")
        self.gridLayout_144.setContentsMargins(20, 20, 20, 20)
        self.label_137 = QLabel(self.frame_135)
        self.label_137.setObjectName("label_137")
        self.label_137.setMinimumSize(QSize(50, 30))
        self.label_137.setMaximumSize(QSize(50, 30))
        self.label_137.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_137.setTextFormat(Qt.AutoText)
        self.label_137.setScaledContents(True)
        self.label_137.setAlignment(Qt.AlignCenter)
        self.label_137.setWordWrap(False)
        self.label_137.setOpenExternalLinks(False)

        self.gridLayout_144.addWidget(self.label_137, 0, 0, 1, 1)

        self.label_138 = QLabel(self.frame_135)
        self.label_138.setObjectName("label_138")

        self.gridLayout_144.addWidget(self.label_138, 0, 1, 1, 1)

        self.frame_136 = QFrame(self.frame_135)
        self.frame_136.setObjectName("frame_136")
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.gridLayout_145 = QGridLayout(self.frame_136)
        self.gridLayout_145.setObjectName("gridLayout_145")
        self.gridLayout_145.setHorizontalSpacing(5)
        self.gridLayout_145.setContentsMargins(0, 0, 0, 0)
        self.toolButton_153 = QToolButton(self.frame_136)
        self.toolButton_153.setObjectName("toolButton_153")
        self.toolButton_153.setMinimumSize(QSize(50, 50))
        self.toolButton_153.setMaximumSize(QSize(50, 50))
        self.toolButton_153.setIcon(icon4)

        self.gridLayout_145.addWidget(self.toolButton_153, 0, 1, 1, 1)

        self.lineEdit_65 = QLineEdit(self.frame_136)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.lineEdit_65.setMinimumSize(QSize(0, 50))

        self.gridLayout_145.addWidget(self.lineEdit_65, 0, 0, 1, 1)

        self.toolButton_154 = QToolButton(self.frame_136)
        self.toolButton_154.setObjectName("toolButton_154")
        self.toolButton_154.setMinimumSize(QSize(50, 50))
        self.toolButton_154.setMaximumSize(QSize(50, 50))
        self.toolButton_154.setIcon(icon5)

        self.gridLayout_145.addWidget(self.toolButton_154, 0, 2, 1, 1)

        self.gridLayout_144.addWidget(self.frame_136, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_135, 11, 0, 1, 1)

        self.frame_145 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_145.setObjectName("frame_145")
        self.frame_145.setMinimumSize(QSize(0, 200))
        self.frame_145.setMaximumSize(QSize(16777215, 200))
        self.frame_145.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.gridLayout_154 = QGridLayout(self.frame_145)
        self.gridLayout_154.setObjectName("gridLayout_154")
        self.gridLayout_154.setContentsMargins(20, 20, 20, 20)
        self.label_147 = QLabel(self.frame_145)
        self.label_147.setObjectName("label_147")
        self.label_147.setMinimumSize(QSize(50, 30))
        self.label_147.setMaximumSize(QSize(50, 30))
        self.label_147.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_147.setTextFormat(Qt.AutoText)
        self.label_147.setScaledContents(True)
        self.label_147.setAlignment(Qt.AlignCenter)
        self.label_147.setWordWrap(False)
        self.label_147.setOpenExternalLinks(False)

        self.gridLayout_154.addWidget(self.label_147, 0, 0, 1, 1)

        self.label_148 = QLabel(self.frame_145)
        self.label_148.setObjectName("label_148")

        self.gridLayout_154.addWidget(self.label_148, 0, 1, 1, 1)

        self.frame_146 = QFrame(self.frame_145)
        self.frame_146.setObjectName("frame_146")
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.gridLayout_155 = QGridLayout(self.frame_146)
        self.gridLayout_155.setObjectName("gridLayout_155")
        self.gridLayout_155.setHorizontalSpacing(5)
        self.gridLayout_155.setContentsMargins(0, 0, 0, 0)
        self.toolButton_163 = QToolButton(self.frame_146)
        self.toolButton_163.setObjectName("toolButton_163")
        self.toolButton_163.setMinimumSize(QSize(50, 50))
        self.toolButton_163.setMaximumSize(QSize(50, 50))
        self.toolButton_163.setIcon(icon4)

        self.gridLayout_155.addWidget(self.toolButton_163, 0, 1, 1, 1)

        self.lineEdit_70 = QLineEdit(self.frame_146)
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.lineEdit_70.setMinimumSize(QSize(0, 50))

        self.gridLayout_155.addWidget(self.lineEdit_70, 0, 0, 1, 1)

        self.toolButton_164 = QToolButton(self.frame_146)
        self.toolButton_164.setObjectName("toolButton_164")
        self.toolButton_164.setMinimumSize(QSize(50, 50))
        self.toolButton_164.setMaximumSize(QSize(50, 50))
        self.toolButton_164.setIcon(icon5)

        self.gridLayout_155.addWidget(self.toolButton_164, 0, 2, 1, 1)

        self.gridLayout_154.addWidget(self.frame_146, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_145, 8, 0, 1, 1)

        self.frame_111 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_111.setObjectName("frame_111")
        self.frame_111.setMinimumSize(QSize(0, 200))
        self.frame_111.setMaximumSize(QSize(16777215, 200))
        self.frame_111.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.gridLayout_120 = QGridLayout(self.frame_111)
        self.gridLayout_120.setObjectName("gridLayout_120")
        self.gridLayout_120.setContentsMargins(20, 20, 20, 20)
        self.label_113 = QLabel(self.frame_111)
        self.label_113.setObjectName("label_113")
        self.label_113.setMinimumSize(QSize(110, 30))
        self.label_113.setMaximumSize(QSize(110, 30))
        self.label_113.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_113.setTextFormat(Qt.AutoText)
        self.label_113.setScaledContents(True)
        self.label_113.setAlignment(Qt.AlignCenter)
        self.label_113.setWordWrap(False)
        self.label_113.setOpenExternalLinks(False)

        self.gridLayout_120.addWidget(self.label_113, 0, 0, 1, 1)

        self.label_114 = QLabel(self.frame_111)
        self.label_114.setObjectName("label_114")

        self.gridLayout_120.addWidget(self.label_114, 0, 1, 1, 1)

        self.frame_112 = QFrame(self.frame_111)
        self.frame_112.setObjectName("frame_112")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.gridLayout_121 = QGridLayout(self.frame_112)
        self.gridLayout_121.setObjectName("gridLayout_121")
        self.gridLayout_121.setHorizontalSpacing(5)
        self.gridLayout_121.setContentsMargins(0, 0, 0, 0)
        self.toolButton_127 = QToolButton(self.frame_112)
        self.toolButton_127.setObjectName("toolButton_127")
        self.toolButton_127.setMinimumSize(QSize(50, 50))
        self.toolButton_127.setMaximumSize(QSize(50, 50))
        self.toolButton_127.setIcon(icon4)

        self.gridLayout_121.addWidget(self.toolButton_127, 0, 1, 1, 1)

        self.lineEdit_52 = QLineEdit(self.frame_112)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_52.setMinimumSize(QSize(0, 50))

        self.gridLayout_121.addWidget(self.lineEdit_52, 0, 0, 1, 1)

        self.toolButton_128 = QToolButton(self.frame_112)
        self.toolButton_128.setObjectName("toolButton_128")
        self.toolButton_128.setMinimumSize(QSize(50, 50))
        self.toolButton_128.setMaximumSize(QSize(50, 50))
        self.toolButton_128.setIcon(icon5)

        self.gridLayout_121.addWidget(self.toolButton_128, 0, 2, 1, 1)

        self.gridLayout_120.addWidget(self.frame_112, 1, 0, 1, 2)

        self.gridLayout_8.addWidget(self.frame_111, 3, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_9.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_11 = QGridLayout(self.tab_7)
        self.gridLayout_11.setSpacing(10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.tab_7)
        self.frame_24.setObjectName("frame_24")
        self.frame_24.setMinimumSize(QSize(0, 60))
        self.frame_24.setMaximumSize(QSize(16777215, 60))
        self.frame_24.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_24)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_27.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_24)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')

        self.gridLayout_27.addWidget(self.label_8, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_27.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.gridLayout_11.addWidget(self.frame_24, 0, 0, 1, 1)

        self.scrollArea_3 = QScrollArea(self.tab_7)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollArea_3.setStyleSheet(
            "	border-style: solid;\n"
            "	border-top-color: transparent;\n"
            "	border-right-color: transparent;\n"
            "	border-left-color: transparent;\n"
            "	border-bottom-color: transparent;\n"
            "	border-width: 0px;"
        )
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 958, 3280))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.setSpacing(10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_10.setContentsMargins(20, 20, 20, 20)
        self.frame_179 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_179.setObjectName("frame_179")
        self.frame_179.setMinimumSize(QSize(0, 200))
        self.frame_179.setMaximumSize(QSize(16777215, 200))
        self.frame_179.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.gridLayout_188 = QGridLayout(self.frame_179)
        self.gridLayout_188.setObjectName("gridLayout_188")
        self.gridLayout_188.setContentsMargins(20, 20, 20, 20)
        self.label_181 = QLabel(self.frame_179)
        self.label_181.setObjectName("label_181")
        self.label_181.setMinimumSize(QSize(30, 30))
        self.label_181.setMaximumSize(QSize(30, 30))
        self.label_181.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_181.setTextFormat(Qt.AutoText)
        self.label_181.setScaledContents(True)
        self.label_181.setAlignment(Qt.AlignCenter)
        self.label_181.setWordWrap(False)
        self.label_181.setOpenExternalLinks(False)

        self.gridLayout_188.addWidget(self.label_181, 0, 0, 1, 1)

        self.label_182 = QLabel(self.frame_179)
        self.label_182.setObjectName("label_182")

        self.gridLayout_188.addWidget(self.label_182, 0, 1, 1, 1)

        self.frame_180 = QFrame(self.frame_179)
        self.frame_180.setObjectName("frame_180")
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.gridLayout_189 = QGridLayout(self.frame_180)
        self.gridLayout_189.setObjectName("gridLayout_189")
        self.gridLayout_189.setHorizontalSpacing(5)
        self.gridLayout_189.setContentsMargins(0, 0, 0, 0)
        self.toolButton_193 = QToolButton(self.frame_180)
        self.toolButton_193.setObjectName("toolButton_193")
        self.toolButton_193.setMinimumSize(QSize(50, 50))
        self.toolButton_193.setMaximumSize(QSize(50, 50))
        self.toolButton_193.setIcon(icon4)

        self.gridLayout_189.addWidget(self.toolButton_193, 0, 1, 1, 1)

        self.lineEdit_85 = QLineEdit(self.frame_180)
        self.lineEdit_85.setObjectName("lineEdit_85")
        self.lineEdit_85.setMinimumSize(QSize(0, 50))

        self.gridLayout_189.addWidget(self.lineEdit_85, 0, 0, 1, 1)

        self.toolButton_194 = QToolButton(self.frame_180)
        self.toolButton_194.setObjectName("toolButton_194")
        self.toolButton_194.setMinimumSize(QSize(50, 50))
        self.toolButton_194.setMaximumSize(QSize(50, 50))
        self.toolButton_194.setIcon(icon5)

        self.gridLayout_189.addWidget(self.toolButton_194, 0, 2, 1, 1)

        self.gridLayout_188.addWidget(self.frame_180, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_179, 9, 0, 1, 1)

        self.frame_123 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_123.setObjectName("frame_123")
        self.frame_123.setMinimumSize(QSize(0, 200))
        self.frame_123.setMaximumSize(QSize(16777215, 200))
        self.frame_123.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.gridLayout_132 = QGridLayout(self.frame_123)
        self.gridLayout_132.setObjectName("gridLayout_132")
        self.gridLayout_132.setContentsMargins(20, 20, 20, 20)
        self.label_125 = QLabel(self.frame_123)
        self.label_125.setObjectName("label_125")
        self.label_125.setMinimumSize(QSize(60, 30))
        self.label_125.setMaximumSize(QSize(60, 30))
        self.label_125.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_125.setTextFormat(Qt.AutoText)
        self.label_125.setScaledContents(True)
        self.label_125.setAlignment(Qt.AlignCenter)
        self.label_125.setWordWrap(False)
        self.label_125.setOpenExternalLinks(False)

        self.gridLayout_132.addWidget(self.label_125, 0, 0, 1, 1)

        self.label_126 = QLabel(self.frame_123)
        self.label_126.setObjectName("label_126")

        self.gridLayout_132.addWidget(self.label_126, 0, 1, 1, 1)

        self.frame_124 = QFrame(self.frame_123)
        self.frame_124.setObjectName("frame_124")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.gridLayout_133 = QGridLayout(self.frame_124)
        self.gridLayout_133.setObjectName("gridLayout_133")
        self.gridLayout_133.setHorizontalSpacing(5)
        self.gridLayout_133.setContentsMargins(0, 0, 0, 0)
        self.toolButton_135 = QToolButton(self.frame_124)
        self.toolButton_135.setObjectName("toolButton_135")
        self.toolButton_135.setMinimumSize(QSize(50, 50))
        self.toolButton_135.setMaximumSize(QSize(50, 50))
        self.toolButton_135.setIcon(icon4)

        self.gridLayout_133.addWidget(self.toolButton_135, 0, 1, 1, 1)

        self.lineEdit_56 = QLineEdit(self.frame_124)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.lineEdit_56.setMinimumSize(QSize(0, 50))

        self.gridLayout_133.addWidget(self.lineEdit_56, 0, 0, 1, 1)

        self.toolButton_136 = QToolButton(self.frame_124)
        self.toolButton_136.setObjectName("toolButton_136")
        self.toolButton_136.setMinimumSize(QSize(50, 50))
        self.toolButton_136.setMaximumSize(QSize(50, 50))
        self.toolButton_136.setIcon(icon5)

        self.gridLayout_133.addWidget(self.toolButton_136, 0, 2, 1, 1)

        self.gridLayout_132.addWidget(self.frame_124, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_123, 4, 0, 1, 1)

        self.frame_157 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_157.setObjectName("frame_157")
        self.frame_157.setMinimumSize(QSize(0, 200))
        self.frame_157.setMaximumSize(QSize(16777215, 200))
        self.frame_157.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.gridLayout_166 = QGridLayout(self.frame_157)
        self.gridLayout_166.setObjectName("gridLayout_166")
        self.gridLayout_166.setContentsMargins(20, 20, 20, 20)
        self.label_159 = QLabel(self.frame_157)
        self.label_159.setObjectName("label_159")
        self.label_159.setMinimumSize(QSize(80, 30))
        self.label_159.setMaximumSize(QSize(80, 30))
        self.label_159.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_159.setTextFormat(Qt.AutoText)
        self.label_159.setScaledContents(True)
        self.label_159.setAlignment(Qt.AlignCenter)
        self.label_159.setWordWrap(False)
        self.label_159.setOpenExternalLinks(False)

        self.gridLayout_166.addWidget(self.label_159, 0, 0, 1, 1)

        self.label_160 = QLabel(self.frame_157)
        self.label_160.setObjectName("label_160")

        self.gridLayout_166.addWidget(self.label_160, 0, 1, 1, 1)

        self.frame_158 = QFrame(self.frame_157)
        self.frame_158.setObjectName("frame_158")
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.gridLayout_167 = QGridLayout(self.frame_158)
        self.gridLayout_167.setObjectName("gridLayout_167")
        self.gridLayout_167.setHorizontalSpacing(5)
        self.gridLayout_167.setContentsMargins(0, 0, 0, 0)
        self.toolButton_139 = QToolButton(self.frame_158)
        self.toolButton_139.setObjectName("toolButton_139")
        self.toolButton_139.setMinimumSize(QSize(50, 50))
        self.toolButton_139.setMaximumSize(QSize(50, 50))
        self.toolButton_139.setIcon(icon4)

        self.gridLayout_167.addWidget(self.toolButton_139, 0, 1, 1, 1)

        self.lineEdit_58 = QLineEdit(self.frame_158)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.lineEdit_58.setMinimumSize(QSize(0, 50))

        self.gridLayout_167.addWidget(self.lineEdit_58, 0, 0, 1, 1)

        self.toolButton_140 = QToolButton(self.frame_158)
        self.toolButton_140.setObjectName("toolButton_140")
        self.toolButton_140.setMinimumSize(QSize(50, 50))
        self.toolButton_140.setMaximumSize(QSize(50, 50))
        self.toolButton_140.setIcon(icon5)

        self.gridLayout_167.addWidget(self.toolButton_140, 0, 2, 1, 1)

        self.gridLayout_166.addWidget(self.frame_158, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_157, 5, 0, 1, 1)

        self.frame_183 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_183.setObjectName("frame_183")
        self.frame_183.setMinimumSize(QSize(0, 200))
        self.frame_183.setMaximumSize(QSize(16777215, 200))
        self.frame_183.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)
        self.gridLayout_192 = QGridLayout(self.frame_183)
        self.gridLayout_192.setObjectName("gridLayout_192")
        self.gridLayout_192.setContentsMargins(20, 20, 20, 20)
        self.label_185 = QLabel(self.frame_183)
        self.label_185.setObjectName("label_185")
        self.label_185.setMinimumSize(QSize(50, 30))
        self.label_185.setMaximumSize(QSize(50, 30))
        self.label_185.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_185.setTextFormat(Qt.AutoText)
        self.label_185.setScaledContents(True)
        self.label_185.setAlignment(Qt.AlignCenter)
        self.label_185.setWordWrap(False)
        self.label_185.setOpenExternalLinks(False)

        self.gridLayout_192.addWidget(self.label_185, 0, 0, 1, 1)

        self.label_186 = QLabel(self.frame_183)
        self.label_186.setObjectName("label_186")

        self.gridLayout_192.addWidget(self.label_186, 0, 1, 1, 1)

        self.frame_184 = QFrame(self.frame_183)
        self.frame_184.setObjectName("frame_184")
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.gridLayout_193 = QGridLayout(self.frame_184)
        self.gridLayout_193.setObjectName("gridLayout_193")
        self.gridLayout_193.setHorizontalSpacing(5)
        self.gridLayout_193.setContentsMargins(0, 0, 0, 0)
        self.toolButton_197 = QToolButton(self.frame_184)
        self.toolButton_197.setObjectName("toolButton_197")
        self.toolButton_197.setMinimumSize(QSize(50, 50))
        self.toolButton_197.setMaximumSize(QSize(50, 50))
        self.toolButton_197.setIcon(icon4)

        self.gridLayout_193.addWidget(self.toolButton_197, 0, 1, 1, 1)

        self.lineEdit_87 = QLineEdit(self.frame_184)
        self.lineEdit_87.setObjectName("lineEdit_87")
        self.lineEdit_87.setMinimumSize(QSize(0, 50))

        self.gridLayout_193.addWidget(self.lineEdit_87, 0, 0, 1, 1)

        self.toolButton_198 = QToolButton(self.frame_184)
        self.toolButton_198.setObjectName("toolButton_198")
        self.toolButton_198.setMinimumSize(QSize(50, 50))
        self.toolButton_198.setMaximumSize(QSize(50, 50))
        self.toolButton_198.setIcon(icon5)

        self.gridLayout_193.addWidget(self.toolButton_198, 0, 2, 1, 1)

        self.gridLayout_192.addWidget(self.frame_184, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_183, 8, 0, 1, 1)

        self.frame_173 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_173.setObjectName("frame_173")
        self.frame_173.setMinimumSize(QSize(0, 200))
        self.frame_173.setMaximumSize(QSize(16777215, 200))
        self.frame_173.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.gridLayout_182 = QGridLayout(self.frame_173)
        self.gridLayout_182.setObjectName("gridLayout_182")
        self.gridLayout_182.setContentsMargins(20, 20, 20, 20)
        self.label_175 = QLabel(self.frame_173)
        self.label_175.setObjectName("label_175")
        self.label_175.setMinimumSize(QSize(100, 30))
        self.label_175.setMaximumSize(QSize(100, 30))
        self.label_175.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_175.setTextFormat(Qt.AutoText)
        self.label_175.setScaledContents(True)
        self.label_175.setAlignment(Qt.AlignCenter)
        self.label_175.setWordWrap(False)
        self.label_175.setOpenExternalLinks(False)

        self.gridLayout_182.addWidget(self.label_175, 0, 0, 1, 1)

        self.label_176 = QLabel(self.frame_173)
        self.label_176.setObjectName("label_176")

        self.gridLayout_182.addWidget(self.label_176, 0, 1, 1, 1)

        self.frame_174 = QFrame(self.frame_173)
        self.frame_174.setObjectName("frame_174")
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.gridLayout_183 = QGridLayout(self.frame_174)
        self.gridLayout_183.setObjectName("gridLayout_183")
        self.gridLayout_183.setHorizontalSpacing(5)
        self.gridLayout_183.setContentsMargins(0, 0, 0, 0)
        self.toolButton_187 = QToolButton(self.frame_174)
        self.toolButton_187.setObjectName("toolButton_187")
        self.toolButton_187.setMinimumSize(QSize(50, 50))
        self.toolButton_187.setMaximumSize(QSize(50, 50))
        self.toolButton_187.setIcon(icon4)

        self.gridLayout_183.addWidget(self.toolButton_187, 0, 1, 1, 1)

        self.lineEdit_82 = QLineEdit(self.frame_174)
        self.lineEdit_82.setObjectName("lineEdit_82")
        self.lineEdit_82.setMinimumSize(QSize(0, 50))

        self.gridLayout_183.addWidget(self.lineEdit_82, 0, 0, 1, 1)

        self.toolButton_188 = QToolButton(self.frame_174)
        self.toolButton_188.setObjectName("toolButton_188")
        self.toolButton_188.setMinimumSize(QSize(50, 50))
        self.toolButton_188.setMaximumSize(QSize(50, 50))
        self.toolButton_188.setIcon(icon5)

        self.gridLayout_183.addWidget(self.toolButton_188, 0, 2, 1, 1)

        self.gridLayout_182.addWidget(self.frame_174, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_173, 14, 0, 1, 1)

        self.frame_181 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_181.setObjectName("frame_181")
        self.frame_181.setMinimumSize(QSize(0, 200))
        self.frame_181.setMaximumSize(QSize(16777215, 200))
        self.frame_181.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.gridLayout_190 = QGridLayout(self.frame_181)
        self.gridLayout_190.setObjectName("gridLayout_190")
        self.gridLayout_190.setContentsMargins(20, 20, 20, 20)
        self.label_183 = QLabel(self.frame_181)
        self.label_183.setObjectName("label_183")
        self.label_183.setMinimumSize(QSize(50, 30))
        self.label_183.setMaximumSize(QSize(50, 30))
        self.label_183.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_183.setTextFormat(Qt.AutoText)
        self.label_183.setScaledContents(True)
        self.label_183.setAlignment(Qt.AlignCenter)
        self.label_183.setWordWrap(False)
        self.label_183.setOpenExternalLinks(False)

        self.gridLayout_190.addWidget(self.label_183, 0, 0, 1, 1)

        self.label_184 = QLabel(self.frame_181)
        self.label_184.setObjectName("label_184")

        self.gridLayout_190.addWidget(self.label_184, 0, 1, 1, 1)

        self.frame_182 = QFrame(self.frame_181)
        self.frame_182.setObjectName("frame_182")
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.gridLayout_191 = QGridLayout(self.frame_182)
        self.gridLayout_191.setObjectName("gridLayout_191")
        self.gridLayout_191.setHorizontalSpacing(5)
        self.gridLayout_191.setContentsMargins(0, 0, 0, 0)
        self.toolButton_195 = QToolButton(self.frame_182)
        self.toolButton_195.setObjectName("toolButton_195")
        self.toolButton_195.setMinimumSize(QSize(50, 50))
        self.toolButton_195.setMaximumSize(QSize(50, 50))
        self.toolButton_195.setIcon(icon4)

        self.gridLayout_191.addWidget(self.toolButton_195, 0, 1, 1, 1)

        self.lineEdit_86 = QLineEdit(self.frame_182)
        self.lineEdit_86.setObjectName("lineEdit_86")
        self.lineEdit_86.setMinimumSize(QSize(0, 50))

        self.gridLayout_191.addWidget(self.lineEdit_86, 0, 0, 1, 1)

        self.toolButton_196 = QToolButton(self.frame_182)
        self.toolButton_196.setObjectName("toolButton_196")
        self.toolButton_196.setMinimumSize(QSize(50, 50))
        self.toolButton_196.setMaximumSize(QSize(50, 50))
        self.toolButton_196.setIcon(icon5)

        self.gridLayout_191.addWidget(self.toolButton_196, 0, 2, 1, 1)

        self.gridLayout_190.addWidget(self.frame_182, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_181, 11, 0, 1, 1)

        self.frame_155 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_155.setObjectName("frame_155")
        self.frame_155.setMinimumSize(QSize(0, 200))
        self.frame_155.setMaximumSize(QSize(16777215, 200))
        self.frame_155.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.gridLayout_164 = QGridLayout(self.frame_155)
        self.gridLayout_164.setObjectName("gridLayout_164")
        self.gridLayout_164.setContentsMargins(20, 20, 20, 20)
        self.label_157 = QLabel(self.frame_155)
        self.label_157.setObjectName("label_157")
        self.label_157.setMinimumSize(QSize(70, 30))
        self.label_157.setMaximumSize(QSize(70, 30))
        self.label_157.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_157.setTextFormat(Qt.AutoText)
        self.label_157.setScaledContents(True)
        self.label_157.setAlignment(Qt.AlignCenter)
        self.label_157.setWordWrap(False)
        self.label_157.setOpenExternalLinks(False)

        self.gridLayout_164.addWidget(self.label_157, 0, 0, 1, 1)

        self.label_158 = QLabel(self.frame_155)
        self.label_158.setObjectName("label_158")

        self.gridLayout_164.addWidget(self.label_158, 0, 1, 1, 1)

        self.frame_156 = QFrame(self.frame_155)
        self.frame_156.setObjectName("frame_156")
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.gridLayout_165 = QGridLayout(self.frame_156)
        self.gridLayout_165.setObjectName("gridLayout_165")
        self.gridLayout_165.setHorizontalSpacing(5)
        self.gridLayout_165.setContentsMargins(0, 0, 0, 0)
        self.toolButton_173 = QToolButton(self.frame_156)
        self.toolButton_173.setObjectName("toolButton_173")
        self.toolButton_173.setMinimumSize(QSize(50, 50))
        self.toolButton_173.setMaximumSize(QSize(50, 50))
        self.toolButton_173.setIcon(icon4)

        self.gridLayout_165.addWidget(self.toolButton_173, 0, 1, 1, 1)

        self.lineEdit_75 = QLineEdit(self.frame_156)
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.lineEdit_75.setMinimumSize(QSize(0, 50))

        self.gridLayout_165.addWidget(self.lineEdit_75, 0, 0, 1, 1)

        self.toolButton_174 = QToolButton(self.frame_156)
        self.toolButton_174.setObjectName("toolButton_174")
        self.toolButton_174.setMinimumSize(QSize(50, 50))
        self.toolButton_174.setMaximumSize(QSize(50, 50))
        self.toolButton_174.setIcon(icon5)

        self.gridLayout_165.addWidget(self.toolButton_174, 0, 2, 1, 1)

        self.gridLayout_164.addWidget(self.frame_156, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_155, 12, 0, 1, 1)

        self.frame_175 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_175.setObjectName("frame_175")
        self.frame_175.setMinimumSize(QSize(0, 200))
        self.frame_175.setMaximumSize(QSize(16777215, 200))
        self.frame_175.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.gridLayout_184 = QGridLayout(self.frame_175)
        self.gridLayout_184.setObjectName("gridLayout_184")
        self.gridLayout_184.setContentsMargins(20, 20, 20, 20)
        self.label_177 = QLabel(self.frame_175)
        self.label_177.setObjectName("label_177")
        self.label_177.setMinimumSize(QSize(60, 30))
        self.label_177.setMaximumSize(QSize(60, 30))
        self.label_177.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_177.setTextFormat(Qt.AutoText)
        self.label_177.setScaledContents(True)
        self.label_177.setAlignment(Qt.AlignCenter)
        self.label_177.setWordWrap(False)
        self.label_177.setOpenExternalLinks(False)

        self.gridLayout_184.addWidget(self.label_177, 0, 0, 1, 1)

        self.label_178 = QLabel(self.frame_175)
        self.label_178.setObjectName("label_178")

        self.gridLayout_184.addWidget(self.label_178, 0, 1, 1, 1)

        self.frame_176 = QFrame(self.frame_175)
        self.frame_176.setObjectName("frame_176")
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.gridLayout_185 = QGridLayout(self.frame_176)
        self.gridLayout_185.setObjectName("gridLayout_185")
        self.gridLayout_185.setHorizontalSpacing(5)
        self.gridLayout_185.setContentsMargins(0, 0, 0, 0)
        self.toolButton_189 = QToolButton(self.frame_176)
        self.toolButton_189.setObjectName("toolButton_189")
        self.toolButton_189.setMinimumSize(QSize(50, 50))
        self.toolButton_189.setMaximumSize(QSize(50, 50))
        self.toolButton_189.setIcon(icon4)

        self.gridLayout_185.addWidget(self.toolButton_189, 0, 1, 1, 1)

        self.lineEdit_83 = QLineEdit(self.frame_176)
        self.lineEdit_83.setObjectName("lineEdit_83")
        self.lineEdit_83.setMinimumSize(QSize(0, 50))

        self.gridLayout_185.addWidget(self.lineEdit_83, 0, 0, 1, 1)

        self.toolButton_190 = QToolButton(self.frame_176)
        self.toolButton_190.setObjectName("toolButton_190")
        self.toolButton_190.setMinimumSize(QSize(50, 50))
        self.toolButton_190.setMaximumSize(QSize(50, 50))
        self.toolButton_190.setIcon(icon5)

        self.gridLayout_185.addWidget(self.toolButton_190, 0, 2, 1, 1)

        self.gridLayout_184.addWidget(self.frame_176, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_175, 10, 0, 1, 1)

        self.frame_185 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_185.setObjectName("frame_185")
        self.frame_185.setMinimumSize(QSize(0, 200))
        self.frame_185.setMaximumSize(QSize(16777215, 200))
        self.frame_185.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.gridLayout_194 = QGridLayout(self.frame_185)
        self.gridLayout_194.setObjectName("gridLayout_194")
        self.gridLayout_194.setContentsMargins(20, 20, 20, 20)
        self.label_187 = QLabel(self.frame_185)
        self.label_187.setObjectName("label_187")
        self.label_187.setMinimumSize(QSize(70, 30))
        self.label_187.setMaximumSize(QSize(70, 30))
        self.label_187.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_187.setTextFormat(Qt.AutoText)
        self.label_187.setScaledContents(True)
        self.label_187.setAlignment(Qt.AlignCenter)
        self.label_187.setWordWrap(False)
        self.label_187.setOpenExternalLinks(False)

        self.gridLayout_194.addWidget(self.label_187, 0, 0, 1, 1)

        self.label_188 = QLabel(self.frame_185)
        self.label_188.setObjectName("label_188")

        self.gridLayout_194.addWidget(self.label_188, 0, 1, 1, 1)

        self.frame_186 = QFrame(self.frame_185)
        self.frame_186.setObjectName("frame_186")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.gridLayout_195 = QGridLayout(self.frame_186)
        self.gridLayout_195.setObjectName("gridLayout_195")
        self.gridLayout_195.setHorizontalSpacing(5)
        self.gridLayout_195.setContentsMargins(0, 0, 0, 0)
        self.toolButton_199 = QToolButton(self.frame_186)
        self.toolButton_199.setObjectName("toolButton_199")
        self.toolButton_199.setMinimumSize(QSize(50, 50))
        self.toolButton_199.setMaximumSize(QSize(50, 50))
        self.toolButton_199.setIcon(icon4)

        self.gridLayout_195.addWidget(self.toolButton_199, 0, 1, 1, 1)

        self.lineEdit_88 = QLineEdit(self.frame_186)
        self.lineEdit_88.setObjectName("lineEdit_88")
        self.lineEdit_88.setMinimumSize(QSize(0, 50))

        self.gridLayout_195.addWidget(self.lineEdit_88, 0, 0, 1, 1)

        self.toolButton_200 = QToolButton(self.frame_186)
        self.toolButton_200.setObjectName("toolButton_200")
        self.toolButton_200.setMinimumSize(QSize(50, 50))
        self.toolButton_200.setMaximumSize(QSize(50, 50))
        self.toolButton_200.setIcon(icon5)

        self.gridLayout_195.addWidget(self.toolButton_200, 0, 2, 1, 1)

        self.gridLayout_194.addWidget(self.frame_186, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_185, 3, 0, 1, 1)

        self.frame_159 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_159.setObjectName("frame_159")
        self.frame_159.setMinimumSize(QSize(0, 300))
        self.frame_159.setMaximumSize(QSize(16777215, 300))
        self.frame_159.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.gridLayout_168 = QGridLayout(self.frame_159)
        self.gridLayout_168.setObjectName("gridLayout_168")
        self.gridLayout_168.setContentsMargins(20, 20, 20, 20)
        self.label_161 = QLabel(self.frame_159)
        self.label_161.setObjectName("label_161")
        self.label_161.setMinimumSize(QSize(120, 30))
        self.label_161.setMaximumSize(QSize(120, 30))
        self.label_161.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_161.setTextFormat(Qt.AutoText)
        self.label_161.setScaledContents(True)
        self.label_161.setAlignment(Qt.AlignCenter)
        self.label_161.setWordWrap(False)
        self.label_161.setOpenExternalLinks(False)

        self.gridLayout_168.addWidget(self.label_161, 0, 0, 1, 1)

        self.label_162 = QLabel(self.frame_159)
        self.label_162.setObjectName("label_162")

        self.gridLayout_168.addWidget(self.label_162, 0, 1, 1, 1)

        self.frame_160 = QFrame(self.frame_159)
        self.frame_160.setObjectName("frame_160")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.gridLayout_169 = QGridLayout(self.frame_160)
        self.gridLayout_169.setObjectName("gridLayout_169")
        self.gridLayout_169.setHorizontalSpacing(5)
        self.gridLayout_169.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_38 = QLineEdit(self.frame_160)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_38.setMinimumSize(QSize(0, 50))

        self.gridLayout_169.addWidget(self.lineEdit_38, 1, 0, 1, 1)

        self.toolButton_175 = QToolButton(self.frame_160)
        self.toolButton_175.setObjectName("toolButton_175")
        self.toolButton_175.setMinimumSize(QSize(50, 50))
        self.toolButton_175.setMaximumSize(QSize(50, 50))
        self.toolButton_175.setIcon(icon4)

        self.gridLayout_169.addWidget(self.toolButton_175, 0, 1, 1, 1)

        self.toolButton_176 = QToolButton(self.frame_160)
        self.toolButton_176.setObjectName("toolButton_176")
        self.toolButton_176.setMinimumSize(QSize(50, 50))
        self.toolButton_176.setMaximumSize(QSize(50, 50))
        self.toolButton_176.setIcon(icon5)

        self.gridLayout_169.addWidget(self.toolButton_176, 0, 2, 1, 1)

        self.lineEdit_76 = QLineEdit(self.frame_160)
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.lineEdit_76.setMinimumSize(QSize(0, 50))

        self.gridLayout_169.addWidget(self.lineEdit_76, 0, 0, 1, 1)

        self.lineEdit_39 = QLineEdit(self.frame_160)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_39.setMinimumSize(QSize(0, 50))

        self.gridLayout_169.addWidget(self.lineEdit_39, 2, 0, 1, 1)

        self.toolButton_99 = QToolButton(self.frame_160)
        self.toolButton_99.setObjectName("toolButton_99")
        self.toolButton_99.setMinimumSize(QSize(50, 50))
        self.toolButton_99.setMaximumSize(QSize(50, 50))
        self.toolButton_99.setIcon(icon4)

        self.gridLayout_169.addWidget(self.toolButton_99, 1, 1, 1, 1)

        self.toolButton_100 = QToolButton(self.frame_160)
        self.toolButton_100.setObjectName("toolButton_100")
        self.toolButton_100.setMinimumSize(QSize(50, 50))
        self.toolButton_100.setMaximumSize(QSize(50, 50))
        self.toolButton_100.setIcon(icon4)

        self.gridLayout_169.addWidget(self.toolButton_100, 2, 1, 1, 1)

        self.toolButton_101 = QToolButton(self.frame_160)
        self.toolButton_101.setObjectName("toolButton_101")
        self.toolButton_101.setMinimumSize(QSize(50, 50))
        self.toolButton_101.setMaximumSize(QSize(50, 50))
        self.toolButton_101.setIcon(icon5)

        self.gridLayout_169.addWidget(self.toolButton_101, 1, 2, 1, 1)

        self.toolButton_102 = QToolButton(self.frame_160)
        self.toolButton_102.setObjectName("toolButton_102")
        self.toolButton_102.setMinimumSize(QSize(50, 50))
        self.toolButton_102.setMaximumSize(QSize(50, 50))
        self.toolButton_102.setIcon(icon5)

        self.gridLayout_169.addWidget(self.toolButton_102, 2, 2, 1, 1)

        self.gridLayout_168.addWidget(self.frame_160, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_159, 6, 0, 1, 1)

        self.frame_167 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_167.setObjectName("frame_167")
        self.frame_167.setMinimumSize(QSize(0, 200))
        self.frame_167.setMaximumSize(QSize(16777215, 200))
        self.frame_167.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.gridLayout_176 = QGridLayout(self.frame_167)
        self.gridLayout_176.setObjectName("gridLayout_176")
        self.gridLayout_176.setContentsMargins(20, 20, 20, 20)
        self.label_169 = QLabel(self.frame_167)
        self.label_169.setObjectName("label_169")
        self.label_169.setMinimumSize(QSize(80, 30))
        self.label_169.setMaximumSize(QSize(80, 30))
        self.label_169.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_169.setTextFormat(Qt.AutoText)
        self.label_169.setScaledContents(True)
        self.label_169.setAlignment(Qt.AlignCenter)
        self.label_169.setWordWrap(False)
        self.label_169.setOpenExternalLinks(False)

        self.gridLayout_176.addWidget(self.label_169, 0, 0, 1, 1)

        self.label_170 = QLabel(self.frame_167)
        self.label_170.setObjectName("label_170")

        self.gridLayout_176.addWidget(self.label_170, 0, 1, 1, 1)

        self.frame_168 = QFrame(self.frame_167)
        self.frame_168.setObjectName("frame_168")
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.gridLayout_177 = QGridLayout(self.frame_168)
        self.gridLayout_177.setObjectName("gridLayout_177")
        self.gridLayout_177.setHorizontalSpacing(5)
        self.gridLayout_177.setContentsMargins(0, 0, 0, 0)
        self.toolButton_181 = QToolButton(self.frame_168)
        self.toolButton_181.setObjectName("toolButton_181")
        self.toolButton_181.setMinimumSize(QSize(50, 50))
        self.toolButton_181.setMaximumSize(QSize(50, 50))
        self.toolButton_181.setIcon(icon5)

        self.gridLayout_177.addWidget(self.toolButton_181, 0, 2, 1, 1)

        self.toolButton_182 = QToolButton(self.frame_168)
        self.toolButton_182.setObjectName("toolButton_182")
        self.toolButton_182.setMinimumSize(QSize(50, 50))
        self.toolButton_182.setMaximumSize(QSize(50, 50))
        self.toolButton_182.setIcon(icon4)

        self.gridLayout_177.addWidget(self.toolButton_182, 0, 1, 1, 1)

        self.lineEdit_79 = QLineEdit(self.frame_168)
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.lineEdit_79.setMinimumSize(QSize(0, 50))

        self.gridLayout_177.addWidget(self.lineEdit_79, 0, 0, 1, 1)

        self.gridLayout_176.addWidget(self.frame_168, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_167, 13, 0, 1, 1)

        self.frame_153 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_153.setObjectName("frame_153")
        self.frame_153.setMinimumSize(QSize(0, 200))
        self.frame_153.setMaximumSize(QSize(16777215, 200))
        self.frame_153.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.gridLayout_162 = QGridLayout(self.frame_153)
        self.gridLayout_162.setObjectName("gridLayout_162")
        self.gridLayout_162.setContentsMargins(20, 20, 20, 20)
        self.label_155 = QLabel(self.frame_153)
        self.label_155.setObjectName("label_155")
        self.label_155.setMinimumSize(QSize(50, 30))
        self.label_155.setMaximumSize(QSize(50, 30))
        self.label_155.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_155.setTextFormat(Qt.AutoText)
        self.label_155.setScaledContents(True)
        self.label_155.setAlignment(Qt.AlignCenter)
        self.label_155.setWordWrap(False)
        self.label_155.setOpenExternalLinks(False)

        self.gridLayout_162.addWidget(self.label_155, 0, 0, 1, 1)

        self.label_156 = QLabel(self.frame_153)
        self.label_156.setObjectName("label_156")

        self.gridLayout_162.addWidget(self.label_156, 0, 1, 1, 1)

        self.frame_154 = QFrame(self.frame_153)
        self.frame_154.setObjectName("frame_154")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.gridLayout_163 = QGridLayout(self.frame_154)
        self.gridLayout_163.setObjectName("gridLayout_163")
        self.gridLayout_163.setHorizontalSpacing(5)
        self.gridLayout_163.setContentsMargins(0, 0, 0, 0)
        self.toolButton_171 = QToolButton(self.frame_154)
        self.toolButton_171.setObjectName("toolButton_171")
        self.toolButton_171.setMinimumSize(QSize(50, 50))
        self.toolButton_171.setMaximumSize(QSize(50, 50))
        self.toolButton_171.setIcon(icon4)

        self.gridLayout_163.addWidget(self.toolButton_171, 0, 1, 1, 1)

        self.lineEdit_74 = QLineEdit(self.frame_154)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.lineEdit_74.setMinimumSize(QSize(0, 50))

        self.gridLayout_163.addWidget(self.lineEdit_74, 0, 0, 1, 1)

        self.toolButton_172 = QToolButton(self.frame_154)
        self.toolButton_172.setObjectName("toolButton_172")
        self.toolButton_172.setMinimumSize(QSize(50, 50))
        self.toolButton_172.setMaximumSize(QSize(50, 50))
        self.toolButton_172.setIcon(icon5)

        self.gridLayout_163.addWidget(self.toolButton_172, 0, 2, 1, 1)

        self.gridLayout_162.addWidget(self.frame_154, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_153, 2, 0, 1, 1)

        self.frame_165 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_165.setObjectName("frame_165")
        self.frame_165.setMinimumSize(QSize(0, 200))
        self.frame_165.setMaximumSize(QSize(16777215, 200))
        self.frame_165.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.gridLayout_174 = QGridLayout(self.frame_165)
        self.gridLayout_174.setObjectName("gridLayout_174")
        self.gridLayout_174.setContentsMargins(20, 20, 20, 20)
        self.label_167 = QLabel(self.frame_165)
        self.label_167.setObjectName("label_167")
        self.label_167.setMinimumSize(QSize(110, 30))
        self.label_167.setMaximumSize(QSize(110, 30))
        self.label_167.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_167.setTextFormat(Qt.AutoText)
        self.label_167.setScaledContents(True)
        self.label_167.setAlignment(Qt.AlignCenter)
        self.label_167.setWordWrap(False)
        self.label_167.setOpenExternalLinks(False)

        self.gridLayout_174.addWidget(self.label_167, 0, 0, 1, 1)

        self.label_168 = QLabel(self.frame_165)
        self.label_168.setObjectName("label_168")

        self.gridLayout_174.addWidget(self.label_168, 0, 1, 1, 1)

        self.frame_166 = QFrame(self.frame_165)
        self.frame_166.setObjectName("frame_166")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.gridLayout_175 = QGridLayout(self.frame_166)
        self.gridLayout_175.setObjectName("gridLayout_175")
        self.gridLayout_175.setHorizontalSpacing(5)
        self.gridLayout_175.setContentsMargins(0, 0, 0, 0)
        self.toolButton_179 = QToolButton(self.frame_166)
        self.toolButton_179.setObjectName("toolButton_179")
        self.toolButton_179.setMinimumSize(QSize(50, 50))
        self.toolButton_179.setMaximumSize(QSize(50, 50))
        self.toolButton_179.setIcon(icon4)

        self.gridLayout_175.addWidget(self.toolButton_179, 0, 1, 1, 1)

        self.lineEdit_78 = QLineEdit(self.frame_166)
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.lineEdit_78.setMinimumSize(QSize(0, 50))

        self.gridLayout_175.addWidget(self.lineEdit_78, 0, 0, 1, 1)

        self.toolButton_180 = QToolButton(self.frame_166)
        self.toolButton_180.setObjectName("toolButton_180")
        self.toolButton_180.setMinimumSize(QSize(50, 50))
        self.toolButton_180.setMaximumSize(QSize(50, 50))
        self.toolButton_180.setIcon(icon5)

        self.gridLayout_175.addWidget(self.toolButton_180, 0, 2, 1, 1)

        self.gridLayout_174.addWidget(self.frame_166, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_165, 7, 0, 1, 1)

        self.frame_151 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_151.setObjectName("frame_151")
        self.frame_151.setMinimumSize(QSize(0, 200))
        self.frame_151.setMaximumSize(QSize(16777215, 200))
        self.frame_151.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.gridLayout_160 = QGridLayout(self.frame_151)
        self.gridLayout_160.setObjectName("gridLayout_160")
        self.gridLayout_160.setContentsMargins(20, 20, 20, 20)
        self.label_153 = QLabel(self.frame_151)
        self.label_153.setObjectName("label_153")
        self.label_153.setMinimumSize(QSize(50, 30))
        self.label_153.setMaximumSize(QSize(50, 30))
        self.label_153.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_153.setTextFormat(Qt.AutoText)
        self.label_153.setScaledContents(True)
        self.label_153.setAlignment(Qt.AlignCenter)
        self.label_153.setWordWrap(False)
        self.label_153.setOpenExternalLinks(False)

        self.gridLayout_160.addWidget(self.label_153, 0, 0, 1, 1)

        self.label_154 = QLabel(self.frame_151)
        self.label_154.setObjectName("label_154")

        self.gridLayout_160.addWidget(self.label_154, 0, 1, 1, 1)

        self.frame_152 = QFrame(self.frame_151)
        self.frame_152.setObjectName("frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.gridLayout_161 = QGridLayout(self.frame_152)
        self.gridLayout_161.setObjectName("gridLayout_161")
        self.gridLayout_161.setHorizontalSpacing(5)
        self.gridLayout_161.setContentsMargins(0, 0, 0, 0)
        self.toolButton_169 = QToolButton(self.frame_152)
        self.toolButton_169.setObjectName("toolButton_169")
        self.toolButton_169.setMinimumSize(QSize(50, 50))
        self.toolButton_169.setMaximumSize(QSize(50, 50))
        self.toolButton_169.setIcon(icon4)

        self.gridLayout_161.addWidget(self.toolButton_169, 0, 1, 1, 1)

        self.lineEdit_73 = QLineEdit(self.frame_152)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.lineEdit_73.setMinimumSize(QSize(0, 50))

        self.gridLayout_161.addWidget(self.lineEdit_73, 0, 0, 1, 1)

        self.toolButton_170 = QToolButton(self.frame_152)
        self.toolButton_170.setObjectName("toolButton_170")
        self.toolButton_170.setMinimumSize(QSize(50, 50))
        self.toolButton_170.setMaximumSize(QSize(50, 50))
        self.toolButton_170.setIcon(icon5)

        self.gridLayout_161.addWidget(self.toolButton_170, 0, 2, 1, 1)

        self.gridLayout_160.addWidget(self.frame_152, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_151, 1, 0, 1, 1)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_33.setObjectName("frame_33")
        self.frame_33.setMinimumSize(QSize(0, 200))
        self.frame_33.setMaximumSize(QSize(16777215, 200))
        self.frame_33.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_33)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.gridLayout_40.setContentsMargins(20, 20, 20, 20)
        self.label_33 = QLabel(self.frame_33)
        self.label_33.setObjectName("label_33")

        self.gridLayout_40.addWidget(self.label_33, 0, 1, 1, 1)

        self.label_34 = QLabel(self.frame_33)
        self.label_34.setObjectName("label_34")
        self.label_34.setMinimumSize(QSize(90, 30))
        self.label_34.setMaximumSize(QSize(90, 30))
        self.label_34.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_34.setTextFormat(Qt.AutoText)
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_34.setWordWrap(False)
        self.label_34.setOpenExternalLinks(False)

        self.gridLayout_40.addWidget(self.label_34, 0, 0, 1, 1)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName("frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_35)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.gridLayout_41.setHorizontalSpacing(5)
        self.gridLayout_41.setVerticalSpacing(0)
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.toolButton_41 = QToolButton(self.frame_35)
        self.toolButton_41.setObjectName("toolButton_41")
        self.toolButton_41.setMinimumSize(QSize(50, 50))
        self.toolButton_41.setMaximumSize(QSize(50, 50))
        self.toolButton_41.setIcon(icon4)

        self.gridLayout_41.addWidget(self.toolButton_41, 0, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_35)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 50))

        self.gridLayout_41.addWidget(self.lineEdit_9, 0, 0, 1, 1)

        self.toolButton_42 = QToolButton(self.frame_35)
        self.toolButton_42.setObjectName("toolButton_42")
        self.toolButton_42.setMinimumSize(QSize(50, 50))
        self.toolButton_42.setMaximumSize(QSize(50, 50))
        self.toolButton_42.setIcon(icon5)

        self.gridLayout_41.addWidget(self.toolButton_42, 0, 2, 1, 1)

        self.gridLayout_40.addWidget(self.frame_35, 1, 0, 1, 2)

        self.gridLayout_10.addWidget(self.frame_33, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_11.addWidget(self.scrollArea_3, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_13 = QGridLayout(self.tab_8)
        self.gridLayout_13.setSpacing(10)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.tab_8)
        self.frame_25.setObjectName("frame_25")
        self.frame_25.setMinimumSize(QSize(0, 60))
        self.frame_25.setMaximumSize(QSize(16777215, 60))
        self.frame_25.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_25)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_28.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_28.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.label_9 = QLabel(self.frame_25)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')

        self.gridLayout_28.addWidget(self.label_9, 0, 1, 1, 1)

        self.gridLayout_13.addWidget(self.frame_25, 0, 0, 1, 1)

        self.scrollArea_4 = QScrollArea(self.tab_8)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollArea_4.setStyleSheet(
            "	border-style: solid;\n"
            "	border-top-color: transparent;\n"
            "	border-right-color: transparent;\n"
            "	border-left-color: transparent;\n"
            "	border-bottom-color: transparent;\n"
            "	border-width: 0px;"
        )
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 958, 4020))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_12.setSpacing(10)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_12.setContentsMargins(20, 20, 20, 20)
        self.frame_177 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_177.setObjectName("frame_177")
        self.frame_177.setMinimumSize(QSize(0, 200))
        self.frame_177.setMaximumSize(QSize(16777215, 200))
        self.frame_177.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.gridLayout_186 = QGridLayout(self.frame_177)
        self.gridLayout_186.setObjectName("gridLayout_186")
        self.gridLayout_186.setContentsMargins(20, 20, 20, 20)
        self.label_179 = QLabel(self.frame_177)
        self.label_179.setObjectName("label_179")
        self.label_179.setMinimumSize(QSize(90, 30))
        self.label_179.setMaximumSize(QSize(90, 30))
        self.label_179.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_179.setTextFormat(Qt.AutoText)
        self.label_179.setScaledContents(True)
        self.label_179.setAlignment(Qt.AlignCenter)
        self.label_179.setWordWrap(False)
        self.label_179.setOpenExternalLinks(False)

        self.gridLayout_186.addWidget(self.label_179, 0, 0, 1, 1)

        self.label_180 = QLabel(self.frame_177)
        self.label_180.setObjectName("label_180")

        self.gridLayout_186.addWidget(self.label_180, 0, 1, 1, 1)

        self.frame_178 = QFrame(self.frame_177)
        self.frame_178.setObjectName("frame_178")
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.gridLayout_187 = QGridLayout(self.frame_178)
        self.gridLayout_187.setObjectName("gridLayout_187")
        self.gridLayout_187.setHorizontalSpacing(5)
        self.gridLayout_187.setContentsMargins(0, 0, 0, 0)
        self.toolButton_191 = QToolButton(self.frame_178)
        self.toolButton_191.setObjectName("toolButton_191")
        self.toolButton_191.setMinimumSize(QSize(50, 50))
        self.toolButton_191.setMaximumSize(QSize(50, 50))
        self.toolButton_191.setIcon(icon4)

        self.gridLayout_187.addWidget(self.toolButton_191, 0, 1, 1, 1)

        self.lineEdit_84 = QLineEdit(self.frame_178)
        self.lineEdit_84.setObjectName("lineEdit_84")
        self.lineEdit_84.setMinimumSize(QSize(0, 50))

        self.gridLayout_187.addWidget(self.lineEdit_84, 0, 0, 1, 1)

        self.toolButton_192 = QToolButton(self.frame_178)
        self.toolButton_192.setObjectName("toolButton_192")
        self.toolButton_192.setMinimumSize(QSize(50, 50))
        self.toolButton_192.setMaximumSize(QSize(50, 50))
        self.toolButton_192.setIcon(icon5)

        self.gridLayout_187.addWidget(self.toolButton_192, 0, 2, 1, 1)

        self.gridLayout_186.addWidget(self.frame_178, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_177, 5, 0, 1, 1)

        self.frame_195 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_195.setObjectName("frame_195")
        self.frame_195.setMinimumSize(QSize(0, 200))
        self.frame_195.setMaximumSize(QSize(16777215, 200))
        self.frame_195.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.gridLayout_204 = QGridLayout(self.frame_195)
        self.gridLayout_204.setObjectName("gridLayout_204")
        self.gridLayout_204.setContentsMargins(20, 20, 20, 20)
        self.label_197 = QLabel(self.frame_195)
        self.label_197.setObjectName("label_197")
        self.label_197.setMinimumSize(QSize(70, 30))
        self.label_197.setMaximumSize(QSize(70, 30))
        self.label_197.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_197.setTextFormat(Qt.AutoText)
        self.label_197.setScaledContents(True)
        self.label_197.setAlignment(Qt.AlignCenter)
        self.label_197.setWordWrap(False)
        self.label_197.setOpenExternalLinks(False)

        self.gridLayout_204.addWidget(self.label_197, 0, 0, 1, 1)

        self.label_198 = QLabel(self.frame_195)
        self.label_198.setObjectName("label_198")

        self.gridLayout_204.addWidget(self.label_198, 0, 1, 1, 1)

        self.frame_196 = QFrame(self.frame_195)
        self.frame_196.setObjectName("frame_196")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.gridLayout_205 = QGridLayout(self.frame_196)
        self.gridLayout_205.setObjectName("gridLayout_205")
        self.gridLayout_205.setHorizontalSpacing(5)
        self.gridLayout_205.setContentsMargins(0, 0, 0, 0)
        self.toolButton_209 = QToolButton(self.frame_196)
        self.toolButton_209.setObjectName("toolButton_209")
        self.toolButton_209.setMinimumSize(QSize(50, 50))
        self.toolButton_209.setMaximumSize(QSize(50, 50))
        self.toolButton_209.setIcon(icon5)

        self.gridLayout_205.addWidget(self.toolButton_209, 0, 2, 1, 1)

        self.toolButton_210 = QToolButton(self.frame_196)
        self.toolButton_210.setObjectName("toolButton_210")
        self.toolButton_210.setMinimumSize(QSize(50, 50))
        self.toolButton_210.setMaximumSize(QSize(50, 50))
        self.toolButton_210.setIcon(icon4)

        self.gridLayout_205.addWidget(self.toolButton_210, 0, 1, 1, 1)

        self.lineEdit_93 = QLineEdit(self.frame_196)
        self.lineEdit_93.setObjectName("lineEdit_93")
        self.lineEdit_93.setMinimumSize(QSize(0, 50))

        self.gridLayout_205.addWidget(self.lineEdit_93, 0, 0, 1, 1)

        self.gridLayout_204.addWidget(self.frame_196, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_195, 13, 0, 1, 1)

        self.frame_187 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_187.setObjectName("frame_187")
        self.frame_187.setMinimumSize(QSize(0, 200))
        self.frame_187.setMaximumSize(QSize(16777215, 200))
        self.frame_187.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.gridLayout_196 = QGridLayout(self.frame_187)
        self.gridLayout_196.setObjectName("gridLayout_196")
        self.gridLayout_196.setContentsMargins(20, 20, 20, 20)
        self.label_189 = QLabel(self.frame_187)
        self.label_189.setObjectName("label_189")
        self.label_189.setMinimumSize(QSize(50, 30))
        self.label_189.setMaximumSize(QSize(50, 30))
        self.label_189.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_189.setTextFormat(Qt.AutoText)
        self.label_189.setScaledContents(True)
        self.label_189.setAlignment(Qt.AlignCenter)
        self.label_189.setWordWrap(False)
        self.label_189.setOpenExternalLinks(False)

        self.gridLayout_196.addWidget(self.label_189, 0, 0, 1, 1)

        self.label_190 = QLabel(self.frame_187)
        self.label_190.setObjectName("label_190")

        self.gridLayout_196.addWidget(self.label_190, 0, 1, 1, 1)

        self.frame_188 = QFrame(self.frame_187)
        self.frame_188.setObjectName("frame_188")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.gridLayout_197 = QGridLayout(self.frame_188)
        self.gridLayout_197.setObjectName("gridLayout_197")
        self.gridLayout_197.setHorizontalSpacing(5)
        self.gridLayout_197.setContentsMargins(0, 0, 0, 0)
        self.toolButton_201 = QToolButton(self.frame_188)
        self.toolButton_201.setObjectName("toolButton_201")
        self.toolButton_201.setMinimumSize(QSize(50, 50))
        self.toolButton_201.setMaximumSize(QSize(50, 50))
        self.toolButton_201.setIcon(icon4)

        self.gridLayout_197.addWidget(self.toolButton_201, 0, 1, 1, 1)

        self.lineEdit_89 = QLineEdit(self.frame_188)
        self.lineEdit_89.setObjectName("lineEdit_89")
        self.lineEdit_89.setMinimumSize(QSize(0, 50))

        self.gridLayout_197.addWidget(self.lineEdit_89, 0, 0, 1, 1)

        self.toolButton_202 = QToolButton(self.frame_188)
        self.toolButton_202.setObjectName("toolButton_202")
        self.toolButton_202.setMinimumSize(QSize(50, 50))
        self.toolButton_202.setMaximumSize(QSize(50, 50))
        self.toolButton_202.setIcon(icon5)

        self.gridLayout_197.addWidget(self.toolButton_202, 0, 2, 1, 1)

        self.gridLayout_196.addWidget(self.frame_188, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_187, 6, 0, 1, 1)

        self.frame_197 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_197.setObjectName("frame_197")
        self.frame_197.setMinimumSize(QSize(0, 200))
        self.frame_197.setMaximumSize(QSize(16777215, 200))
        self.frame_197.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.gridLayout_206 = QGridLayout(self.frame_197)
        self.gridLayout_206.setObjectName("gridLayout_206")
        self.gridLayout_206.setContentsMargins(20, 20, 20, 20)
        self.label_199 = QLabel(self.frame_197)
        self.label_199.setObjectName("label_199")
        self.label_199.setMinimumSize(QSize(50, 30))
        self.label_199.setMaximumSize(QSize(50, 30))
        self.label_199.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_199.setTextFormat(Qt.AutoText)
        self.label_199.setScaledContents(True)
        self.label_199.setAlignment(Qt.AlignCenter)
        self.label_199.setWordWrap(False)
        self.label_199.setOpenExternalLinks(False)

        self.gridLayout_206.addWidget(self.label_199, 0, 0, 1, 1)

        self.label_200 = QLabel(self.frame_197)
        self.label_200.setObjectName("label_200")

        self.gridLayout_206.addWidget(self.label_200, 0, 1, 1, 1)

        self.frame_198 = QFrame(self.frame_197)
        self.frame_198.setObjectName("frame_198")
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.gridLayout_207 = QGridLayout(self.frame_198)
        self.gridLayout_207.setObjectName("gridLayout_207")
        self.gridLayout_207.setHorizontalSpacing(5)
        self.gridLayout_207.setContentsMargins(0, 0, 0, 0)
        self.toolButton_211 = QToolButton(self.frame_198)
        self.toolButton_211.setObjectName("toolButton_211")
        self.toolButton_211.setMinimumSize(QSize(50, 50))
        self.toolButton_211.setMaximumSize(QSize(50, 50))
        self.toolButton_211.setIcon(icon4)

        self.gridLayout_207.addWidget(self.toolButton_211, 0, 1, 1, 1)

        self.lineEdit_94 = QLineEdit(self.frame_198)
        self.lineEdit_94.setObjectName("lineEdit_94")
        self.lineEdit_94.setMinimumSize(QSize(0, 50))

        self.gridLayout_207.addWidget(self.lineEdit_94, 0, 0, 1, 1)

        self.toolButton_212 = QToolButton(self.frame_198)
        self.toolButton_212.setObjectName("toolButton_212")
        self.toolButton_212.setMinimumSize(QSize(50, 50))
        self.toolButton_212.setMaximumSize(QSize(50, 50))
        self.toolButton_212.setIcon(icon5)

        self.gridLayout_207.addWidget(self.toolButton_212, 0, 2, 1, 1)

        self.gridLayout_206.addWidget(self.frame_198, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_197, 18, 0, 1, 1)

        self.frame_203 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_203.setObjectName("frame_203")
        self.frame_203.setMinimumSize(QSize(0, 200))
        self.frame_203.setMaximumSize(QSize(16777215, 200))
        self.frame_203.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_203.setFrameShape(QFrame.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Raised)
        self.gridLayout_212 = QGridLayout(self.frame_203)
        self.gridLayout_212.setObjectName("gridLayout_212")
        self.gridLayout_212.setContentsMargins(20, 20, 20, 20)
        self.label_205 = QLabel(self.frame_203)
        self.label_205.setObjectName("label_205")
        self.label_205.setMinimumSize(QSize(60, 30))
        self.label_205.setMaximumSize(QSize(60, 30))
        self.label_205.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_205.setTextFormat(Qt.AutoText)
        self.label_205.setScaledContents(True)
        self.label_205.setAlignment(Qt.AlignCenter)
        self.label_205.setWordWrap(False)
        self.label_205.setOpenExternalLinks(False)

        self.gridLayout_212.addWidget(self.label_205, 0, 0, 1, 1)

        self.label_206 = QLabel(self.frame_203)
        self.label_206.setObjectName("label_206")

        self.gridLayout_212.addWidget(self.label_206, 0, 1, 1, 1)

        self.frame_204 = QFrame(self.frame_203)
        self.frame_204.setObjectName("frame_204")
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.gridLayout_213 = QGridLayout(self.frame_204)
        self.gridLayout_213.setObjectName("gridLayout_213")
        self.gridLayout_213.setHorizontalSpacing(5)
        self.gridLayout_213.setContentsMargins(0, 0, 0, 0)
        self.toolButton_217 = QToolButton(self.frame_204)
        self.toolButton_217.setObjectName("toolButton_217")
        self.toolButton_217.setMinimumSize(QSize(50, 50))
        self.toolButton_217.setMaximumSize(QSize(50, 50))
        self.toolButton_217.setIcon(icon4)

        self.gridLayout_213.addWidget(self.toolButton_217, 0, 1, 1, 1)

        self.lineEdit_97 = QLineEdit(self.frame_204)
        self.lineEdit_97.setObjectName("lineEdit_97")
        self.lineEdit_97.setMinimumSize(QSize(0, 50))

        self.gridLayout_213.addWidget(self.lineEdit_97, 0, 0, 1, 1)

        self.toolButton_218 = QToolButton(self.frame_204)
        self.toolButton_218.setObjectName("toolButton_218")
        self.toolButton_218.setMinimumSize(QSize(50, 50))
        self.toolButton_218.setMaximumSize(QSize(50, 50))
        self.toolButton_218.setIcon(icon5)

        self.gridLayout_213.addWidget(self.toolButton_218, 0, 2, 1, 1)

        self.gridLayout_212.addWidget(self.frame_204, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_203, 10, 0, 1, 1)

        self.frame_161 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_161.setObjectName("frame_161")
        self.frame_161.setMinimumSize(QSize(0, 200))
        self.frame_161.setMaximumSize(QSize(16777215, 200))
        self.frame_161.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.gridLayout_170 = QGridLayout(self.frame_161)
        self.gridLayout_170.setObjectName("gridLayout_170")
        self.gridLayout_170.setContentsMargins(20, 20, 20, 20)
        self.label_163 = QLabel(self.frame_161)
        self.label_163.setObjectName("label_163")
        self.label_163.setMinimumSize(QSize(100, 30))
        self.label_163.setMaximumSize(QSize(100, 30))
        self.label_163.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_163.setTextFormat(Qt.AutoText)
        self.label_163.setScaledContents(True)
        self.label_163.setAlignment(Qt.AlignCenter)
        self.label_163.setWordWrap(False)
        self.label_163.setOpenExternalLinks(False)

        self.gridLayout_170.addWidget(self.label_163, 0, 0, 1, 1)

        self.label_164 = QLabel(self.frame_161)
        self.label_164.setObjectName("label_164")

        self.gridLayout_170.addWidget(self.label_164, 0, 1, 1, 1)

        self.frame_162 = QFrame(self.frame_161)
        self.frame_162.setObjectName("frame_162")
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.gridLayout_171 = QGridLayout(self.frame_162)
        self.gridLayout_171.setObjectName("gridLayout_171")
        self.gridLayout_171.setHorizontalSpacing(5)
        self.gridLayout_171.setContentsMargins(0, 0, 0, 0)
        self.toolButton_177 = QToolButton(self.frame_162)
        self.toolButton_177.setObjectName("toolButton_177")
        self.toolButton_177.setMinimumSize(QSize(50, 50))
        self.toolButton_177.setMaximumSize(QSize(50, 50))
        self.toolButton_177.setIcon(icon4)

        self.gridLayout_171.addWidget(self.toolButton_177, 0, 1, 1, 1)

        self.lineEdit_77 = QLineEdit(self.frame_162)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.lineEdit_77.setMinimumSize(QSize(0, 50))

        self.gridLayout_171.addWidget(self.lineEdit_77, 0, 0, 1, 1)

        self.toolButton_178 = QToolButton(self.frame_162)
        self.toolButton_178.setObjectName("toolButton_178")
        self.toolButton_178.setMinimumSize(QSize(50, 50))
        self.toolButton_178.setMaximumSize(QSize(50, 50))
        self.toolButton_178.setIcon(icon5)

        self.gridLayout_171.addWidget(self.toolButton_178, 0, 2, 1, 1)

        self.gridLayout_170.addWidget(self.frame_162, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_161, 1, 0, 1, 1)

        self.frame_163 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_163.setObjectName("frame_163")
        self.frame_163.setMinimumSize(QSize(0, 200))
        self.frame_163.setMaximumSize(QSize(16777215, 200))
        self.frame_163.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.gridLayout_172 = QGridLayout(self.frame_163)
        self.gridLayout_172.setObjectName("gridLayout_172")
        self.gridLayout_172.setContentsMargins(20, 20, 20, 20)
        self.label_165 = QLabel(self.frame_163)
        self.label_165.setObjectName("label_165")
        self.label_165.setMinimumSize(QSize(100, 30))
        self.label_165.setMaximumSize(QSize(100, 30))
        self.label_165.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_165.setTextFormat(Qt.AutoText)
        self.label_165.setScaledContents(True)
        self.label_165.setAlignment(Qt.AlignCenter)
        self.label_165.setWordWrap(False)
        self.label_165.setOpenExternalLinks(False)

        self.gridLayout_172.addWidget(self.label_165, 0, 0, 1, 1)

        self.label_166 = QLabel(self.frame_163)
        self.label_166.setObjectName("label_166")

        self.gridLayout_172.addWidget(self.label_166, 0, 1, 1, 1)

        self.frame_164 = QFrame(self.frame_163)
        self.frame_164.setObjectName("frame_164")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.gridLayout_173 = QGridLayout(self.frame_164)
        self.gridLayout_173.setObjectName("gridLayout_173")
        self.gridLayout_173.setHorizontalSpacing(5)
        self.gridLayout_173.setContentsMargins(0, 0, 0, 0)
        self.toolButton_183 = QToolButton(self.frame_164)
        self.toolButton_183.setObjectName("toolButton_183")
        self.toolButton_183.setMinimumSize(QSize(50, 50))
        self.toolButton_183.setMaximumSize(QSize(50, 50))
        self.toolButton_183.setIcon(icon4)

        self.gridLayout_173.addWidget(self.toolButton_183, 0, 1, 1, 1)

        self.lineEdit_80 = QLineEdit(self.frame_164)
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.lineEdit_80.setMinimumSize(QSize(0, 50))

        self.gridLayout_173.addWidget(self.lineEdit_80, 0, 0, 1, 1)

        self.toolButton_184 = QToolButton(self.frame_164)
        self.toolButton_184.setObjectName("toolButton_184")
        self.toolButton_184.setMinimumSize(QSize(50, 50))
        self.toolButton_184.setMaximumSize(QSize(50, 50))
        self.toolButton_184.setIcon(icon5)

        self.gridLayout_173.addWidget(self.toolButton_184, 0, 2, 1, 1)

        self.gridLayout_172.addWidget(self.frame_164, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_163, 2, 0, 1, 1)

        self.frame_36 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_36.setObjectName("frame_36")
        self.frame_36.setMinimumSize(QSize(0, 200))
        self.frame_36.setMaximumSize(QSize(16777215, 200))
        self.frame_36.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_36)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.gridLayout_42.setContentsMargins(20, 20, 20, 20)
        self.label_35 = QLabel(self.frame_36)
        self.label_35.setObjectName("label_35")

        self.gridLayout_42.addWidget(self.label_35, 0, 1, 1, 1)

        self.label_36 = QLabel(self.frame_36)
        self.label_36.setObjectName("label_36")
        self.label_36.setMinimumSize(QSize(90, 30))
        self.label_36.setMaximumSize(QSize(90, 30))
        self.label_36.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_36.setTextFormat(Qt.AutoText)
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_36.setWordWrap(False)
        self.label_36.setOpenExternalLinks(False)

        self.gridLayout_42.addWidget(self.label_36, 0, 0, 1, 1)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName("frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_37)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.gridLayout_43.setHorizontalSpacing(5)
        self.gridLayout_43.setVerticalSpacing(0)
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.toolButton_43 = QToolButton(self.frame_37)
        self.toolButton_43.setObjectName("toolButton_43")
        self.toolButton_43.setMinimumSize(QSize(50, 50))
        self.toolButton_43.setMaximumSize(QSize(50, 50))
        self.toolButton_43.setIcon(icon4)

        self.gridLayout_43.addWidget(self.toolButton_43, 0, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_37)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 50))

        self.gridLayout_43.addWidget(self.lineEdit_10, 0, 0, 1, 1)

        self.toolButton_44 = QToolButton(self.frame_37)
        self.toolButton_44.setObjectName("toolButton_44")
        self.toolButton_44.setMinimumSize(QSize(50, 50))
        self.toolButton_44.setMaximumSize(QSize(50, 50))
        self.toolButton_44.setIcon(icon5)

        self.gridLayout_43.addWidget(self.toolButton_44, 0, 2, 1, 1)

        self.gridLayout_42.addWidget(self.frame_37, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_36, 0, 0, 1, 1)

        self.frame_209 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_209.setObjectName("frame_209")
        self.frame_209.setMinimumSize(QSize(0, 200))
        self.frame_209.setMaximumSize(QSize(16777215, 200))
        self.frame_209.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_209.setFrameShape(QFrame.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Raised)
        self.gridLayout_218 = QGridLayout(self.frame_209)
        self.gridLayout_218.setObjectName("gridLayout_218")
        self.gridLayout_218.setContentsMargins(20, 20, 20, 20)
        self.label_211 = QLabel(self.frame_209)
        self.label_211.setObjectName("label_211")
        self.label_211.setMinimumSize(QSize(50, 30))
        self.label_211.setMaximumSize(QSize(50, 30))
        self.label_211.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_211.setTextFormat(Qt.AutoText)
        self.label_211.setScaledContents(True)
        self.label_211.setAlignment(Qt.AlignCenter)
        self.label_211.setWordWrap(False)
        self.label_211.setOpenExternalLinks(False)

        self.gridLayout_218.addWidget(self.label_211, 0, 0, 1, 1)

        self.label_212 = QLabel(self.frame_209)
        self.label_212.setObjectName("label_212")

        self.gridLayout_218.addWidget(self.label_212, 0, 1, 1, 1)

        self.frame_210 = QFrame(self.frame_209)
        self.frame_210.setObjectName("frame_210")
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self.gridLayout_219 = QGridLayout(self.frame_210)
        self.gridLayout_219.setObjectName("gridLayout_219")
        self.gridLayout_219.setHorizontalSpacing(5)
        self.gridLayout_219.setContentsMargins(0, 0, 0, 0)
        self.toolButton_223 = QToolButton(self.frame_210)
        self.toolButton_223.setObjectName("toolButton_223")
        self.toolButton_223.setMinimumSize(QSize(50, 50))
        self.toolButton_223.setMaximumSize(QSize(50, 50))
        self.toolButton_223.setIcon(icon4)

        self.gridLayout_219.addWidget(self.toolButton_223, 0, 1, 1, 1)

        self.lineEdit_100 = QLineEdit(self.frame_210)
        self.lineEdit_100.setObjectName("lineEdit_100")
        self.lineEdit_100.setMinimumSize(QSize(0, 50))

        self.gridLayout_219.addWidget(self.lineEdit_100, 0, 0, 1, 1)

        self.toolButton_224 = QToolButton(self.frame_210)
        self.toolButton_224.setObjectName("toolButton_224")
        self.toolButton_224.setMinimumSize(QSize(50, 50))
        self.toolButton_224.setMaximumSize(QSize(50, 50))
        self.toolButton_224.setIcon(icon5)

        self.gridLayout_219.addWidget(self.toolButton_224, 0, 2, 1, 1)

        self.gridLayout_218.addWidget(self.frame_210, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_209, 11, 0, 1, 1)

        self.frame_207 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_207.setObjectName("frame_207")
        self.frame_207.setMinimumSize(QSize(0, 200))
        self.frame_207.setMaximumSize(QSize(16777215, 200))
        self.frame_207.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.gridLayout_216 = QGridLayout(self.frame_207)
        self.gridLayout_216.setObjectName("gridLayout_216")
        self.gridLayout_216.setContentsMargins(20, 20, 20, 20)
        self.label_209 = QLabel(self.frame_207)
        self.label_209.setObjectName("label_209")
        self.label_209.setMinimumSize(QSize(100, 30))
        self.label_209.setMaximumSize(QSize(100, 30))
        self.label_209.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_209.setTextFormat(Qt.AutoText)
        self.label_209.setScaledContents(True)
        self.label_209.setAlignment(Qt.AlignCenter)
        self.label_209.setWordWrap(False)
        self.label_209.setOpenExternalLinks(False)

        self.gridLayout_216.addWidget(self.label_209, 0, 0, 1, 1)

        self.label_210 = QLabel(self.frame_207)
        self.label_210.setObjectName("label_210")

        self.gridLayout_216.addWidget(self.label_210, 0, 1, 1, 1)

        self.frame_208 = QFrame(self.frame_207)
        self.frame_208.setObjectName("frame_208")
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.gridLayout_217 = QGridLayout(self.frame_208)
        self.gridLayout_217.setObjectName("gridLayout_217")
        self.gridLayout_217.setHorizontalSpacing(5)
        self.gridLayout_217.setContentsMargins(0, 0, 0, 0)
        self.toolButton_221 = QToolButton(self.frame_208)
        self.toolButton_221.setObjectName("toolButton_221")
        self.toolButton_221.setMinimumSize(QSize(50, 50))
        self.toolButton_221.setMaximumSize(QSize(50, 50))
        self.toolButton_221.setIcon(icon4)

        self.gridLayout_217.addWidget(self.toolButton_221, 0, 1, 1, 1)

        self.lineEdit_99 = QLineEdit(self.frame_208)
        self.lineEdit_99.setObjectName("lineEdit_99")
        self.lineEdit_99.setMinimumSize(QSize(0, 50))

        self.gridLayout_217.addWidget(self.lineEdit_99, 0, 0, 1, 1)

        self.toolButton_222 = QToolButton(self.frame_208)
        self.toolButton_222.setObjectName("toolButton_222")
        self.toolButton_222.setMinimumSize(QSize(50, 50))
        self.toolButton_222.setMaximumSize(QSize(50, 50))
        self.toolButton_222.setIcon(icon5)

        self.gridLayout_217.addWidget(self.toolButton_222, 0, 2, 1, 1)

        self.gridLayout_216.addWidget(self.frame_208, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_207, 9, 0, 1, 1)

        self.frame_189 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_189.setObjectName("frame_189")
        self.frame_189.setMinimumSize(QSize(0, 200))
        self.frame_189.setMaximumSize(QSize(16777215, 200))
        self.frame_189.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.gridLayout_198 = QGridLayout(self.frame_189)
        self.gridLayout_198.setObjectName("gridLayout_198")
        self.gridLayout_198.setContentsMargins(20, 20, 20, 20)
        self.label_191 = QLabel(self.frame_189)
        self.label_191.setObjectName("label_191")
        self.label_191.setMinimumSize(QSize(110, 30))
        self.label_191.setMaximumSize(QSize(110, 30))
        self.label_191.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_191.setTextFormat(Qt.AutoText)
        self.label_191.setScaledContents(True)
        self.label_191.setAlignment(Qt.AlignCenter)
        self.label_191.setWordWrap(False)
        self.label_191.setOpenExternalLinks(False)

        self.gridLayout_198.addWidget(self.label_191, 0, 0, 1, 1)

        self.label_192 = QLabel(self.frame_189)
        self.label_192.setObjectName("label_192")

        self.gridLayout_198.addWidget(self.label_192, 0, 1, 1, 1)

        self.frame_190 = QFrame(self.frame_189)
        self.frame_190.setObjectName("frame_190")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.gridLayout_199 = QGridLayout(self.frame_190)
        self.gridLayout_199.setObjectName("gridLayout_199")
        self.gridLayout_199.setHorizontalSpacing(5)
        self.gridLayout_199.setContentsMargins(0, 0, 0, 0)
        self.toolButton_203 = QToolButton(self.frame_190)
        self.toolButton_203.setObjectName("toolButton_203")
        self.toolButton_203.setMinimumSize(QSize(50, 50))
        self.toolButton_203.setMaximumSize(QSize(50, 50))
        self.toolButton_203.setIcon(icon4)

        self.gridLayout_199.addWidget(self.toolButton_203, 0, 1, 1, 1)

        self.lineEdit_90 = QLineEdit(self.frame_190)
        self.lineEdit_90.setObjectName("lineEdit_90")
        self.lineEdit_90.setMinimumSize(QSize(0, 50))

        self.gridLayout_199.addWidget(self.lineEdit_90, 0, 0, 1, 1)

        self.toolButton_204 = QToolButton(self.frame_190)
        self.toolButton_204.setObjectName("toolButton_204")
        self.toolButton_204.setMinimumSize(QSize(50, 50))
        self.toolButton_204.setMaximumSize(QSize(50, 50))
        self.toolButton_204.setIcon(icon5)

        self.gridLayout_199.addWidget(self.toolButton_204, 0, 2, 1, 1)

        self.gridLayout_198.addWidget(self.frame_190, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_189, 16, 0, 1, 1)

        self.frame_201 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_201.setObjectName("frame_201")
        self.frame_201.setMinimumSize(QSize(0, 200))
        self.frame_201.setMaximumSize(QSize(16777215, 200))
        self.frame_201.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.gridLayout_210 = QGridLayout(self.frame_201)
        self.gridLayout_210.setObjectName("gridLayout_210")
        self.gridLayout_210.setContentsMargins(20, 20, 20, 20)
        self.label_203 = QLabel(self.frame_201)
        self.label_203.setObjectName("label_203")
        self.label_203.setMinimumSize(QSize(80, 30))
        self.label_203.setMaximumSize(QSize(80, 30))
        self.label_203.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_203.setTextFormat(Qt.AutoText)
        self.label_203.setScaledContents(True)
        self.label_203.setAlignment(Qt.AlignCenter)
        self.label_203.setWordWrap(False)
        self.label_203.setOpenExternalLinks(False)

        self.gridLayout_210.addWidget(self.label_203, 0, 0, 1, 1)

        self.label_204 = QLabel(self.frame_201)
        self.label_204.setObjectName("label_204")

        self.gridLayout_210.addWidget(self.label_204, 0, 1, 1, 1)

        self.frame_202 = QFrame(self.frame_201)
        self.frame_202.setObjectName("frame_202")
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)
        self.gridLayout_211 = QGridLayout(self.frame_202)
        self.gridLayout_211.setObjectName("gridLayout_211")
        self.gridLayout_211.setHorizontalSpacing(5)
        self.gridLayout_211.setContentsMargins(0, 0, 0, 0)
        self.toolButton_215 = QToolButton(self.frame_202)
        self.toolButton_215.setObjectName("toolButton_215")
        self.toolButton_215.setMinimumSize(QSize(50, 50))
        self.toolButton_215.setMaximumSize(QSize(50, 50))
        self.toolButton_215.setIcon(icon4)

        self.gridLayout_211.addWidget(self.toolButton_215, 0, 1, 1, 1)

        self.lineEdit_96 = QLineEdit(self.frame_202)
        self.lineEdit_96.setObjectName("lineEdit_96")
        self.lineEdit_96.setMinimumSize(QSize(0, 50))

        self.gridLayout_211.addWidget(self.lineEdit_96, 0, 0, 1, 1)

        self.toolButton_216 = QToolButton(self.frame_202)
        self.toolButton_216.setObjectName("toolButton_216")
        self.toolButton_216.setMinimumSize(QSize(50, 50))
        self.toolButton_216.setMaximumSize(QSize(50, 50))
        self.toolButton_216.setIcon(icon5)

        self.gridLayout_211.addWidget(self.toolButton_216, 0, 2, 1, 1)

        self.gridLayout_210.addWidget(self.frame_202, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_201, 14, 0, 1, 1)

        self.frame_193 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_193.setObjectName("frame_193")
        self.frame_193.setMinimumSize(QSize(0, 200))
        self.frame_193.setMaximumSize(QSize(16777215, 200))
        self.frame_193.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.gridLayout_202 = QGridLayout(self.frame_193)
        self.gridLayout_202.setObjectName("gridLayout_202")
        self.gridLayout_202.setContentsMargins(20, 20, 20, 20)
        self.label_195 = QLabel(self.frame_193)
        self.label_195.setObjectName("label_195")
        self.label_195.setMinimumSize(QSize(50, 30))
        self.label_195.setMaximumSize(QSize(50, 30))
        self.label_195.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_195.setTextFormat(Qt.AutoText)
        self.label_195.setScaledContents(True)
        self.label_195.setAlignment(Qt.AlignCenter)
        self.label_195.setWordWrap(False)
        self.label_195.setOpenExternalLinks(False)

        self.gridLayout_202.addWidget(self.label_195, 0, 0, 1, 1)

        self.label_196 = QLabel(self.frame_193)
        self.label_196.setObjectName("label_196")

        self.gridLayout_202.addWidget(self.label_196, 0, 1, 1, 1)

        self.frame_194 = QFrame(self.frame_193)
        self.frame_194.setObjectName("frame_194")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.gridLayout_203 = QGridLayout(self.frame_194)
        self.gridLayout_203.setObjectName("gridLayout_203")
        self.gridLayout_203.setHorizontalSpacing(5)
        self.gridLayout_203.setContentsMargins(0, 0, 0, 0)
        self.toolButton_207 = QToolButton(self.frame_194)
        self.toolButton_207.setObjectName("toolButton_207")
        self.toolButton_207.setMinimumSize(QSize(50, 50))
        self.toolButton_207.setMaximumSize(QSize(50, 50))
        self.toolButton_207.setIcon(icon4)

        self.gridLayout_203.addWidget(self.toolButton_207, 0, 1, 1, 1)

        self.lineEdit_92 = QLineEdit(self.frame_194)
        self.lineEdit_92.setObjectName("lineEdit_92")
        self.lineEdit_92.setMinimumSize(QSize(0, 50))

        self.gridLayout_203.addWidget(self.lineEdit_92, 0, 0, 1, 1)

        self.toolButton_208 = QToolButton(self.frame_194)
        self.toolButton_208.setObjectName("toolButton_208")
        self.toolButton_208.setMinimumSize(QSize(50, 50))
        self.toolButton_208.setMaximumSize(QSize(50, 50))
        self.toolButton_208.setIcon(icon5)

        self.gridLayout_203.addWidget(self.toolButton_208, 0, 2, 1, 1)

        self.gridLayout_202.addWidget(self.frame_194, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_193, 7, 0, 1, 1)

        self.frame_169 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_169.setObjectName("frame_169")
        self.frame_169.setMinimumSize(QSize(0, 200))
        self.frame_169.setMaximumSize(QSize(16777215, 200))
        self.frame_169.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.gridLayout_178 = QGridLayout(self.frame_169)
        self.gridLayout_178.setObjectName("gridLayout_178")
        self.gridLayout_178.setContentsMargins(20, 20, 20, 20)
        self.label_171 = QLabel(self.frame_169)
        self.label_171.setObjectName("label_171")
        self.label_171.setMinimumSize(QSize(90, 30))
        self.label_171.setMaximumSize(QSize(90, 30))
        self.label_171.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_171.setTextFormat(Qt.AutoText)
        self.label_171.setScaledContents(True)
        self.label_171.setAlignment(Qt.AlignCenter)
        self.label_171.setWordWrap(False)
        self.label_171.setOpenExternalLinks(False)

        self.gridLayout_178.addWidget(self.label_171, 0, 0, 1, 1)

        self.label_172 = QLabel(self.frame_169)
        self.label_172.setObjectName("label_172")

        self.gridLayout_178.addWidget(self.label_172, 0, 1, 1, 1)

        self.frame_170 = QFrame(self.frame_169)
        self.frame_170.setObjectName("frame_170")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.gridLayout_179 = QGridLayout(self.frame_170)
        self.gridLayout_179.setObjectName("gridLayout_179")
        self.gridLayout_179.setHorizontalSpacing(5)
        self.gridLayout_179.setContentsMargins(0, 0, 0, 0)
        self.toolButton_185 = QToolButton(self.frame_170)
        self.toolButton_185.setObjectName("toolButton_185")
        self.toolButton_185.setMinimumSize(QSize(50, 50))
        self.toolButton_185.setMaximumSize(QSize(50, 50))
        self.toolButton_185.setIcon(icon4)

        self.gridLayout_179.addWidget(self.toolButton_185, 0, 1, 1, 1)

        self.lineEdit_81 = QLineEdit(self.frame_170)
        self.lineEdit_81.setObjectName("lineEdit_81")
        self.lineEdit_81.setMinimumSize(QSize(0, 50))

        self.gridLayout_179.addWidget(self.lineEdit_81, 0, 0, 1, 1)

        self.toolButton_186 = QToolButton(self.frame_170)
        self.toolButton_186.setObjectName("toolButton_186")
        self.toolButton_186.setMinimumSize(QSize(50, 50))
        self.toolButton_186.setMaximumSize(QSize(50, 50))
        self.toolButton_186.setIcon(icon5)

        self.gridLayout_179.addWidget(self.toolButton_186, 0, 2, 1, 1)

        self.gridLayout_178.addWidget(self.frame_170, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_169, 12, 0, 1, 1)

        self.frame_171 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_171.setObjectName("frame_171")
        self.frame_171.setMinimumSize(QSize(0, 200))
        self.frame_171.setMaximumSize(QSize(16777215, 200))
        self.frame_171.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.gridLayout_180 = QGridLayout(self.frame_171)
        self.gridLayout_180.setObjectName("gridLayout_180")
        self.gridLayout_180.setContentsMargins(20, 20, 20, 20)
        self.label_173 = QLabel(self.frame_171)
        self.label_173.setObjectName("label_173")
        self.label_173.setMinimumSize(QSize(100, 30))
        self.label_173.setMaximumSize(QSize(100, 30))
        self.label_173.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_173.setTextFormat(Qt.AutoText)
        self.label_173.setScaledContents(True)
        self.label_173.setAlignment(Qt.AlignCenter)
        self.label_173.setWordWrap(False)
        self.label_173.setOpenExternalLinks(False)

        self.gridLayout_180.addWidget(self.label_173, 0, 0, 1, 1)

        self.label_174 = QLabel(self.frame_171)
        self.label_174.setObjectName("label_174")

        self.gridLayout_180.addWidget(self.label_174, 0, 1, 1, 1)

        self.frame_172 = QFrame(self.frame_171)
        self.frame_172.setObjectName("frame_172")
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.gridLayout_181 = QGridLayout(self.frame_172)
        self.gridLayout_181.setObjectName("gridLayout_181")
        self.gridLayout_181.setHorizontalSpacing(5)
        self.gridLayout_181.setContentsMargins(0, 0, 0, 0)
        self.toolButton_141 = QToolButton(self.frame_172)
        self.toolButton_141.setObjectName("toolButton_141")
        self.toolButton_141.setMinimumSize(QSize(50, 50))
        self.toolButton_141.setMaximumSize(QSize(50, 50))
        self.toolButton_141.setIcon(icon4)

        self.gridLayout_181.addWidget(self.toolButton_141, 0, 1, 1, 1)

        self.lineEdit_59 = QLineEdit(self.frame_172)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.lineEdit_59.setMinimumSize(QSize(0, 50))

        self.gridLayout_181.addWidget(self.lineEdit_59, 0, 0, 1, 1)

        self.toolButton_142 = QToolButton(self.frame_172)
        self.toolButton_142.setObjectName("toolButton_142")
        self.toolButton_142.setMinimumSize(QSize(50, 50))
        self.toolButton_142.setMaximumSize(QSize(50, 50))
        self.toolButton_142.setIcon(icon5)

        self.gridLayout_181.addWidget(self.toolButton_142, 0, 2, 1, 1)

        self.gridLayout_180.addWidget(self.frame_172, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_171, 4, 0, 1, 1)

        self.frame_211 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_211.setObjectName("frame_211")
        self.frame_211.setMinimumSize(QSize(0, 200))
        self.frame_211.setMaximumSize(QSize(16777215, 200))
        self.frame_211.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.gridLayout_220 = QGridLayout(self.frame_211)
        self.gridLayout_220.setObjectName("gridLayout_220")
        self.gridLayout_220.setContentsMargins(20, 20, 20, 20)
        self.label_213 = QLabel(self.frame_211)
        self.label_213.setObjectName("label_213")
        self.label_213.setMinimumSize(QSize(50, 30))
        self.label_213.setMaximumSize(QSize(50, 30))
        self.label_213.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_213.setTextFormat(Qt.AutoText)
        self.label_213.setScaledContents(True)
        self.label_213.setAlignment(Qt.AlignCenter)
        self.label_213.setWordWrap(False)
        self.label_213.setOpenExternalLinks(False)

        self.gridLayout_220.addWidget(self.label_213, 0, 0, 1, 1)

        self.label_214 = QLabel(self.frame_211)
        self.label_214.setObjectName("label_214")

        self.gridLayout_220.addWidget(self.label_214, 0, 1, 1, 1)

        self.frame_212 = QFrame(self.frame_211)
        self.frame_212.setObjectName("frame_212")
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)
        self.gridLayout_221 = QGridLayout(self.frame_212)
        self.gridLayout_221.setObjectName("gridLayout_221")
        self.gridLayout_221.setHorizontalSpacing(5)
        self.gridLayout_221.setContentsMargins(0, 0, 0, 0)
        self.toolButton_225 = QToolButton(self.frame_212)
        self.toolButton_225.setObjectName("toolButton_225")
        self.toolButton_225.setMinimumSize(QSize(50, 50))
        self.toolButton_225.setMaximumSize(QSize(50, 50))
        self.toolButton_225.setIcon(icon4)

        self.gridLayout_221.addWidget(self.toolButton_225, 0, 1, 1, 1)

        self.lineEdit_101 = QLineEdit(self.frame_212)
        self.lineEdit_101.setObjectName("lineEdit_101")
        self.lineEdit_101.setMinimumSize(QSize(0, 50))

        self.gridLayout_221.addWidget(self.lineEdit_101, 0, 0, 1, 1)

        self.toolButton_226 = QToolButton(self.frame_212)
        self.toolButton_226.setObjectName("toolButton_226")
        self.toolButton_226.setMinimumSize(QSize(50, 50))
        self.toolButton_226.setMaximumSize(QSize(50, 50))
        self.toolButton_226.setIcon(icon5)

        self.gridLayout_221.addWidget(self.toolButton_226, 0, 2, 1, 1)

        self.gridLayout_220.addWidget(self.frame_212, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_211, 8, 0, 1, 1)

        self.frame_213 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_213.setObjectName("frame_213")
        self.frame_213.setMinimumSize(QSize(0, 200))
        self.frame_213.setMaximumSize(QSize(16777215, 200))
        self.frame_213.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.gridLayout_222 = QGridLayout(self.frame_213)
        self.gridLayout_222.setObjectName("gridLayout_222")
        self.gridLayout_222.setContentsMargins(20, 20, 20, 20)
        self.label_215 = QLabel(self.frame_213)
        self.label_215.setObjectName("label_215")
        self.label_215.setMinimumSize(QSize(110, 30))
        self.label_215.setMaximumSize(QSize(110, 30))
        self.label_215.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_215.setTextFormat(Qt.AutoText)
        self.label_215.setScaledContents(True)
        self.label_215.setAlignment(Qt.AlignCenter)
        self.label_215.setWordWrap(False)
        self.label_215.setOpenExternalLinks(False)

        self.gridLayout_222.addWidget(self.label_215, 0, 0, 1, 1)

        self.label_216 = QLabel(self.frame_213)
        self.label_216.setObjectName("label_216")

        self.gridLayout_222.addWidget(self.label_216, 0, 1, 1, 1)

        self.frame_214 = QFrame(self.frame_213)
        self.frame_214.setObjectName("frame_214")
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.gridLayout_223 = QGridLayout(self.frame_214)
        self.gridLayout_223.setObjectName("gridLayout_223")
        self.gridLayout_223.setHorizontalSpacing(5)
        self.gridLayout_223.setContentsMargins(0, 0, 0, 0)
        self.toolButton_227 = QToolButton(self.frame_214)
        self.toolButton_227.setObjectName("toolButton_227")
        self.toolButton_227.setMinimumSize(QSize(50, 50))
        self.toolButton_227.setMaximumSize(QSize(50, 50))
        self.toolButton_227.setIcon(icon4)

        self.gridLayout_223.addWidget(self.toolButton_227, 0, 1, 1, 1)

        self.lineEdit_102 = QLineEdit(self.frame_214)
        self.lineEdit_102.setObjectName("lineEdit_102")
        self.lineEdit_102.setMinimumSize(QSize(0, 50))

        self.gridLayout_223.addWidget(self.lineEdit_102, 0, 0, 1, 1)

        self.toolButton_228 = QToolButton(self.frame_214)
        self.toolButton_228.setObjectName("toolButton_228")
        self.toolButton_228.setMinimumSize(QSize(50, 50))
        self.toolButton_228.setMaximumSize(QSize(50, 50))
        self.toolButton_228.setIcon(icon5)

        self.gridLayout_223.addWidget(self.toolButton_228, 0, 2, 1, 1)

        self.gridLayout_222.addWidget(self.frame_214, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_213, 3, 0, 1, 1)

        self.frame_199 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_199.setObjectName("frame_199")
        self.frame_199.setMinimumSize(QSize(0, 200))
        self.frame_199.setMaximumSize(QSize(16777215, 200))
        self.frame_199.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.gridLayout_208 = QGridLayout(self.frame_199)
        self.gridLayout_208.setObjectName("gridLayout_208")
        self.gridLayout_208.setContentsMargins(20, 20, 20, 20)
        self.label_201 = QLabel(self.frame_199)
        self.label_201.setObjectName("label_201")
        self.label_201.setMinimumSize(QSize(110, 30))
        self.label_201.setMaximumSize(QSize(110, 30))
        self.label_201.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_201.setTextFormat(Qt.AutoText)
        self.label_201.setScaledContents(True)
        self.label_201.setAlignment(Qt.AlignCenter)
        self.label_201.setWordWrap(False)
        self.label_201.setOpenExternalLinks(False)

        self.gridLayout_208.addWidget(self.label_201, 0, 0, 1, 1)

        self.label_202 = QLabel(self.frame_199)
        self.label_202.setObjectName("label_202")

        self.gridLayout_208.addWidget(self.label_202, 0, 1, 1, 1)

        self.frame_200 = QFrame(self.frame_199)
        self.frame_200.setObjectName("frame_200")
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.gridLayout_209 = QGridLayout(self.frame_200)
        self.gridLayout_209.setObjectName("gridLayout_209")
        self.gridLayout_209.setHorizontalSpacing(5)
        self.gridLayout_209.setContentsMargins(0, 0, 0, 0)
        self.toolButton_213 = QToolButton(self.frame_200)
        self.toolButton_213.setObjectName("toolButton_213")
        self.toolButton_213.setMinimumSize(QSize(50, 50))
        self.toolButton_213.setMaximumSize(QSize(50, 50))
        self.toolButton_213.setIcon(icon4)

        self.gridLayout_209.addWidget(self.toolButton_213, 0, 1, 1, 1)

        self.lineEdit_95 = QLineEdit(self.frame_200)
        self.lineEdit_95.setObjectName("lineEdit_95")
        self.lineEdit_95.setMinimumSize(QSize(0, 50))

        self.gridLayout_209.addWidget(self.lineEdit_95, 0, 0, 1, 1)

        self.toolButton_214 = QToolButton(self.frame_200)
        self.toolButton_214.setObjectName("toolButton_214")
        self.toolButton_214.setMinimumSize(QSize(50, 50))
        self.toolButton_214.setMaximumSize(QSize(50, 50))
        self.toolButton_214.setIcon(icon5)

        self.gridLayout_209.addWidget(self.toolButton_214, 0, 2, 1, 1)

        self.gridLayout_208.addWidget(self.frame_200, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_199, 15, 0, 1, 1)

        self.frame_191 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_191.setObjectName("frame_191")
        self.frame_191.setMinimumSize(QSize(0, 200))
        self.frame_191.setMaximumSize(QSize(16777215, 200))
        self.frame_191.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-col"
            "or: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   back"
            "ground: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            ""
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:"
            "horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.gridLayout_200 = QGridLayout(self.frame_191)
        self.gridLayout_200.setObjectName("gridLayout_200")
        self.gridLayout_200.setContentsMargins(20, 20, 20, 20)
        self.label_193 = QLabel(self.frame_191)
        self.label_193.setObjectName("label_193")
        self.label_193.setMinimumSize(QSize(90, 30))
        self.label_193.setMaximumSize(QSize(90, 30))
        self.label_193.setStyleSheet(
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.label_193.setTextFormat(Qt.AutoText)
        self.label_193.setScaledContents(True)
        self.label_193.setAlignment(Qt.AlignCenter)
        self.label_193.setWordWrap(False)
        self.label_193.setOpenExternalLinks(False)

        self.gridLayout_200.addWidget(self.label_193, 0, 0, 1, 1)

        self.label_194 = QLabel(self.frame_191)
        self.label_194.setObjectName("label_194")

        self.gridLayout_200.addWidget(self.label_194, 0, 1, 1, 1)

        self.frame_192 = QFrame(self.frame_191)
        self.frame_192.setObjectName("frame_192")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.gridLayout_201 = QGridLayout(self.frame_192)
        self.gridLayout_201.setObjectName("gridLayout_201")
        self.gridLayout_201.setHorizontalSpacing(5)
        self.gridLayout_201.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_91 = QLineEdit(self.frame_192)
        self.lineEdit_91.setObjectName("lineEdit_91")
        self.lineEdit_91.setMinimumSize(QSize(0, 50))

        self.gridLayout_201.addWidget(self.lineEdit_91, 0, 0, 1, 1)

        self.toolButton_205 = QToolButton(self.frame_192)
        self.toolButton_205.setObjectName("toolButton_205")
        self.toolButton_205.setMinimumSize(QSize(50, 50))
        self.toolButton_205.setMaximumSize(QSize(50, 50))
        self.toolButton_205.setIcon(icon5)

        self.gridLayout_201.addWidget(self.toolButton_205, 0, 2, 1, 1)

        self.toolButton_206 = QToolButton(self.frame_192)
        self.toolButton_206.setObjectName("toolButton_206")
        self.toolButton_206.setMinimumSize(QSize(50, 50))
        self.toolButton_206.setMaximumSize(QSize(50, 50))
        self.toolButton_206.setIcon(icon4)

        self.gridLayout_201.addWidget(self.toolButton_206, 0, 1, 1, 1)

        self.gridLayout_200.addWidget(self.frame_192, 1, 0, 1, 2)

        self.gridLayout_12.addWidget(self.frame_191, 17, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_13.addWidget(self.scrollArea_4, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.gridLayout_5.addWidget(self.tabWidget_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "}\n"
            "QPushButton {\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "QPushButton:hover {\n"
            "                border-style: solid;\n"
            "                border-top-color: transparent;\n"
            "                border-right-color: transparent;\n"
            "                border-left-color: #00a884;\n"
            "                border-bottom-color: transparent;\n"
            "                border-width: 5px;\n"
            "                background-color: rgb(45, 45, 45);\n"
            "}"
        )
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn = QPushButton(self.frame_3)
        self.btn.setObjectName("btn")
        self.btn.setMinimumSize(QSize(90, 190))
        self.btn.setMaximumSize(QSize(90, 16777215))
        self.btn.setStyleSheet("")
        icon6 = QIcon()
        icon6.addFile(
            ":/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn.setIcon(icon6)

        self.gridLayout_4.addWidget(self.btn, 0, 0, 1, 1)

        self.btn2 = QPushButton(self.frame_3)
        self.btn2.setObjectName("btn2")
        self.btn2.setMinimumSize(QSize(90, 190))
        self.btn2.setMaximumSize(QSize(90, 16777215))
        self.btn2.setStyleSheet("")
        icon7 = QIcon()
        icon7.addFile(":/images/icons/cil-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn2.setIcon(icon7)

        self.gridLayout_4.addWidget(self.btn2, 2, 0, 1, 1)

        self.btn3 = QPushButton(self.frame_3)
        self.btn3.setObjectName("btn3")
        self.btn3.setMinimumSize(QSize(90, 190))
        self.btn3.setMaximumSize(QSize(90, 16777215))
        self.btn3.setStyleSheet("")
        icon8 = QIcon()
        icon8.addFile(":/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn3.setIcon(icon8)

        self.gridLayout_4.addWidget(self.btn3, 3, 0, 1, 1)

        self.btn1 = QPushButton(self.frame_3)
        self.btn1.setObjectName("btn1")
        self.btn1.setMinimumSize(QSize(90, 190))
        self.btn1.setMaximumSize(QSize(90, 16777215))
        self.btn1.setStyleSheet("")
        icon9 = QIcon()
        icon9.addFile(
            ":/images/icons/cil-wifi-signal-2.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn1.setIcon(icon9)

        self.gridLayout_4.addWidget(self.btn1, 1, 0, 1, 1)

        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_15 = QGridLayout(self.tab_2)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setMinimumSize(QSize(100, 0))
        self.frame_4.setMaximumSize(QSize(100, 16777215))
        self.frame_4.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: rgb(32, 32, 32);\n"
            "}\n"
            "QPushButton {\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "QPushButton:hover {\n"
            "                border-style: solid;\n"
            "                border-top-color: transparent;\n"
            "                border-right-color: transparent;\n"
            "                border-left-color: #00a884;\n"
            "                border-bottom-color: transparent;\n"
            "                border-width: 5px;\n"
            "                background-color: rgb(45, 45, 45);\n"
            "}"
        )
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_4)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_enc = QPushButton(self.frame_4)
        self.btn_enc.setObjectName("btn_enc")
        self.btn_enc.setMinimumSize(QSize(90, 390))
        self.btn_enc.setMaximumSize(QSize(90, 16777215))
        self.btn_enc.setStyleSheet("")
        icon10 = QIcon()
        icon10.addFile(
            ":/images/icons/cil-expand-up.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_enc.setIcon(icon10)

        self.gridLayout_14.addWidget(self.btn_enc, 0, 0, 1, 1)

        self.btn_dec = QPushButton(self.frame_4)
        self.btn_dec.setObjectName("btn_dec")
        self.btn_dec.setMinimumSize(QSize(90, 390))
        self.btn_dec.setMaximumSize(QSize(90, 16777215))
        self.btn_dec.setStyleSheet("")
        icon11 = QIcon()
        icon11.addFile(
            ":/images/icons/cil-expand-down.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_dec.setIcon(icon11)

        self.gridLayout_14.addWidget(self.btn_dec, 1, 0, 1, 1)

        self.gridLayout_15.addWidget(self.frame_4, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.gridLayout_18 = QGridLayout(self.page)
        self.gridLayout_18.setSpacing(10)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.page)
        self.frame_26.setObjectName("frame_26")
        self.frame_26.setMinimumSize(QSize(0, 60))
        self.frame_26.setMaximumSize(QSize(16777215, 60))
        self.frame_26.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_26)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.horizontalSpacer_16 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_29.addItem(self.horizontalSpacer_16, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame_26)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')

        self.gridLayout_29.addWidget(self.label_10, 0, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_29.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.gridLayout_18.addWidget(self.frame_26, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "	border-radius: 8px;\n"
            ""
            "	border-width: 2px;\n"
            "	border-style: solid;\n"
            "	border-color: #00a884;\n"
            '	font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            ""
        )
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_8)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName("frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 80))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_14)
        self.gridLayout_16.setSpacing(10)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_14)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 70))
        self.lineEdit.setMaximumSize(QSize(16777215, 70))
        self.lineEdit.setStyleSheet(
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.toolButton_219 = QToolButton(self.frame_14)
        self.toolButton_219.setObjectName("toolButton_219")
        self.toolButton_219.setMinimumSize(QSize(70, 70))
        self.toolButton_219.setMaximumSize(QSize(70, 70))
        self.toolButton_219.setIcon(icon5)

        self.gridLayout_16.addWidget(self.toolButton_219, 0, 1, 1, 1)

        self.gridLayout_17.addWidget(self.frame_14, 1, 1, 1, 1)

        self.label_6 = QToolButton(self.frame_8)
        self.label_6.setObjectName("label_6")
        self.label_6.setEnabled(True)
        self.label_6.setMinimumSize(QSize(900, 400))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setAcceptDrops(True)
        self.label_6.setStyleSheet('font: 18pt "MS Shell Dlg 2";\n' "")

        self.gridLayout_17.addWidget(self.label_6, 0, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_17.addItem(self.horizontalSpacer_20, 0, 0, 1, 1)

        self.toolButton_4 = QToolButton(self.frame_8)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(900, 70))
        self.toolButton_4.setMaximumSize(QSize(16777215, 70))
        self.toolButton_4.setStyleSheet('font: 9pt "Arial Rounded MT Bold";')

        self.gridLayout_17.addWidget(self.toolButton_4, 2, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_17.addItem(self.horizontalSpacer_21, 0, 2, 1, 1)

        self.gridLayout_18.addWidget(self.frame_8, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_61 = QGridLayout(self.page_2)
        self.gridLayout_61.setSpacing(10)
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.page_2)
        self.frame_27.setObjectName("frame_27")
        self.frame_27.setMinimumSize(QSize(0, 60))
        self.frame_27.setMaximumSize(QSize(16777215, 60))
        self.frame_27.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_27)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.horizontalSpacer_18 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_32.addItem(self.horizontalSpacer_18, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame_27)
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')

        self.gridLayout_32.addWidget(self.label_13, 0, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_32.addItem(self.horizontalSpacer_19, 0, 2, 1, 1)

        self.gridLayout_61.addWidget(self.frame_27, 0, 0, 1, 1)

        self.frame_42 = QFrame(self.page_2)
        self.frame_42.setObjectName("frame_42")
        self.frame_42.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "	border-radius: 8px;\n"
            ""
            "	border-width: 2px;\n"
            "	border-style: solid;\n"
            "	border-color: #00a884;\n"
            '	font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            ""
        )
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_42)
        self.gridLayout_59.setSpacing(0)
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName("frame_43")
        self.frame_43.setMaximumSize(QSize(16777215, 80))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_43)
        self.gridLayout_60.setSpacing(10)
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = QLineEdit(self.frame_43)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 70))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_7.setStyleSheet(
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";'
        )
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.lineEdit_7, 0, 0, 1, 1)

        self.toolButton_220 = QToolButton(self.frame_43)
        self.toolButton_220.setObjectName("toolButton_220")
        self.toolButton_220.setMinimumSize(QSize(70, 70))
        self.toolButton_220.setMaximumSize(QSize(70, 70))
        icon12 = QIcon()
        icon12.addFile(
            ":/images/icons/cil-clipboard.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.toolButton_220.setIcon(icon12)

        self.gridLayout_60.addWidget(self.toolButton_220, 0, 1, 1, 1)

        self.gridLayout_59.addWidget(self.frame_43, 1, 1, 1, 1)

        self.label_16 = QToolButton(self.frame_42)
        self.label_16.setObjectName("label_16")
        self.label_16.setEnabled(True)
        self.label_16.setMinimumSize(QSize(900, 400))
        self.label_16.setMaximumSize(QSize(16777215, 16777215))
        self.label_16.setAcceptDrops(True)
        self.label_16.setStyleSheet('font: 18pt "MS Shell Dlg 2";\n' "")

        self.gridLayout_59.addWidget(self.label_16, 0, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_59.addItem(self.horizontalSpacer_22, 0, 0, 1, 1)

        self.toolButton_5 = QToolButton(self.frame_42)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(900, 70))
        self.toolButton_5.setMaximumSize(QSize(16777215, 70))
        self.toolButton_5.setStyleSheet('font: 9pt "Arial Rounded MT Bold";')

        self.gridLayout_59.addWidget(self.toolButton_5, 2, 1, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_59.addItem(self.horizontalSpacer_23, 0, 2, 1, 1)

        self.gridLayout_61.addWidget(self.frame_42, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_15.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.tab_3)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_6)
        self.gridLayout_19.setSpacing(25)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_19.setContentsMargins(25, 25, 25, 25)
        self.tableWidget = QTableWidget(self.frame_6)
        if self.tableWidget.columnCount() < 2:
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if self.tableWidget.rowCount() < 2:
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        self.tableWidget.setObjectName("tableWidget")

        self.gridLayout_19.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.tab_3)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_5)
        self.gridLayout_24.setSpacing(20)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout_24.setContentsMargins(25, 25, 25, 25)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName("frame_7")
        self.frame_7.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: #303030;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_7)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_2, 1, 0, 1, 1)

        self.gridLayout_24.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName("frame_10")
        self.frame_10.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: #303030;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_10)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName("label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_7, 1, 0, 1, 1)

        self.gridLayout_24.addWidget(self.frame_10, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName("frame_9")
        self.frame_9.setStyleSheet(
            "QFrame\n"
            "{\n"
            "background-color: #303030;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_9)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_4, 1, 0, 1, 1)

        self.gridLayout_24.addWidget(self.frame_9, 0, 2, 1, 1)

        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.gridLayout_20.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Linux Commands Helper", None)
        )
        # if QT_CONFIG(tooltip)
        self.file_pushButton.setToolTip(
            QCoreApplication.translate("MainWindow", "Encrypt & Decrypt File", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.file_pushButton.setStatusTip(
            QCoreApplication.translate("MainWindow", "Encrypt & Decrypt File", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.file_pushButton.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Encrypt & Decrypt File", None)
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.file_pushButton.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        self.file_pushButton.setText("")
        # if QT_CONFIG(tooltip)
        self.lch_pushButton.setToolTip(
            QCoreApplication.translate("MainWindow", "Linux Commands Helper", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.lch_pushButton.setStatusTip(
            QCoreApplication.translate("MainWindow", "Linux Commands Helper", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.lch_pushButton.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Linux Commands Helper", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.lch_pushButton.setText("")
        # if QT_CONFIG(tooltip)
        self.da_pushButton.setToolTip(
            QCoreApplication.translate("MainWindow", "Storage Analyzer", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.da_pushButton.setStatusTip(
            QCoreApplication.translate("MainWindow", "Storage Analyzer", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.da_pushButton.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Storage Analyzer", None)
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.da_pushButton.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.da_pushButton.setText("")
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        self.label_99.setText(QCoreApplication.translate("MainWindow", "rmdir", None))
        self.label_100.setText(
            QCoreApplication.translate("MainWindow", "Deletes an empty directory", None)
        )
        self.toolButton_107.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_107.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_42.setText(
            QCoreApplication.translate("MainWindow", "rmdir [directoryName]", None)
        )
        self.toolButton_108.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_108.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_101.setText(QCoreApplication.translate("MainWindow", "mkdir", None))
        self.label_102.setText(
            QCoreApplication.translate("MainWindow", "Creates a new directory", None)
        )
        self.toolButton_109.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_109.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_43.setText(
            QCoreApplication.translate("MainWindow", "mkdir [directoryName]", None)
        )
        self.toolButton_110.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_110.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_97.setText(QCoreApplication.translate("MainWindow", "touch", None))
        self.label_98.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Creates an empty file or updates the timestamp of an existing file",
                None,
            )
        )
        self.toolButton_105.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_105.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_41.setText(
            QCoreApplication.translate("MainWindow", "touch [fileName]", None)
        )
        self.toolButton_106.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_106.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_69.setText(QCoreApplication.translate("MainWindow", "diff", None))
        self.label_70.setText(
            QCoreApplication.translate(
                "MainWindow", "Compares two files and displays the differences", None
            )
        )
        self.toolButton_77.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_77.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_27.setText(
            QCoreApplication.translate("MainWindow", "diff [file 1] [file 2]", None)
        )
        self.toolButton_78.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_78.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_115.setText(
            QCoreApplication.translate("MainWindow", "zip/unzip", None)
        )
        self.label_116.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Compresses files into a ZIP archive and extracts ZIP files",
                None,
            )
        )
        self.toolButton_123.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_123.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_124.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_124.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_50.setText(
            QCoreApplication.translate(
                "MainWindow", "zip [Compresses_file_name] [file(s)]", None
            )
        )
        self.lineEdit_46.setText(
            QCoreApplication.translate(
                "MainWindow", "unzip [Compressed_file_name.zip]", None
            )
        )
        self.toolButton_115.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_115.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_116.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_116.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_73.setText(QCoreApplication.translate("MainWindow", "stat", None))
        self.label_74.setText(
            QCoreApplication.translate(
                "MainWindow", "Displays detailed information about a file", None
            )
        )
        self.toolButton_81.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_81.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_29.setText(
            QCoreApplication.translate("MainWindow", "stat [fileName]", None)
        )
        self.toolButton_82.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_82.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_111.setText(
            QCoreApplication.translate("MainWindow", "rar/unrar", None)
        )
        self.label_112.setText(
            QCoreApplication.translate("MainWindow", "Manages RAR file archives", None)
        )
        self.toolButton_120.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_120.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_48.setText(
            QCoreApplication.translate("MainWindow", "rar archive.rar", None)
        )
        self.toolButton_119.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_119.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_49.setText(
            QCoreApplication.translate("MainWindow", "unrar archive.rar", None)
        )
        self.toolButton_121.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_121.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_122.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_122.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_95.setText(QCoreApplication.translate("MainWindow", "cp", None))
        self.label_96.setText(
            QCoreApplication.translate(
                "MainWindow", "Copies files and directories", None
            )
        )
        self.toolButton_103.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_103.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_40.setText(
            QCoreApplication.translate(
                "MainWindow", "cp [FileName] [destinationToPaste]", None
            )
        )
        self.toolButton_104.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_104.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_71.setText(QCoreApplication.translate("MainWindow", "tar -cf", None))
        self.label_72.setText(
            QCoreApplication.translate("MainWindow", "To create a new archive", None)
        )
        self.lineEdit_28.setText(
            QCoreApplication.translate(
                "MainWindow", "tar -cf [archive_file_name.tar] [file(s)]", None
            )
        )
        self.toolButton_80.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_80.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_79.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_79.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_105.setText(QCoreApplication.translate("MainWindow", "cd", None))
        self.label_106.setText(
            QCoreApplication.translate(
                "MainWindow", "Switches the current working directory", None
            )
        )
        self.toolButton_113.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_113.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_45.setText(
            QCoreApplication.translate("MainWindow", "cd [directory]", None)
        )
        self.toolButton_114.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_114.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_89.setText(QCoreApplication.translate("MainWindow", "mv", None))
        self.label_90.setText(
            QCoreApplication.translate(
                "MainWindow", "Moves files between directories", None
            )
        )
        self.toolButton_97.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_97.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_37.setText(
            QCoreApplication.translate(
                "MainWindow", "mv [FileName] [destinationToPaste]", None
            )
        )
        self.toolButton_98.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_98.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_79.setText(QCoreApplication.translate("MainWindow", "grep", None))
        self.label_80.setText(
            QCoreApplication.translate(
                "MainWindow", "Searches for text patterns in files", None
            )
        )
        self.toolButton_87.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_87.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_32.setText(
            QCoreApplication.translate(
                "MainWindow", "grep [searchWord] [file name]", None
            )
        )
        self.toolButton_88.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_88.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_28.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Lists files and directories in the current directory",
                None,
            )
        )
        self.label_27.setText(QCoreApplication.translate("MainWindow", "ls ", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", "ls", None))
        self.toolButton_36.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_36.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_35.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_35.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_81.setText(QCoreApplication.translate("MainWindow", "less", None))
        self.label_82.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Allows forward and backward navigation through text",
                None,
            )
        )
        self.toolButton_89.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_89.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_33.setText(
            QCoreApplication.translate("MainWindow", "less [fileName]", None)
        )
        self.toolButton_90.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_90.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_103.setText(QCoreApplication.translate("MainWindow", "pwd", None))
        self.label_104.setText(
            QCoreApplication.translate(
                "MainWindow", "Displays the current directory's full path", None
            )
        )
        self.toolButton_111.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_111.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_44.setText(QCoreApplication.translate("MainWindow", "pwd", None))
        self.toolButton_112.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_112.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_85.setText(QCoreApplication.translate("MainWindow", "cat", None))
        self.label_86.setText(
            QCoreApplication.translate(
                "MainWindow", "Displays the contents of one or more files", None
            )
        )
        self.toolButton_93.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_93.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_35.setText(
            QCoreApplication.translate("MainWindow", "cat [fileName]", None)
        )
        self.toolButton_94.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_94.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_75.setText(QCoreApplication.translate("MainWindow", "chown", None))
        self.label_76.setText(
            QCoreApplication.translate("MainWindow", "Changes file ownership", None)
        )
        self.toolButton_83.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_83.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_30.setText(
            QCoreApplication.translate(
                "MainWindow", "chown [username] [filename]", None
            )
        )
        self.toolButton_84.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_84.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_77.setText(QCoreApplication.translate("MainWindow", "chmod", None))
        self.label_78.setText(
            QCoreApplication.translate("MainWindow", "Modifies file permissions", None)
        )
        self.toolButton_85.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_85.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_31.setText(
            QCoreApplication.translate(
                "MainWindow", "chmod [groupName]+[permissionName(rwx)] [fileName]", None
            )
        )
        self.toolButton_86.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_86.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_87.setText(QCoreApplication.translate("MainWindow", "rm", None))
        self.label_88.setText(
            QCoreApplication.translate(
                "MainWindow", "Deletes files and directories", None
            )
        )
        self.toolButton_95.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_95.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_36.setText(
            QCoreApplication.translate(
                "MainWindow", "rm [file or Directory name]", None
            )
        )
        self.toolButton_96.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_96.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_107.setText(
            QCoreApplication.translate("MainWindow", "tar -xf", None)
        )
        self.label_108.setText(
            QCoreApplication.translate("MainWindow", "To extract an archive", None)
        )
        self.toolButton_117.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_117.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_47.setText(
            QCoreApplication.translate("MainWindow", "tar -xf archive.tar", None)
        )
        self.toolButton_118.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_118.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_83.setText(QCoreApplication.translate("MainWindow", "more", None))
        self.label_84.setText(
            QCoreApplication.translate(
                "MainWindow", "Displays text one screen at a time", None
            )
        )
        self.toolButton_91.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_91.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_34.setText(
            QCoreApplication.translate("MainWindow", "more [fileName]", None)
        )
        self.toolButton_92.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_92.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "Tab 1", None),
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "Networking", None)
        )
        self.label_131.setText(QCoreApplication.translate("MainWindow", "ip", None))
        self.label_132.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Show and manipulate routing, devices, policy routing, and tunnels",
                None,
            )
        )
        self.toolButton_147.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_147.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_62.setText(
            QCoreApplication.translate("MainWindow", "ip route show", None)
        )
        self.toolButton_148.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_148.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_139.setText(QCoreApplication.translate("MainWindow", "ping", None))
        self.label_140.setText(
            QCoreApplication.translate(
                "MainWindow", "Send ICMP ECHO_REQUEST to network hosts", None
            )
        )
        self.toolButton_155.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_155.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_66.setText(
            QCoreApplication.translate(
                "MainWindow", "ping [hostname or IP address]", None
            )
        )
        self.toolButton_156.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_156.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_135.setText(
            QCoreApplication.translate("MainWindow", "tcpdump", None)
        )
        self.label_136.setText(
            QCoreApplication.translate("MainWindow", "A packet analyzer", None)
        )
        self.toolButton_151.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_151.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_64.setText(
            QCoreApplication.translate("MainWindow", "tcpdump -i [interface]", None)
        )
        self.toolButton_152.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_152.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_109.setText(
            QCoreApplication.translate("MainWindow", "netstat", None)
        )
        self.label_110.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Display networking information, including routing tables, interface statistics, and more.",
                None,
            )
        )
        self.toolButton_125.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_125.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_51.setText(
            QCoreApplication.translate("MainWindow", "netstat -nr", None)
        )
        self.toolButton_126.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_126.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_31.setText(
            QCoreApplication.translate(
                "MainWindow", "Configure a network interface", None
            )
        )
        self.label_32.setText(
            QCoreApplication.translate("MainWindow", "ifconfig", None)
        )
        self.toolButton_39.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_39.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_8.setText(
            QCoreApplication.translate("MainWindow", "ifconfig", None)
        )
        self.toolButton_40.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_40.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_117.setText(QCoreApplication.translate("MainWindow", "ss", None))
        self.label_118.setText(
            QCoreApplication.translate(
                "MainWindow", "Another utility to investigate sockets", None
            )
        )
        self.toolButton_129.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_129.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_53.setText(
            QCoreApplication.translate("MainWindow", "ss -tunlp", None)
        )
        self.toolButton_130.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_130.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_127.setText(QCoreApplication.translate("MainWindow", "route", None))
        self.label_128.setText(
            QCoreApplication.translate(
                "MainWindow", "Show or manipulate the IP routing table", None
            )
        )
        self.toolButton_143.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_143.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_60.setText(
            QCoreApplication.translate("MainWindow", "route -n", None)
        )
        self.toolButton_144.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_144.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_119.setText(
            QCoreApplication.translate("MainWindow", "ip6tables", None)
        )
        self.label_120.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Administration tool for IPv6 packet filtering and NAT",
                None,
            )
        )
        self.toolButton_131.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_131.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_54.setText(
            QCoreApplication.translate("MainWindow", "ip6tables -L", None)
        )
        self.toolButton_132.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_132.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_129.setText(QCoreApplication.translate("MainWindow", "sshd", None))
        self.label_130.setText(
            QCoreApplication.translate(
                "MainWindow", "Secure Shell Daemon (SSH server)", None
            )
        )
        self.lineEdit_61.setText(
            QCoreApplication.translate("MainWindow", "service sshd status", None)
        )
        self.toolButton_145.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_145.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_146.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_146.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_133.setText(QCoreApplication.translate("MainWindow", "host", None))
        self.label_134.setText(
            QCoreApplication.translate("MainWindow", "DNS lookup utility", None)
        )
        self.toolButton_149.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_149.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_63.setText(
            QCoreApplication.translate(
                "MainWindow", "host [hostname or IP address]", None
            )
        )
        self.toolButton_150.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_150.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_145.setText(QCoreApplication.translate("MainWindow", "nc", None))
        self.label_146.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Netcat - utility for reading from and writing to network connections",
                None,
            )
        )
        self.toolButton_162.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_162.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_161.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_161.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_69.setText(
            QCoreApplication.translate(
                "MainWindow", "nc -zv [hostname or IP address] [port]", None
            )
        )
        self.label_149.setText(QCoreApplication.translate("MainWindow", "wget", None))
        self.label_150.setText(
            QCoreApplication.translate(
                "MainWindow", "Non-interactive downloader of files from the web", None
            )
        )
        self.toolButton_165.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_165.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_71.setText(
            QCoreApplication.translate("MainWindow", "wget [URL]", None)
        )
        self.toolButton_166.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_166.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_123.setText(
            QCoreApplication.translate("MainWindow", "iptables", None)
        )
        self.label_124.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Administration tool for IPv4 packet filtering and NAT",
                None,
            )
        )
        self.toolButton_137.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_137.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_57.setText(
            QCoreApplication.translate("MainWindow", "iptables -L", None)
        )
        self.toolButton_138.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_138.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_143.setText(QCoreApplication.translate("MainWindow", "nmap", None))
        self.label_144.setText(
            QCoreApplication.translate(
                "MainWindow", "Network exploration tool and security scanner", None
            )
        )
        self.toolButton_159.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_159.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_68.setText(
            QCoreApplication.translate(
                "MainWindow", "nmap [hostname or IP address]", None
            )
        )
        self.toolButton_160.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_160.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_151.setText(QCoreApplication.translate("MainWindow", "iw", None))
        self.label_152.setText(
            QCoreApplication.translate(
                "MainWindow",
                "nl80211 based CLI configuration utility for wireless devices",
                None,
            )
        )
        self.toolButton_167.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_167.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_72.setText(
            QCoreApplication.translate("MainWindow", "iw dev", None)
        )
        self.toolButton_168.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_168.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_121.setText(QCoreApplication.translate("MainWindow", "curl", None))
        self.label_122.setText(
            QCoreApplication.translate(
                "MainWindow", "Command-line tool for making HTTP requests", None
            )
        )
        self.toolButton_134.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_134.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_133.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_133.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_55.setText(
            QCoreApplication.translate("MainWindow", "curl [URL]", None)
        )
        self.label_141.setText(
            QCoreApplication.translate("MainWindow", "iwconfig", None)
        )
        self.label_142.setText(
            QCoreApplication.translate(
                "MainWindow", "Configure a wireless network interface", None
            )
        )
        self.toolButton_157.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_157.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_67.setText(
            QCoreApplication.translate("MainWindow", "iwconfig", None)
        )
        self.toolButton_158.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_158.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_137.setText(QCoreApplication.translate("MainWindow", "arp", None))
        self.label_138.setText(
            QCoreApplication.translate(
                "MainWindow", "Display or modify the ARP cache", None
            )
        )
        self.toolButton_153.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_153.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_65.setText(
            QCoreApplication.translate("MainWindow", "arp -a", None)
        )
        self.toolButton_154.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_154.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_147.setText(QCoreApplication.translate("MainWindow", "dig", None))
        self.label_148.setText(
            QCoreApplication.translate("MainWindow", "A flexible DNS query tool", None)
        )
        self.toolButton_163.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_163.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_70.setText(
            QCoreApplication.translate(
                "MainWindow", "dig [hostname or IP address]", None
            )
        )
        self.toolButton_164.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_164.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_113.setText(
            QCoreApplication.translate("MainWindow", "traceroute", None)
        )
        self.label_114.setText(
            QCoreApplication.translate(
                "MainWindow", "Print the route packets take to network host", None
            )
        )
        self.toolButton_127.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_127.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_52.setText(
            QCoreApplication.translate(
                "MainWindow", "traceroute [hostname or IP address]", None
            )
        )
        self.toolButton_128.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_128.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_6),
            QCoreApplication.translate("MainWindow", "Page", None),
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "Process Management", None)
        )
        self.label_181.setText(QCoreApplication.translate("MainWindow", "du", None))
        self.label_182.setText(
            QCoreApplication.translate("MainWindow", "Estimate file space usage", None)
        )
        self.toolButton_193.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_193.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_85.setText(
            QCoreApplication.translate("MainWindow", "du -h", None)
        )
        self.toolButton_194.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_194.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_125.setText(QCoreApplication.translate("MainWindow", "kill", None))
        self.label_126.setText(
            QCoreApplication.translate(
                "MainWindow", "Terminate or signal processes", None
            )
        )
        self.toolButton_135.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_135.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_56.setText(
            QCoreApplication.translate("MainWindow", " kill [process_id]", None)
        )
        self.toolButton_136.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_136.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_159.setText(
            QCoreApplication.translate("MainWindow", "killall", None)
        )
        self.label_160.setText(
            QCoreApplication.translate("MainWindow", "Kill processes by name", None)
        )
        self.toolButton_139.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_139.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_58.setText(
            QCoreApplication.translate("MainWindow", "killall [process_name]", None)
        )
        self.toolButton_140.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_140.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_185.setText(QCoreApplication.translate("MainWindow", "df", None))
        self.label_186.setText(
            QCoreApplication.translate("MainWindow", "Display disk space usage", None)
        )
        self.toolButton_197.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_197.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_87.setText(
            QCoreApplication.translate("MainWindow", "df -h", None)
        )
        self.toolButton_198.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_198.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_175.setText(
            QCoreApplication.translate("MainWindow", "shutdown", None)
        )
        self.label_176.setText(
            QCoreApplication.translate(
                "MainWindow", "Halt or power off the system", None
            )
        )
        self.toolButton_187.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_187.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_82.setText(
            QCoreApplication.translate("MainWindow", "shutdown -h now", None)
        )
        self.toolButton_188.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_188.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_183.setText(QCoreApplication.translate("MainWindow", "ps", None))
        self.label_184.setText(
            QCoreApplication.translate(
                "MainWindow", "Report a snapshot of the current processes", None
            )
        )
        self.toolButton_195.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_195.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_86.setText(
            QCoreApplication.translate("MainWindow", "ps aux", None)
        )
        self.toolButton_196.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_196.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_157.setText(QCoreApplication.translate("MainWindow", "pkill", None))
        self.label_158.setText(
            QCoreApplication.translate(
                "MainWindow", "Signal processes based on their name", None
            )
        )
        self.toolButton_173.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_173.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_75.setText(
            QCoreApplication.translate("MainWindow", "pkill [process_name]", None)
        )
        self.toolButton_174.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_174.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_177.setText(QCoreApplication.translate("MainWindow", "free", None))
        self.label_178.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Display amount of free and used memory in the system",
                None,
            )
        )
        self.toolButton_189.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_189.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_83.setText(
            QCoreApplication.translate("MainWindow", "free -h", None)
        )
        self.toolButton_190.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_190.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_187.setText(QCoreApplication.translate("MainWindow", "htop", None))
        self.label_188.setText(
            QCoreApplication.translate(
                "MainWindow", "An interactive process viewer", None
            )
        )
        self.toolButton_199.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_199.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_88.setText(QCoreApplication.translate("MainWindow", "htop", None))
        self.toolButton_200.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_200.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_161.setText(
            QCoreApplication.translate("MainWindow", "systemctl", None)
        )
        self.label_162.setText(
            QCoreApplication.translate(
                "MainWindow", "Control the systemd system and service manager", None
            )
        )
        self.lineEdit_38.setText(
            QCoreApplication.translate(
                "MainWindow", "systemctl start [service_name]", None
            )
        )
        self.toolButton_175.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_175.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_176.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_176.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_76.setText(
            QCoreApplication.translate(
                "MainWindow", "systemctl status [service_name]", None
            )
        )
        self.lineEdit_39.setText(
            QCoreApplication.translate(
                "MainWindow", "systemctl stop [service_name]", None
            )
        )
        self.toolButton_99.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_99.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_100.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_100.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_101.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_101.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_102.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_102.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_169.setText(QCoreApplication.translate("MainWindow", "reboot", None))
        self.label_170.setText(
            QCoreApplication.translate("MainWindow", "Reboot the system", None)
        )
        self.toolButton_181.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_181.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_182.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_182.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_79.setText(
            QCoreApplication.translate("MainWindow", "reboot", None)
        )
        self.label_155.setText(QCoreApplication.translate("MainWindow", "ps", None))
        self.label_156.setText(
            QCoreApplication.translate(
                "MainWindow", "Report a snapshot of the current processes", None
            )
        )
        self.toolButton_171.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_171.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_74.setText(
            QCoreApplication.translate("MainWindow", "ps aux", None)
        )
        self.toolButton_172.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_172.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_167.setText(
            QCoreApplication.translate("MainWindow", "journalctl", None)
        )
        self.label_168.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Query and display messages from the journal, managed by systemd",
                None,
            )
        )
        self.toolButton_179.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_179.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_78.setText(
            QCoreApplication.translate("MainWindow", "journalctl", None)
        )
        self.toolButton_180.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_180.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_153.setText(QCoreApplication.translate("MainWindow", "top", None))
        self.label_154.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Display and update sorted information about system processes",
                None,
            )
        )
        self.toolButton_169.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_169.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_73.setText(QCoreApplication.translate("MainWindow", "top", None))
        self.toolButton_170.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_170.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_33.setText(
            QCoreApplication.translate(
                "MainWindow", "Display how long the system has been running", None
            )
        )
        self.label_34.setText(QCoreApplication.translate("MainWindow", "uptime", None))
        self.toolButton_41.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_41.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_9.setText(
            QCoreApplication.translate("MainWindow", "uptime", None)
        )
        self.toolButton_42.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_42.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_7),
            QCoreApplication.translate("MainWindow", "Page", None),
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "User Management", None)
        )
        self.label_179.setText(QCoreApplication.translate("MainWindow", "groups", None))
        self.label_180.setText(
            QCoreApplication.translate(
                "MainWindow", "Display groups a user is in", None
            )
        )
        self.toolButton_191.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_191.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_84.setText(
            QCoreApplication.translate("MainWindow", "groups [username]", None)
        )
        self.toolButton_192.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_192.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_197.setText(QCoreApplication.translate("MainWindow", "visudo", None))
        self.label_198.setText(
            QCoreApplication.translate("MainWindow", "Edit the sudoers file", None)
        )
        self.toolButton_209.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_209.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_210.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_210.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_93.setText(
            QCoreApplication.translate("MainWindow", "visudo", None)
        )
        self.label_189.setText(QCoreApplication.translate("MainWindow", "id", None))
        self.label_190.setText(
            QCoreApplication.translate(
                "MainWindow", "Display user and group information", None
            )
        )
        self.toolButton_201.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_201.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_89.setText(
            QCoreApplication.translate("MainWindow", "id [username]", None)
        )
        self.toolButton_202.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_202.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_199.setText(QCoreApplication.translate("MainWindow", "su", None))
        self.label_200.setText(
            QCoreApplication.translate("MainWindow", "Switch user", None)
        )
        self.toolButton_211.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_211.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_94.setText(
            QCoreApplication.translate("MainWindow", "su [username]", None)
        )
        self.toolButton_212.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_212.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_205.setText(QCoreApplication.translate("MainWindow", "chsh", None))
        self.label_206.setText(
            QCoreApplication.translate("MainWindow", "Change login shell", None)
        )
        self.toolButton_217.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_217.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_97.setText(
            QCoreApplication.translate(
                "MainWindow", "chsh -s [new_shell] [username]", None
            )
        )
        self.toolButton_218.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_218.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_163.setText(QCoreApplication.translate("MainWindow", "passwd", None))
        self.label_164.setText(
            QCoreApplication.translate("MainWindow", "Change user password", None)
        )
        self.toolButton_177.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_177.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_77.setText(
            QCoreApplication.translate("MainWindow", "passwd [username]", None)
        )
        self.toolButton_178.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_178.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_165.setText(
            QCoreApplication.translate("MainWindow", "userdel", None)
        )
        self.label_166.setText(
            QCoreApplication.translate("MainWindow", "Delete a user account", None)
        )
        self.toolButton_183.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_183.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_80.setText(
            QCoreApplication.translate("MainWindow", "userdel [username]", None)
        )
        self.toolButton_184.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_184.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_35.setText(
            QCoreApplication.translate("MainWindow", "Create a new user account", None)
        )
        self.label_36.setText(QCoreApplication.translate("MainWindow", "useradd", None))
        self.toolButton_43.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_43.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_10.setText(
            QCoreApplication.translate("MainWindow", "useradd [username]", None)
        )
        self.toolButton_44.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_44.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_211.setText(QCoreApplication.translate("MainWindow", "su", None))
        self.label_212.setText(
            QCoreApplication.translate("MainWindow", "Switch user", None)
        )
        self.toolButton_223.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_223.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_100.setText(
            QCoreApplication.translate("MainWindow", "su [username]", None)
        )
        self.toolButton_224.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_224.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_209.setText(QCoreApplication.translate("MainWindow", "finger", None))
        self.label_210.setText(
            QCoreApplication.translate("MainWindow", "Display user information", None)
        )
        self.toolButton_221.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_221.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_99.setText(
            QCoreApplication.translate("MainWindow", "finger [username]", None)
        )
        self.toolButton_222.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_222.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_191.setText(
            QCoreApplication.translate("MainWindow", "logname", None)
        )
        self.label_192.setText(
            QCoreApplication.translate(
                "MainWindow", "Print the current login name", None
            )
        )
        self.toolButton_203.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_203.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_90.setText(
            QCoreApplication.translate("MainWindow", "logname", None)
        )
        self.toolButton_204.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_204.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_203.setText(QCoreApplication.translate("MainWindow", "chage", None))
        self.label_204.setText(
            QCoreApplication.translate(
                "MainWindow", "Change user password expiry information", None
            )
        )
        self.toolButton_215.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_215.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_96.setText(
            QCoreApplication.translate("MainWindow", "chage [username]", None)
        )
        self.toolButton_216.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_216.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_195.setText(QCoreApplication.translate("MainWindow", "who", None))
        self.label_196.setText(
            QCoreApplication.translate(
                "MainWindow", "Display who is logged in and what they are doing", None
            )
        )
        self.toolButton_207.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_207.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_92.setText(QCoreApplication.translate("MainWindow", "w", None))
        self.toolButton_208.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_208.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_171.setText(QCoreApplication.translate("MainWindow", "sudo", None))
        self.label_172.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Execute a command as another user (typically as a superuser)",
                None,
            )
        )
        self.toolButton_185.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_185.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_81.setText(
            QCoreApplication.translate("MainWindow", "sudo [command]", None)
        )
        self.toolButton_186.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_186.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_173.setText(
            QCoreApplication.translate("MainWindow", "groupdel", None)
        )
        self.label_174.setText(
            QCoreApplication.translate("MainWindow", "Delete a group", None)
        )
        self.toolButton_141.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_141.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_59.setText(
            QCoreApplication.translate("MainWindow", "groupdel [group_name]", None)
        )
        self.toolButton_142.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_142.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_213.setText(QCoreApplication.translate("MainWindow", "w", None))
        self.label_214.setText(
            QCoreApplication.translate("MainWindow", "A flexible DNS query tool", None)
        )
        self.toolButton_225.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_225.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_101.setText(
            QCoreApplication.translate(
                "MainWindow", "dig [hostname or IP address]", None
            )
        )
        self.toolButton_226.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_226.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_215.setText(
            QCoreApplication.translate("MainWindow", "groupadd", None)
        )
        self.label_216.setText(
            QCoreApplication.translate("MainWindow", "Create a new group", None)
        )
        self.toolButton_227.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_227.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_102.setText(
            QCoreApplication.translate("MainWindow", "groupadd [group_name]", None)
        )
        self.toolButton_228.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_228.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_201.setText(QCoreApplication.translate("MainWindow", "last", None))
        self.label_202.setText(
            QCoreApplication.translate(
                "MainWindow", "Display a list of last logged in users", None
            )
        )
        self.toolButton_213.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_213.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_95.setText(QCoreApplication.translate("MainWindow", "last", None))
        self.toolButton_214.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_214.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_193.setText(QCoreApplication.translate("MainWindow", "whoami", None))
        self.label_194.setText(
            QCoreApplication.translate("MainWindow", "Print effective user ID", None)
        )
        self.lineEdit_91.setText(
            QCoreApplication.translate("MainWindow", "whoami", None)
        )
        self.toolButton_205.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_205.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_206.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_206.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_8),
            QCoreApplication.translate("MainWindow", "Page", None),
        )
        # if QT_CONFIG(tooltip)
        self.btn.setToolTip(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn.setStatusTip(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.btn.setWhatsThis(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.btn.setAccessibleName(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.btn.setAccessibleDescription(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(accessibility)
        self.btn.setText("")
        # if QT_CONFIG(tooltip)
        self.btn2.setToolTip(
            QCoreApplication.translate("MainWindow", "Process Management", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn2.setStatusTip(
            QCoreApplication.translate("MainWindow", "Process Management", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.btn2.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Process Management", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn2.setText("")
        # if QT_CONFIG(tooltip)
        self.btn3.setToolTip(
            QCoreApplication.translate("MainWindow", "User Management", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn3.setStatusTip(
            QCoreApplication.translate("MainWindow", "User Management", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.btn3.setWhatsThis(
            QCoreApplication.translate("MainWindow", "User Management", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn3.setText("")
        # if QT_CONFIG(tooltip)
        self.btn1.setToolTip(
            QCoreApplication.translate("MainWindow", "Networking", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn1.setStatusTip(
            QCoreApplication.translate("MainWindow", "Networking", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.btn1.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Networking", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn1.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Tab 1", None),
        )
        # if QT_CONFIG(tooltip)
        self.btn_enc.setToolTip(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_enc.setStatusTip(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.btn_enc.setWhatsThis(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.btn_enc.setAccessibleName(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.btn_enc.setAccessibleDescription(
            QCoreApplication.translate("MainWindow", "File Management", None)
        )
        # endif // QT_CONFIG(accessibility)
        self.btn_enc.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_dec.setToolTip(
            QCoreApplication.translate("MainWindow", "Networking", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.btn_dec.setStatusTip(
            QCoreApplication.translate("MainWindow", "Networking", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.btn_dec.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Networking", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_dec.setText("")
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Encrypt File", None)
        )
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Key", None)
        )
        self.toolButton_219.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_219.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow", "drop file here to encrypt it", None
            )
        )
        self.toolButton_4.setText(
            QCoreApplication.translate("MainWindow", "Encrypt", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "Decrypt File", None)
        )
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Key", None)
        )
        self.toolButton_220.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_220.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow", "drop file here to decrypt it", None
            )
        )
        self.toolButton_5.setText(
            QCoreApplication.translate("MainWindow", "Decrypt", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Tab 2", None),
        )
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "New Column", None)
        )
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "New Column", None)
        )
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "1", None)
        )
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", "2", None)
        )

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", "ilbbilwdibwd", None)
        )
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", "bidlb", None)
        )
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", "dbiq", None)
        )
        ___qtablewidgetitem7 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", "aojosqj", None)
        )
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(
            QCoreApplication.translate("MainWindow", "Total Disk Space", None)
        )
        self.label_2.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "Used Space", None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Free Space", None)
        )
        self.label_4.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Page", None),
        )

    # retranslateUi
