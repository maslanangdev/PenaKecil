# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import subprocess
import os
import ntpath

from PIL import Image

from pdf2image import convert_from_path

class Ui_MainWindow(object):
    def __init__(self):
        self.pdfList = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.queueList = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.queueList.setObjectName("queueList")
        self.verticalLayout_2.addWidget(self.queueList)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addPush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addPush.setObjectName("addPush")

        

        self.horizontalLayout_2.addWidget(self.addPush)
        
       
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.removeList = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.removeList.setObjectName("removeList")
        self.removeList.setText("Remove List")
        self.verticalLayout_2.addWidget(self.removeList)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.qualityCombo = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.qualityCombo.setPlaceholderText("")
        self.qualityCombo.setObjectName("qualityCombo")
        self.verticalLayout_2.addWidget(self.qualityCombo)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setText("DPI")
        self.verticalLayout_2.addWidget(self.label_6)
        self.specifyDPI = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.specifyDPI.setMaximum(10000)
        self.specifyDPI.setValue(300)
        self.verticalLayout_2.addWidget(self.specifyDPI)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputPath = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.outputPath.setObjectName("outputPath")
        self.horizontalLayout.addWidget(self.outputPath)
        self.outPush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.outPush.setObjectName("outPush")
        self.horizontalLayout.addWidget(self.outPush)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.exportPush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportPush.setEnabled(True)
        self.exportPush.setMinimumSize(QtCore.QSize(0, 40))
        self.exportPush.setObjectName("exportPush")
        self.horizontalLayout_5.addWidget(self.exportPush)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.removeList.clicked.connect(self.removeLEST)

  
  
        # formats = ["Screen (72 dpi)", 
        # "E-Book (150 dpi)", 
        # "Pre-Press (300 dpi)", 
        # "Printer (300 dpi)", 
        # "Default", 
        # "JPEG HIGH", 
        # "JPEG MEDIUM", 
        # "JPEG LOW"]

  
        formats = ["PDF", "JPEG"]
        
        for h in formats:
            self.qualityCombo.addItem(h)

        # self.qualityCombo.setCurrentText(_translate("MainWindow", "Select Quality"))
        # self.qualityCombo.setItemText(0, _translate("MainWindow", ""))
        # self.qualityCombo.setItemText(1, _translate("MainWindow", "E-Book (150 dpi)"))
        # self.qualityCombo.setItemText(2, _translate("MainWindow", ))
        # self.qualityCombo.setItemText(3, _translate("MainWindow", )
        # self.qualityCombo.setItemText(4, _translate("MainWindow", ))

        self.retranslateUi(MainWindow)
        self.qualityCombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addPush.clicked.connect(self.fileloader)
        self.exportPush.clicked.connect(self.GAAAASSSSSS)
        self.outPush.clicked.connect(self.folderbrowser)
        self.outputPath.setText(os.path.expanduser("~") + "\Documents")

    def removeLEST(self):
        self.queueList.clear()
        self.pdfList.clear()

    def fileloader(self):
        print("Open_FILE")
        fileList = QFileDialog.getOpenFileNames(MainWindow, "Select PDF Files", "C:\\", "Portable Document Format (*.pdf);; JPEG Picture (*.jpeg; *.jpg)")
        print(fileList)

        self.pdfList.extend(fileList[0])
        self.queueList.addItems(fileList[0])
        # for x in fileList[0]:
        #     self.queueList.addItem(x)

    def folderbrowser(self):
        print("Select_FOLDER")
        exDir = QFileDialog.getExistingDirectory(MainWindow, "Select Directory")
        self.outputPath.setText(exDir)


    def GAAAASSSSSS(self):
        being_process_thing_list = self.pdfList
        quality = self.specifyDPI.value()
        print("mengProses . . .")
        processed = 0
        if self.qualityCombo.currentText() == "PDF":
            for c in being_process_thing_list:
                filename = f"{self.outputPath.text()}\\{ntpath.basename(c)}"
                name, ext = os.path.splitext(filename)
                if ext == ".pdf":
                # if c[:-4] == ".pdf":
                    print(name+ext)
                    a = f'gs\\gs9.53.3\\bin\\gswin32c.exe -sDEVICE=pdfwrite -dCompabilityLevel=1.4 -dPDFSETTINGS=/default -r{quality} -dNOPAUSE -dBATCH -sOutputFile="{name}_Q{quality}.pdf" "{c}"'
                    print(a)
                    os.system(a)
                else:
                    img = Image.open(c)
                    img.save(f"{name}_Q-{quality}.pdf", quality=80, optimize=True, progressive=True)
                
                processed = processed + 1
                percentage = (processed/len(being_process_thing_list))*100
                self.progressBar.setValue(percentage)


        if self.qualityCombo.currentText() == "JPEG":
            for c in being_process_thing_list:
                filename = f"{self.outputPath.text()}\\{ntpath.basename(c)}"
                name, ext = os.path.splitext(filename)
                # pages = convert_from_path(f"{c}", poppler_path=r"poppler-21.03.0\Library\bin")
                # print(c)
                # for x in range(len(pages)):
                #     outName = f"{self.outputPath.text()}\\{ntpath.basename(c).split('.jp')}_page{str(x+1)}.jpg".replace("[", "").replace("]", "")
                #     print(str(x))
                #     pages[x].save(outName, 'JPEG')
                if ext == ".pdf":
                # if c[:-4] == ".pdf":

                    a = f'gs\\gs9.53.3\\bin\\gswin32c.exe -sDEVICE=jpeg -dNOPAUSE -dBATCH -r{quality} -sOutputFile="{name}_page-%03d_Q-{quality}.jpeg" "{c}"'
                    print(a)
                    os.system(a)

                else:
                    img = Image.open(c)
                    img.save(f"{name}_Q-{quality}.jpeg", quality=80, optimize=True, progressive=True)

                ext == ""
                    
                

                processed = processed + 1
                percentage = (processed/len(being_process_thing_list))*100
                self.progressBar.setValue(percentage) 


        

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PenaKecil - A Front-End to Adjust PDF Quality"))
        self.label.setText(_translate("MainWindow", "PenaKecil"))
        self.label_2.setText(_translate("MainWindow", "A simple Ghostscript front-end to adjust PDF quality"))
        self.label_5.setText(_translate("MainWindow", "Files Queue : "))
        self.addPush.setText(_translate("MainWindow", "Add File"))
        self.label_4.setText(_translate("MainWindow", "Output Format : "))
        self.outputPath.setPlaceholderText(_translate("MainWindow", "Output file path goes here...."))
        self.outPush.setText(_translate("MainWindow", "Browse"))
        self.exportPush.setText(_translate("MainWindow", "Export !"))
        self.label_3.setText(_translate("MainWindow", "PenaKecil 1.1 - PreAlpha0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# placeholder name for this project is CendolBakso

    '''
    Copyright (C) <2021>  <maslanang>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    '''



