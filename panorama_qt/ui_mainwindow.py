# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 884)
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.img_path = QTextEdit(self.centralwidget)
        self.img_path.setObjectName(u"img_path")
        self.img_path.setGeometry(QRect(100, 30, 501, 31))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.img_path.setFont(font)
        self.img_path.setToolTipDuration(1)
        self.img_path.setReadOnly(True)
        self.btn_choose_img_path = QPushButton(self.centralwidget)
        self.btn_choose_img_path.setObjectName(u"btn_choose_img_path")
        self.btn_choose_img_path.setEnabled(True)
        self.btn_choose_img_path.setGeometry(QRect(610, 30, 81, 31))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.btn_choose_img_path.setFont(font1)
        self.btn_choose_img_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_choose_img_path.setMouseTracking(False)
        self.btn_choose_img_path.setAutoFillBackground(False)
        self.btn_choose_img_path.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(241, 241, 241);\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(40, 440, 681, 391))
        self.listWidget.setFont(font)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget.setIconSize(QSize(150, 150))
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setFlow(QListView.LeftToRight)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(0)
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setUniformItemSizes(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 71, 31))
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.label.setFont(font2)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 840, 221, 31))
        font3 = QFont()
        font3.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setKerning(True)
        self.frame_2.setFont(font3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(70, 0, 16, 21))
        font4 = QFont()
        font4.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        font4.setKerning(True)
        self.label_16.setFont(font4)
        self.label_16.setLineWidth(1)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_16.setIndent(-1)
        self.img_all_num = QLabel(self.frame_2)
        self.img_all_num.setObjectName(u"img_all_num")
        self.img_all_num.setGeometry(QRect(90, 0, 31, 21))
        self.img_all_num.setFont(font4)
        self.img_all_num.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.img_all_num.setIndent(-1)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(110, 0, 16, 21))
        self.label_18.setFont(font4)
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(150, 0, 31, 21))
        self.label_19.setFont(font4)
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.img_selected_num = QLabel(self.frame_2)
        self.img_selected_num.setObjectName(u"img_selected_num")
        self.img_selected_num.setGeometry(QRect(180, 0, 21, 21))
        self.img_selected_num.setFont(font4)
        self.img_selected_num.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(200, 0, 16, 21))
        self.label_21.setFont(font4)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.check_box_select_all = QCheckBox(self.frame_2)
        self.check_box_select_all.setObjectName(u"check_box_select_all")
        self.check_box_select_all.setGeometry(QRect(0, 0, 51, 16))
        self.check_box_select_all.setFont(font4)
        self.check_box_select_all.setIconSize(QSize(16, 16))
        self.btn_stitch = QPushButton(self.centralwidget)
        self.btn_stitch.setObjectName(u"btn_stitch")
        self.btn_stitch.setEnabled(True)
        self.btn_stitch.setGeometry(QRect(630, 840, 81, 31))
        self.btn_stitch.setFont(font1)
        self.btn_stitch.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stitch.setMouseTracking(False)
        self.btn_stitch.setLayoutDirection(Qt.RightToLeft)
        self.btn_stitch.setAutoFillBackground(False)
        self.btn_stitch.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(241, 241, 241);\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}\n"
"")
        self.btn_stitch.setCheckable(False)
        self.btn_stitch.setAutoDefault(False)
        self.btn_stitch.setFlat(False)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 130, 751, 281))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_video_2 = QLabel(self.frame_3)
        self.label_video_2.setObjectName(u"label_video_2")
        self.label_video_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_video_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(60, 100, 69, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 54, 22))
        self.pushButton_photo = QPushButton(self.centralwidget)
        self.pushButton_photo.setObjectName(u"pushButton_photo")
        self.pushButton_photo.setGeometry(QRect(620, 90, 91, 31))
        self.pushButton_photo.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(241, 241, 241);\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}")
        self.choose_cam = QPushButton(self.centralwidget)
        self.choose_cam.setObjectName(u"choose_cam")
        self.choose_cam.setGeometry(QRect(140, 90, 91, 31))
        self.choose_cam.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(241, 241, 241);\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(179, 216, 255);\n"
"	border-color: rgb(102, 161, 255);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_stitch.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.action_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.action_3.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.img_path.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.img_path.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u62fc\u63a5\u56fe\u7247\u6240\u5728\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.img_path.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u62fc\u63a5\u56fe\u7247\u6240\u5728\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.btn_choose_img_path.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u9009\u62e9\u62fc\u63a5\u56fe\u7247\u6240\u5728\u6587\u4ef6\u5939</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_choose_img_path.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u62fc\u63a5\u56fe\u7247\u6240\u5728\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
        self.btn_choose_img_path.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\u76ee\u5f55\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5171", None))
        self.img_all_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u5f20", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u9009", None))
        self.img_selected_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5f20", None))
#if QT_CONFIG(statustip)
        self.check_box_select_all.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5168\u9009\u6216\u53d6\u6d88\u5168\u9009", None))
#endif // QT_CONFIG(statustip)
        self.check_box_select_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
#if QT_CONFIG(shortcut)
        self.check_box_select_all.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_stitch.setToolTip(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u62fc\u63a5\u6240\u9009\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_stitch.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u62fc\u63a5\u6240\u9009\u56fe\u7247", None))
#endif // QT_CONFIG(statustip)
        self.btn_stitch.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u62fc\u63a5", None))
        self.label_video_2.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934", None))
        self.pushButton_photo.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u7167", None))
        self.choose_cam.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u76f8\u673a", None))
    # retranslateUi

