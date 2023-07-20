import os
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QMessageBox
from PySide2.QtGui import QIcon, QImage, QPixmap
from PySide2.QtCore import Qt, QTimer
from ui_mainwindow import Ui_MainWindow
from imagestitching import OralImgStitch
import matplotlib.pyplot as plt
import cv2
class MainProgram(QMainWindow):
	def __init__(self, parent=None):
		super(MainProgram, self).__init__(parent)

		self.file_path = ''
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.cam = cv2.VideoCapture()
		self.setWindowTitle("全景")
		self.show()



		self.ui.choose_cam.clicked.connect(self.open_camera)
		self.ui.btn_choose_img_path.clicked.connect(self.choose_img_path)
		self.ui.btn_stitch.clicked.connect(self.stitch_img)
		self.ui.listWidget.itemSelectionChanged.connect(self.update_selection_info)
		self.ui.check_box_select_all.stateChanged.connect(self.img_list_select_all)
		self.ui.pushButton_photo.clicked.connect(self.photo_capture)
		self.init_timer()



	def choose_img_path(self):
		self.file_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		print("当前工作目录为：" + self.file_path)
		if self.file_path == '' : return
		self.ui.img_path.setText(self.file_path)
		if self.ui.listWidget.count() != 0:
			self.ui.listWidget.clear()
		for each in os.listdir(self.file_path):
			self.ui.listWidget.addItem(QListWidgetItem(QIcon(self.file_path+"/"+each), each))
		self.ui.img_all_num.setText(str(self.ui.listWidget.count()))

	def stitch_img(self):
		if (self.ui.listWidget.count() == 0) or (len(self.ui.listWidget.selectedItems()) == 0):
			self.stitching_crashHandler(4)
			return

		process_img_list = [self.ui.img_path.toPlainText()+'/'+item.text() 
			for item in self.ui.listWidget.selectedItems()]
		stitcher = OralImgStitch(process_img_list)

		try:
			# if self.ui.check_box_crop.isChecked():
			# 	output_img, status = stitcher.stitchImage(is_crop=True)
			# else:
			# 	output_img, status = stitcher.stitchImage(is_crop=False)
			output_img, status = stitcher.stitchImage(is_crop=False)
			# self.ui.progressBar.setVisible(False)
			if status != 0:
				self.stitching_crashHandler(status)
		except Exception as e:
			print(e)
			self.stitching_crashHandler(3)


		plt.imshow(output_img)
		plt.axis('off')
		plt.show()
		self.ui.listWidget.clearSelection()
		self.ui.check_box_select_all.setCheckState(Qt.Unchecked)
		self.ui.check_box_crop.setCheckState(Qt.Unchecked)
	def img_list_select_all(self, s):
		if s == 2:
			self.ui.listWidget.selectAll()
		else:
			self.ui.listWidget.clearSelection()

	def update_selection_info(self):
		self.ui.img_selected_num.setText(str(len(self.ui.listWidget.selectedItems())))

	def open_camera(self):
		cam_index = self.ui.comboBox.currentIndex()
		print(cam_index)

		flag = self.cam.open(cam_index)
		print(flag)
		if flag is False:
			QMessageBox.information(self, "警告", "该设备未正常连接", QMessageBox.Ok)
		else:
			# 幕布可以播放
			self.ui.label_video_2.setEnabled(True)
			self.timer.start()
			print("beginning！")

	def close_camera(self):
		self.cap.release()
		self.timer.stop()

	def init_timer(self):
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.show_pic)
	def show_pic(self):
		ret, frame = self.cam.read()
		if ret:
			cur_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			# 视频流的长和宽
			height, width = cur_frame.shape[:2]
			pixmap = QImage(cur_frame, width, height, QImage.Format_RGB888)
			pixmap = QPixmap.fromImage(pixmap)
			# 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
			ratio = max(width / self.ui.label_video_2.width(), height / self.ui.label_video_2.height())
			pixmap.setDevicePixelRatio(ratio)
			# 视频流置于label中间部分播放
			self.ui.label_video_2.setAlignment(Qt.AlignCenter)
			self.ui.label_video_2.setPixmap(pixmap)




	def photo_capture(self):

		time_tuple = time.localtime(time.time())
		path = self.file_path
		file_name = '{}.jpg'.format(self.ui.listWidget.count() + 1)
		print(path)

		ret, frame = self.cam.read()
		cv2.imshow('Video Cam', frame)
		ret2 = cv2.imwrite(path + '/' + file_name, frame)
		if ret2:
			print('拍照成功，图片已经存入工作目录，名称为:' + '{}_{}_{}_{}'.format(self.ui.comboBox.currentIndex(), time_tuple[2], time_tuple[3], time_tuple[4]))
			self.ui.listWidget.addItem(QListWidgetItem(QIcon(self.file_path + "/" + file_name), file_name))
			self.ui.img_all_num.setText(str(self.ui.listWidget.count()))
		else:
			print('拍照失败')



	def stitching_crashHandler(self, status):
		dlg = QMessageBox(self)
		dlg.setWindowTitle("拼接失败")
		fail_info = ["RUN！",
			"所选图片特征点不足无法拼接。\n请重新选择或添加更多图片！",
			"所选图片视角变化过大。\n请缩短扫描间距再重新拼接！",
			"未知错误，请重新选择图片或检查是否包含中文路径！",
			"请先选择所要拼接的图片！"]
		dlg.setText(fail_info[status])
		dlg.setStandardButtons(QMessageBox.Yes)
		dlg.setIcon(QMessageBox.Warning)
		btn = dlg.exec_()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainProgram()
	sys.exit(app.exec_())

